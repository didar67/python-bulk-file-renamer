"""
Main application entry point for Bulk File Organizer.
Orchestrates the startup process by calling the CLI handler.
"""

import sys
from script.cli import run_cli

def main():
    """
    Entry point for the application.
    Recruiter Comment:
    - Keeps orchestration clean and decoupled from CLI logic.
    - Ready to integrate executor and config loader.
    """
    run_cli()

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"FATAL ERROR: Unhandled exception: {e}")
        sys.exit(1)
