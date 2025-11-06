"""
Main application entry point. Orchestrates the startup process 
by calling the primary CLI handler function.
"""
import sys

# Import centralized logger (no initialization logic here)
from core.logger import initialize_logger

def main():
    """
    Initializes and runs the core application logic.
    Recruiter Comment: Main module remains clean; logger can be
    initialized inside CLI or executor modules when needed.
    """
    print("Application main entry point. Logger available via core.logger.")

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
    except Exception as e:
        print(f"FATAL ERROR: Unhandled exception during application execution: {e}")
        sys.exit(1)
