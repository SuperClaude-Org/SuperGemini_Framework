"""
Modes component for SuperGemini behavioral modes
"""

from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path

from ..core.base import Component
from ..services.gemini_md import GEMINIMdService


class ModesComponent(Component):
    """SuperGemini behavioral modes component"""
    
    def __init__(self, install_dir: Optional[Path] = None):
        """Initialize modes component"""
        super().__init__(install_dir, Path(""))
    
    def get_metadata(self) -> Dict[str, str]:
        """Get component metadata"""
        return {
            "name": "modes",
            "version": "4.0.3",
            "description": "SuperGemini behavioral modes (Brainstorming, Introspection, Task Management, Token Efficiency)",
            "category": "modes"
        }
    
    def _install(self, config: Dict[str, Any]) -> bool:
        """Install modes component"""
        self.logger.info("Installing SuperGemini behavioral modes...")

        # Validate installation
        success, errors = self.validate_prerequisites()
        if not success:
            for error in errors:
                self.logger.error(error)
            return False

        # Get files to install
        files_to_install = self.get_files_to_install()

        if not files_to_install:
            self.logger.warning("No mode files found to install")
            return False

        # Copy mode files
        success_count = 0
        for source, target in files_to_install:
            self.logger.debug(f"Copying {source.name} to {target}")
            
            if self.file_manager.copy_file(source, target):
                success_count += 1
                self.logger.debug(f"Successfully copied {source.name}")
            else:
                self.logger.error(f"Failed to copy {source.name}")

        if success_count != len(files_to_install):
            self.logger.error(f"Only {success_count}/{len(files_to_install)} mode files copied successfully")
            return False

        self.logger.success(f"Modes component installed successfully ({success_count} mode files)")

        return self._post_install()

    def _post_install(self) -> bool:
        """Post-installation tasks"""
        try:
            # Update metadata
            metadata_mods = {
                "components": {
                    "modes": {
                        "version": "4.0.3",
                        "installed": True,
                        "files_count": len(self.component_files)
                    }
                }
            }
            self.settings_manager.update_metadata(metadata_mods)
            self.logger.info("Updated metadata with modes component registration")
            
            # Add component registration
            self.settings_manager.add_component_registration("modes", {
                "version": "4.0.3",
                "category": "modes",
                "files_count": len(self.component_files)
            })
            self.logger.info("Registered modes component in metadata")
            
            # Update GEMINI.md with mode imports
            try:
                manager = GEMINIMdService(self.install_dir)
                manager.add_imports(self.component_files, category="Behavioral Modes")
                self.logger.info("Updated GEMINI.md with mode imports")
            except Exception as e:
                self.logger.warning(f"Failed to update GEMINI.md with mode imports: {e}")
                # Don't fail the whole installation for this
            
            return True
        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False
    
    def uninstall(self) -> bool:
        """Uninstall modes component"""
        try:
            self.logger.info("Uninstalling SuperGemini modes component...")
            
            # Remove mode files
            removed_count = 0
            for _, target in self.get_files_to_install():
                if self.file_manager.remove_file(target):
                    removed_count += 1
                    self.logger.debug(f"Removed {target.name}")
            
            # Remove modes directory if empty
            try:
                if self.install_component_subdir.exists():
                    remaining_files = list(self.install_component_subdir.iterdir())
                    if not remaining_files:
                        self.install_component_subdir.rmdir()
                        self.logger.debug("Removed empty modes directory")
            except Exception as e:
                self.logger.warning(f"Could not remove modes directory: {e}")
            
            # Update settings.json
            try:
                if self.settings_manager.is_component_installed("modes"):
                    self.settings_manager.remove_component_registration("modes")
                    self.logger.info("Removed modes component from settings.json")
            except Exception as e:
                self.logger.warning(f"Could not update settings.json: {e}")
            
            self.logger.success(f"Modes component uninstalled ({removed_count} files removed)")
            return True
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during modes uninstallation: {e}")
            return False
    
    def get_dependencies(self) -> List[str]:
        """Get dependencies"""
        return ["core"]
    
    def _get_source_dir(self) -> Optional[Path]:
        """Get source directory for mode files"""
        # Assume we're in SuperGemini/setup/components/modes.py
        # and mode files are in SuperGemini/SuperGemini/Modes/
        project_root = Path(__file__).parent.parent.parent
        modes_dir = project_root / "SuperGemini" / "Modes"
        
        # Return None if directory doesn't exist to prevent warning
        if not modes_dir.exists():
            return None
        
        return modes_dir
    
    def _discover_component_files(self) -> List[str]:
        """
        Discover MODE files, excluding Gemini CLI incompatible ones
        
        Filters out MODE files that require parallel agents or features not supported by Gemini CLI
        """
        source_dir = self._get_source_dir()
        
        if not source_dir:
            return []
        
        # Gemini CLI compatible MODE files only
        gemini_compatible_modes = [
            'MODE_Brainstorming.md',      # Uses dialogue patterns only
            'MODE_Introspection.md',      # Uses self-analysis only  
            'MODE_Task_Management.md',    # Uses MCP memory (works)
            'MODE_Token_Efficiency.md'   # Uses compression patterns only
        ]
        
        # Gemini CLI incompatible MODE files (require parallel agents)
        gemini_incompatible_modes = [
            'MODE_Orchestration.md'       # Requires parallel execution, delegation
        ]
        
        discovered_files = []
        
        try:
            if not source_dir.exists():
                self.logger.warning(f"Modes source directory not found: {source_dir}")
                return []
            
            # Check which compatible files actually exist
            for mode_file in gemini_compatible_modes:
                file_path = source_dir / mode_file
                if file_path.exists():
                    discovered_files.append(mode_file)
                    self.logger.debug(f"Found compatible MODE file: {mode_file}")
                else:
                    self.logger.warning(f"Compatible MODE file not found: {mode_file}")
            
            # Log excluded files for transparency
            for mode_file in gemini_incompatible_modes:
                file_path = source_dir / mode_file
                if file_path.exists():
                    self.logger.info(f"Excluding incompatible MODE file: {mode_file} (requires parallel agents)")
            
            self.logger.info(f"Selected {len(discovered_files)} Gemini CLI compatible MODE files")
            
            return sorted(discovered_files)
            
        except Exception as e:
            self.logger.error(f"Error discovering MODE files: {e}")
            return []

    def get_size_estimate(self) -> int:
        """Get estimated installation size"""
        source_dir = self._get_source_dir()
        total_size = 0
        
        if source_dir and source_dir.exists():
            for filename in self.component_files:
                file_path = source_dir / filename
                if file_path.exists():
                    total_size += file_path.stat().st_size
        
        # Minimum size estimate
        total_size = max(total_size, 20480)  # At least 20KB
        
        return total_size