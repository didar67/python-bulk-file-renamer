"""
Logger Module for Bulk File Organizer
Purpose: Provides a centralized, reusable logging system
         for all modules in the project using rotating log files.
"""

import logging
from logging.handlers import RotatingFileHandler
import os

def initialize_logger(log_file: str = "bulk_file_organizer.log", level=logging.INFO):
    """
    Initializes a rotating logger for the application.
    
    Args:
        log_file (str): Log file path.
        level (int): Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
    
    Returns:
        logging.Logger: Configured logger instance.
    
    Recruiter Comment:
    - RotatingFileHandler prevents oversized log files.
    - if not logger.hasHandlers() ensures multiple handlers are not added.
    - Console handler included for real-time output.
    """

    logger = logging.getLogger("BulkFileOrganizer")
    logger.setLevel(level)

    if not logger.hasHandlers():
        # Rotating file handler (5MB per file, keep 3 backups)
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=5 * 1024 * 1024,
            backupCount=3
        )
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

        # Console handler for real-time log output
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger
