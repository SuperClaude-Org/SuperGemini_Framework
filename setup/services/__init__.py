"""
SuperGemini Services Module
Business logic services for the SuperGemini installation system
"""

from .gemini_md import GEMINIMdService
from .config import ConfigService
from .files import FileService
from .settings import SettingsService

# Backward compatibility alias
CLAUDEMdService = GEMINIMdService

__all__ = [
    'GEMINIMdService',
    'CLAUDEMdService',  # Keep for backward compatibility
    'ConfigService', 
    'FileService',
    'SettingsService'
]