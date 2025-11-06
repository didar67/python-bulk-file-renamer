"""
Executor module for Bulk File Organizer
Author: Didarul Islam
Purpose: Implements the core file renaming logic in a modular and testable way.
"""

import os
import shutil
from core.logger import initialize_logger
from utils.helper import validate_folder_path

class FileRenamer:
    """
    Class to handle bulk renaming of files with dry-run support.
    """

    def __init__(self, folder_path: str, prefix: str, dry_run: bool = False):
        """
        Initializes the FileRenamer.
        
        Args:
            folder_path (str): Target folder path.
            prefix (str): Prefix to prepend to files.
            dry_run (bool): If True, simulate renaming without actual file changes.
        """
        self.folder_path = folder_path
        self.prefix = prefix
        self.dry_run = dry_run
        self.logger = initialize_logger()

    async def rename_files(self) -> None:
        """
        Rename files in bulk asynchronously with dry-run support.
        Recruiter Comment:
        - Dry-run ensures safe testing before actual rename.
        - Async allows integration with other async operations if needed.
        """
        try:
            validate_folder_path(self.folder_path)
            files = sorted(os.listdir(self.folder_path))
            total_renamed = 0

            for idx, filename in enumerate(files, start=1):
                old_path = os.path.join(self.folder_path, filename)
                if os.path.isfile(old_path):
                    extension = os.path.splitext(filename)[1]
                    new_filename = f"{self.prefix}_{idx:03d}{extension}"
                    new_path = os.path.join(self.folder_path, new_filename)

                    if self.dry_run:
                        self.logger.info(f"[DRY-RUN] {filename} -> {new_filename}")
                    else:
                        shutil.move(old_path, new_path)
                        self.logger.info(f"Renamed {filename} -> {new_filename}")
                        total_renamed += 1

            self.logger.info(f"✅ Total files renamed: {total_renamed}")

        except FileNotFoundError:
            self.logger.error(f"Folder not found: {self.folder_path}")
        except PermissionError:
            self.logger.error(f"Permission denied in folder: {self.folder_path}")
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
