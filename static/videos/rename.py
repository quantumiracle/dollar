import os

def rename_files_in_folders(folder_path):
    try:
        # Walk through the directory structure
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                # Check if the file name contains spaces
                if ' ' in filename:
                    # Create a new filename by replacing spaces with underscores
                    new_filename = filename.replace(' ', '_')
                    # Construct full file paths
                    old_file_path = os.path.join(root, filename)
                    new_file_path = os.path.join(root, new_filename)
                    # Rename the file
                    os.rename(old_file_path, new_file_path)
                    print(f'Renamed: "{old_file_path}" -> "{new_file_path}"')
        print("All files have been renamed.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the root folder path to rename files recursively
folder_path = "top_samples"  # Change to your folder path
rename_files_in_folders(folder_path)
