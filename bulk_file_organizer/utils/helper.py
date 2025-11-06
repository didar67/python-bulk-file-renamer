"""
Helper Module for Bulk File Organizer
Purpose: Provides reusable helper utilities for path validation 
         and future automation features.
"""

import os

def validate_path(path: str) -> bool:
    """
    Validates whether the provided path exists and is a directory.

    Args:
        path (str): The directory path to validate.

    Returns:
        bool: True if valid directory, False otherwise.

    Recruiter Comment:
    - Keeps CLI clean by offloading common logic.
    - Future-proof for adding file existence or permission checks.
    """
    return os.path.exists(path) and os.path.isdir(path)
