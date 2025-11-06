"""
Executor module for Bulk File Organizer
Author: Didarul Islam
Purpose: Implements the core file renaming logic in a modular and testable way.
"""

import os
import shutil
from core.logger import initialize_logger
from utils.helper import validate_folder_path

class BulkFileRenamer:
    """
    Class to handle bulk renaming of files with dry-run support.
    """

    def __init__(self, folder_path: str, pattern: str, dry_run: bool = False):
        """
        Initializes the BulkFileRenamer.

        Args:
            folder_path (str): Target folder path.
            pattern (str): Pattern for renaming, e.g., "file_{index}".
            dry_run (bool): If True, simulate renaming without actual file changes.
        """
        self.folder_path = folder_path
        self.pattern = pattern
        self.dry_run = dry_run
        self.logger = initialize_logger()

    def rename_files(self, logger) -> dict:
        """
        Rename files in bulk with dry-run support.
        Recruiter Comment:
        - Dry-run ensures safe testing before actual rename.
        """
        try:
            validate_folder_path(self.folder_path)
            files = sorted(os.listdir(self.folder_path))
            total_renamed = 0

            for idx, filename in enumerate(files, start=1):
                old_path = os.path.join(self.folder_path, filename)
                if os.path.isfile(old_path):
                    extension = os.path.splitext(filename)[1]
                    new_filename = self.pattern.replace("{index}", f"_{idx:03d}") + extension
                    new_path = os.path.join(self.folder_path, new_filename)

                    if self.dry_run:
                        logger.info(f"[DRY-RUN] {filename} -> {new_filename}")
                    else:
                        shutil.move(old_path, new_path)
                        logger.info(f"Renamed {filename} -> {new_filename}")
                    total_renamed += 1

            logger.info(f"✅ Total files renamed: {total_renamed}")
            return {"renamed_count": total_renamed, "error": None}

        except FileNotFoundError as e:
            logger.error(f"Folder not found: {self.folder_path}")
            return {"renamed_count": 0, "error": str(e)}
        except PermissionError as e:
            logger.error(f"Permission denied in folder: {self.folder_path}")
            return {"renamed_count": 0, "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {"renamed_count": 0, "error": str(e)}
