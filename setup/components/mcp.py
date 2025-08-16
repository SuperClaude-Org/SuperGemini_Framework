"""
MCP component for MCP server integration
"""

import subprocess
import sys
from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path

from ..base.component import Component
from ..utils.ui import display_info, display_warning


class MCPComponent(Component):
    """MCP servers integration component"""
    
    def __init__(self, install_dir: Optional[Path] = None):
        """Initialize MCP component"""
        super().__init__(install_dir)
        
        # Define MCP servers to install
        self.mcp_servers = {
            "sequential-thinking": {
                "name": "sequential-thinking",
                "description": "Multi-step problem solving and systematic analysis",
                "npm_package": "@modelcontextprotocol/server-sequential-thinking",
                "required": True
            },
            "context7": {
                "name": "context7", 
                "description": "Official library documentation and code examples",
                "npm_package": "@upstash/context7-mcp",
                "required": True
            },
            "magic": {
                "name": "magic",
                "description": "Modern UI component generation and design systems",
                "npm_package": "@21st-dev/magic",
                "required": False,
                "api_key_env": "TWENTYFIRST_API_KEY",
                "api_key_description": "21st.dev API key for UI component generation",
                "disabled_by_default": True,
                "disabled_reason": "Gemini API compatibility issues - function naming conflicts"
            },
            "playwright": {
                "name": "playwright",
                "description": "Cross-browser E2E testing and automation",
                "npm_package": "@playwright/mcp@latest",
                "required": False
            }
        }
    
    def get_metadata(self) -> Dict[str, str]:
        """Get component metadata"""
        return {
            "name": "mcp",
            "version": "3.2.2",
            "description": "MCP server integration (Context7, Sequential, Playwright active; Magic disabled by default)",
            "category": "integration"
        }
    
    def validate_prerequisites(self, installSubPath: Optional[Path] = None) -> Tuple[bool, List[str]]:
        """Check prerequisites"""
        errors = []
        
        # Check if Node.js is available
        try:
            result = subprocess.run(
                ["node", "--version"], 
                capture_output=True, 
                text=True, 
                timeout=10,
                shell=(sys.platform == "win32")
            )
            if result.returncode != 0:
                errors.append("Node.js not found - required for MCP servers")
            else:
                version = result.stdout.strip()
                self.logger.debug(f"Found Node.js {version}")
                
                # Check version (require 18+)
                try:
                    version_num = int(version.lstrip('v').split('.')[0])
                    if version_num < 18:
                        errors.append(f"Node.js version {version} found, but version 18+ required")
                except:
                    self.logger.warning(f"Could not parse Node.js version: {version}")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            errors.append("Node.js not found - required for MCP servers")
        
        # Check if Gemini CLI is available
        try:
            result = subprocess.run(
                ["gemini", "--version"], 
                capture_output=True, 
                text=True, 
                timeout=10,
                shell=(sys.platform == "win32")
            )
            if result.returncode != 0:
                errors.append("Gemini CLI not found - required for MCP server management")
            else:
                version = result.stdout.strip()
                self.logger.debug(f"Found Gemini CLI {version}")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            errors.append("Gemini CLI not found - required for MCP server management")
        
        # Check if npm is available
        try:
            result = subprocess.run(
                ["npm", "--version"], 
                capture_output=True, 
                text=True, 
                timeout=10,
                shell=(sys.platform == "win32")
            )
            if result.returncode != 0:
                errors.append("npm not found - required for MCP server installation")
            else:
                version = result.stdout.strip()
                self.logger.debug(f"Found npm {version}")
        except (subprocess.TimeoutExpired, FileNotFoundError):
            errors.append("npm not found - required for MCP server installation")
        
        return len(errors) == 0, errors
    
    def get_files_to_install(self) -> List[Tuple[Path, Path]]:
        """Get files to install (none for MCP component)"""
        return []
    
    def get_metadata_modifications(self) -> Dict[str, Any]:
        """Get metadata modifications for MCP component"""
        return {
            "components": {
                "mcp": {
                    "version": "3.2.2",
                    "installed": True,
                    "servers_count": len(self.mcp_servers)
                }
            },
            "mcp": {
                "enabled": True,
                "servers": list(self.mcp_servers.keys()),
                "auto_update": False
            }
        }
    
    def _check_mcp_server_installed(self, server_name: str) -> bool:
        """Check if MCP server is already configured in settings.json"""
        try:
            settings_path = self.install_dir / "settings.json"
            if not settings_path.exists():
                return False
            
            import json
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            
            # Check if server is in mcpServers section
            if "mcpServers" in settings:
                return server_name in settings["mcpServers"]
            
            return False
            
        except Exception as e:
            self.logger.warning(f"Error checking MCP server status: {e}")
            return False
    
    def _configure_mcp_server_in_settings(self, server_name: str, server_info: Dict[str, Any]) -> bool:
        """Configure MCP server in Gemini settings.json"""
        try:
            settings_path = self.install_dir / "settings.json"
            
            # Load existing settings or create new
            settings = {}
            if settings_path.exists():
                import json
                with open(settings_path, 'r') as f:
                    settings = json.load(f)
            
            # Determine target section based on disabled_by_default flag
            is_disabled_by_default = server_info.get("disabled_by_default", False)
            target_section = "_disabledMcpServers" if is_disabled_by_default else "mcpServers"
            
            # Ensure target section exists
            if target_section not in settings:
                settings[target_section] = {}
            
            # Add comments for disabled section
            if is_disabled_by_default and "_comment" not in settings[target_section]:
                settings[target_section]["_comment"] = f"{server_info['description']} - disabled due to compatibility issues"
                settings[target_section]["_instructions"] = f"Reason: {server_info.get('disabled_reason', 'Compatibility issues')}. Move to mcpServers section to enable."
            
            # Configure the server
            npm_package = server_info["npm_package"]
            command_mapping = {
                "@modelcontextprotocol/server-sequential-thinking": "npx",
                "@upstash/context7-mcp": "npx",
                "@21st-dev/magic": "npx",
                "@playwright/mcp": "npx"
            }
            
            command = command_mapping.get(npm_package, "npx")
            server_config = {
                "command": command,
                "args": ["-y", npm_package]
            }
            
            # Add environment variables if needed
            if "api_key_env" in server_info:
                import os
                api_key_value = os.getenv(server_info["api_key_env"])
                if api_key_value:
                    server_config["env"] = {
                        server_info["api_key_env"]: api_key_value
                    }
                else:
                    server_config["env"] = {}
            
            # Add to appropriate settings section
            settings[target_section][server_name] = server_config
            
            # Save settings
            import json
            with open(settings_path, 'w') as f:
                json.dump(settings, f, indent=2)
            
            status = "disabled" if is_disabled_by_default else "enabled"
            self.logger.debug(f"Configured {server_name} as {status} in settings.json")
            return True
            
        except Exception as e:
            self.logger.error(f"Error configuring MCP server in settings: {e}")
            return False
    
    def _install_mcp_server(self, server_info: Dict[str, Any], config: Dict[str, Any]) -> bool:
        """Install a single MCP server via npm and configure in settings.json"""
        server_name = server_info["name"]
        npm_package = server_info["npm_package"]
        
        try:
            self.logger.info(f"Installing MCP server: {server_name}")
            
            # Handle API key requirements
            if "api_key_env" in server_info:
                api_key_env = server_info["api_key_env"]
                api_key_desc = server_info.get("api_key_description", f"API key for {server_name}")
                
                if not config.get("dry_run", False):
                    display_info(f"MCP server '{server_name}' requires an API key")
                    display_info(f"Environment variable: {api_key_env}")
                    display_info(f"Description: {api_key_desc}")
                    
                    # Check if API key is already set
                    import os
                    if not os.getenv(api_key_env):
                        display_warning(f"API key {api_key_env} not found in environment")
                        self.logger.warning(f"Proceeding without {api_key_env} - server may not function properly")
            
            # Install via npm globally
            if config.get("dry_run"):
                self.logger.info(f"Would install MCP server via npm: npm install -g {npm_package}")
                return True
            
            self.logger.debug(f"Running: npm install -g {npm_package}")
            
            result = subprocess.run(
                ["npm", "install", "-g", npm_package],
                capture_output=True,
                text=True,
                timeout=180,  # 3 minutes timeout for installation
                shell=(sys.platform == "win32")
            )
            
            if result.returncode == 0:
                self.logger.success(f"Successfully installed npm package: {npm_package}")
                
                # Configure in settings.json
                if self._configure_mcp_server_in_settings(server_name, server_info):
                    self.logger.success(f"Successfully configured MCP server: {server_name}")
                    return True
                else:
                    self.logger.error(f"Failed to configure MCP server {server_name} in settings.json")
                    return False
            else:
                error_msg = result.stderr.strip() if result.stderr else "Unknown error"
                self.logger.error(f"Failed to install npm package {npm_package}: {error_msg}")
                return False
                
        except subprocess.TimeoutExpired:
            self.logger.error(f"Timeout installing MCP server {server_name}")
            return False
        except Exception as e:
            self.logger.error(f"Error installing MCP server {server_name}: {e}")
            return False
    
    def _uninstall_mcp_server(self, server_name: str) -> bool:
        """Remove MCP server from settings.json"""
        try:
            self.logger.info(f"Removing MCP server configuration: {server_name}")
            
            settings_path = self.install_dir / "settings.json"
            if not settings_path.exists():
                self.logger.info(f"No settings.json found, nothing to remove")
                return True
            
            import json
            with open(settings_path, 'r') as f:
                settings = json.load(f)
            
            # Remove from mcpServers if exists
            if "mcpServers" in settings and server_name in settings["mcpServers"]:
                del settings["mcpServers"][server_name]
                
                # Keep empty mcpServers section to preserve user's configuration structure
                # Don't delete the section even if empty, in case user has other servers
                
                # Save updated settings
                with open(settings_path, 'w') as f:
                    json.dump(settings, f, indent=2)
                
                self.logger.success(f"Successfully removed MCP server configuration: {server_name}")
            else:
                self.logger.info(f"MCP server {server_name} not found in configuration")
            
            return True
                
        except Exception as e:
            self.logger.error(f"Error removing MCP server configuration: {e}")
            return False
    
    def _install(self, config: Dict[str, Any]) -> bool:
        """Install MCP component"""
        self.logger.info("Installing SuperGemini MCP servers...")
        self.logger.info("Note: Some servers may be disabled by default due to compatibility issues")

        # Validate prerequisites
        success, errors = self.validate_prerequisites()
        if not success:
            for error in errors:
                self.logger.error(error)
            return False

        # Install each MCP server
        installed_count = 0
        failed_servers = []

        for server_name, server_info in self.mcp_servers.items():
            if self._install_mcp_server(server_info, config):
                installed_count += 1
            else:
                failed_servers.append(server_name)
                
                # Check if this is a required server
                if server_info.get("required", False):
                    self.logger.error(f"Required MCP server {server_name} failed to install")
                    return False

        # Verify installation
        if not config.get("dry_run", False):
            self.logger.info("Verifying MCP server configuration...")
            try:
                settings_path = self.install_dir / "settings.json"
                if settings_path.exists():
                    import json
                    with open(settings_path, 'r') as f:
                        settings = json.load(f)
                    
                    if "mcpServers" in settings:
                        self.logger.debug("Configured MCP servers:")
                        for server_name, server_config in settings["mcpServers"].items():
                            self.logger.debug(f"  {server_name}: {server_config.get('command')} {' '.join(server_config.get('args', []))}")
                    else:
                        self.logger.warning("No MCP servers found in configuration")
                else:
                    self.logger.warning("Settings.json not found")
                    
            except Exception as e:
                self.logger.warning(f"Could not verify MCP configuration: {e}")

        if failed_servers:
            self.logger.warning(f"Some MCP servers failed to install: {failed_servers}")
            self.logger.success(f"MCP component partially installed ({installed_count} servers)")
        else:
            self.logger.success(f"MCP component installed successfully ({installed_count} servers)")

        return self._post_install()

    def _post_install(self) -> bool:
        # Update metadata
        try:
            metadata_mods = self.get_metadata_modifications()
            self.settings_manager.update_metadata(metadata_mods)

            # Add component registration to metadata
            self.settings_manager.add_component_registration("mcp", {
                "version": "3.2.2",
                "category": "integration",
                "servers_count": len(self.mcp_servers)
            })

            self.logger.info("Updated metadata with MCP component registration")
        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False

        return True

    
    def uninstall(self) -> bool:
        """Uninstall MCP component - preserves user's MCP servers"""
        try:
            self.logger.info("Preserving MCP servers for continued use...")
            
            # We intentionally DO NOT remove MCP servers from settings.json
            # Users may want to keep using them with Gemini CLI
            self.logger.info("MCP servers preserved in settings.json")
            
            # Only update metadata to remove component registration
            try:
                if self.settings_manager.is_component_installed("mcp"):
                    self.settings_manager.remove_component_registration("mcp")
                    # Remove MCP metadata but keep actual server configurations
                    metadata = self.settings_manager.load_metadata()
                    if "mcp" in metadata:
                        del metadata["mcp"]
                        self.settings_manager.save_metadata(metadata)
                    self.logger.info("Removed MCP component from metadata (servers preserved)")
            except Exception as e:
                self.logger.warning(f"Could not update metadata: {e}")
            
            self.logger.success("MCP component uninstalled (servers preserved for continued use)")
            return True
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during MCP uninstallation: {e}")
            return False
    
    def get_dependencies(self) -> List[str]:
        """Get dependencies"""
        return ["core"]
    
    def update(self, config: Dict[str, Any]) -> bool:
        """Update MCP component"""
        try:
            self.logger.info("Updating SuperGemini MCP servers...")
            
            # Check current version
            current_version = self.settings_manager.get_component_version("mcp")
            target_version = self.get_metadata()["version"]
            
            if current_version == target_version:
                self.logger.info(f"MCP component already at version {target_version}")
                return True
            
            self.logger.info(f"Updating MCP component from {current_version} to {target_version}")
            
            # For MCP servers, update means reinstall to get latest versions
            updated_count = 0
            failed_servers = []
            
            for server_name, server_info in self.mcp_servers.items():
                try:
                    # Uninstall old version
                    if self._check_mcp_server_installed(server_name):
                        self._uninstall_mcp_server(server_name)
                    
                    # Install new version
                    if self._install_mcp_server(server_info, config):
                        updated_count += 1
                    else:
                        failed_servers.append(server_name)
                        
                except Exception as e:
                    self.logger.error(f"Error updating MCP server {server_name}: {e}")
                    failed_servers.append(server_name)
            
            # Update metadata
            try:
                # Update component version in metadata
                metadata = self.settings_manager.load_metadata()
                if "components" in metadata and "mcp" in metadata["components"]:
                    metadata["components"]["mcp"]["version"] = target_version
                    metadata["components"]["mcp"]["servers_count"] = len(self.mcp_servers)
                if "mcp" in metadata:
                    metadata["mcp"]["servers"] = list(self.mcp_servers.keys())
                self.settings_manager.save_metadata(metadata)
            except Exception as e:
                self.logger.warning(f"Could not update metadata: {e}")
            
            if failed_servers:
                self.logger.warning(f"Some MCP servers failed to update: {failed_servers}")
                return False
            else:
                self.logger.success(f"MCP component updated to version {target_version}")
                return True
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during MCP update: {e}")
            return False
    
    def validate_installation(self) -> Tuple[bool, List[str]]:
        """Validate MCP component installation"""
        errors = []
        
        # Check metadata registration
        if not self.settings_manager.is_component_installed("mcp"):
            errors.append("MCP component not registered in metadata")
            return False, errors
        
        # Check version matches
        installed_version = self.settings_manager.get_component_version("mcp")
        expected_version = self.get_metadata()["version"]
        if installed_version != expected_version:
            errors.append(f"Version mismatch: installed {installed_version}, expected {expected_version}")
        
        # Check if required servers are configured
        try:
            settings_path = self.install_dir / "settings.json"
            if not settings_path.exists():
                errors.append("Settings.json not found")
            else:
                import json
                with open(settings_path, 'r') as f:
                    settings = json.load(f)
                
                if "mcpServers" not in settings:
                    errors.append("No MCP servers configured in settings.json")
                else:
                    # Check if required servers are configured
                    for server_name, server_info in self.mcp_servers.items():
                        if server_info.get("required", False):
                            if server_name not in settings["mcpServers"]:
                                errors.append(f"Required MCP server not configured: {server_name}")
                            
        except Exception as e:
            errors.append(f"Could not verify MCP server configuration: {e}")
        
        return len(errors) == 0, errors
    
    def _get_source_dir(self):
        """Get source directory for framework files"""
        return None

    def get_size_estimate(self) -> int:
        """Get estimated installation size"""
        # MCP servers are installed via npm, estimate based on typical sizes
        base_size = 50 * 1024 * 1024  # ~50MB for all servers combined
        return base_size
    
    def get_installation_summary(self) -> Dict[str, Any]:
        """Get installation summary"""
        return {
            "component": self.get_metadata()["name"],
            "version": self.get_metadata()["version"],
            "servers_count": len(self.mcp_servers),
            "mcp_servers": list(self.mcp_servers.keys()),
            "estimated_size": self.get_size_estimate(),
            "dependencies": self.get_dependencies(),
            "required_tools": ["node", "npm", "gemini"]
        }
