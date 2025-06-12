# Python Bulk File Renamer Script 

import os 
import sys

def rename_files_in_bulk(folder_path, prefix):
    """
    Rename all files in the given folder with a custom prefix and serial numbers.
    """

    try:
        # Get and sort all items in the folder
        files = os.listdir(folder_path)
        files.sort()

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

                # Rename the file
                os.rename(old_path, new_path)

        print("✅ All files were renamed successfully.")

    except Exception as error:
        # Handle unexpected errors 
        print(f"❌ Error: {error}")

# Only runs when executed directly from CLI
if __name__ == "__main__":
    # Require exactly 2 arguments : folder path and prefix
    if len(sys.argv) != 3:
        print(f"Usage: python rename_bulk.py <folder_path> <prefix>.")

    else:
        rename_files_in_bulk(sys.argv[1], sys.argv[2])