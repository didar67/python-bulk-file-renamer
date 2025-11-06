"""
Helper Module for Bulk File Organizer
Purpose: Provides reusable helper utilities for path validation 
         and future automation features.
"""

import os

def validate_folder_path(path: str) -> None:
    """
    Validates the existence of a folder path.
    
    Args:
        path (str): Folder path to validate.
    
    Raises:
        FileNotFoundError: If folder does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Folder does not exist: {path}")
