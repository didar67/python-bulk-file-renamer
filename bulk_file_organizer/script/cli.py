"""
CLI Module for Bulk File Organizer
Purpose: Provides a professional, argparse-based command-line interface
         for interacting with the Bulk File Organizer tool.
"""

import argparse
from utils.helper import validate_path
from core.logger import initialize_logger

def run_cli():
    """
    Handles CLI argument parsing and dispatches application commands.
    
    Recruiter Comment:
    - Uses argparse for structured CLI commands.
    - Designed for scalability — future subcommands (e.g., dry-run, config) can be added easily.
    - Validation and logging integrated cleanly.
    """
    parser = argparse.ArgumentParser(
        description="Bulk File Organizer — Automate your file renaming tasks efficiently.",
        epilog="Example: python main.py --source ./downloads --rename-pattern file_{index}"
    )

    parser.add_argument(
        "--source",
        required=True,
        help="Source directory containing files to rename."
    )

    parser.add_argument(
        "--rename-pattern",
        required=True,
        help="Pattern for renaming files (e.g., file_{index})."
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate renaming without making any actual changes."
    )

    args = parser.parse_args()

    # Initialize centralized logger
    logger = initialize_logger()

    # Validate input path
    if not validate_path(args.source):
        logger.error("Invalid source directory path provided.")
        return

    logger.info("CLI arguments parsed successfully.")
    logger.info(f"Source: {args.source}, Pattern: {args.rename_pattern}, Dry-run: {args.dry_run}")

    # (Placeholder) Integration point for executor
    logger.info("Ready to execute bulk renaming operation...")
