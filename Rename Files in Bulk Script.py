# Python Bulk File Renamer Script 
# Purpose: Rename all files in a specified folder by adding a custom prefix and serial numbers.

import os 
import sys
import logging
import argparse

def setup_logger(custom_level=logging.INFO):
    """ Set up logger for the script """
    logging.basicConfig(
        level = custom_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )
    

def rename_files_in_bulk(folder_path: str, prefix: str) -> None:
    """
    Rename all files in the given folder with a custom prefix and serial numbers.
    """

    try:
        logging.info(f"Scanning folder {folder_path}")

        # Get and sort all items in the folder
        files = os.listdir(folder_path)
        files.sort()
        total_renamed = 0

        # Loop through files with index starting at 1
        for index, filename in enumerate(files, start=1):
            old_path = os.path.join(folder_path,filename)

            # Rename only if it's a file
            if os.path.isfile(old_path):
                # File extension (e.g., '.txt', '.jpg')
                extension = os.path.splitext(filename)[1]
                
                # Build the new filename 
                new_filename = f"{prefix}_{index:03d}{extension}"
                new_path = os.path.join(folder_path,new_filename)

                logging.debug(f"Renaming {filename} -> {new_filename}")

                # Rename the file
                os.rename(old_path, new_path)
                total_renamed += 1  # Increment counter

        logging.info(f"Successfully renamed {total_renamed} files.")

    
    except FileNotFoundError:
        logging.error(f"Folder not found {folder_path}")

    except PermissionError:
        logging.error(f"Can not rename file in {folder_path}")

    except Exception as error:
        # Handle unexpected errors 
        logging.error(f"❌ Error: {error}")

def parse_arg():
    """ Parse command line arguments using argparse."""
    parser= argparse.ArgumentParser(description='Bulk rename files in a folder with a custom prefix and serial numbers.')
    parser.add_argument("folder_path", help="Path of the folder")
    parser.add_argument("prefix", help="prefix to prepend to all files.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging.")
    
    return parser.parse_args()


# Only runs when executed directly from CLI
if __name__ == "__main__":
    args = parse_arg()

    # Set logging level based on verbose flag
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logger(log_level)

    logging.debug(f"Arguments received: folder_path={args.folder_path}, prefix={args.prefix}")
    rename_files_in_bulk(args.folder_path, args.prefix)

    # Final confirmation message
    logging.info("✅ Bulk renaming operation completed successfully.")