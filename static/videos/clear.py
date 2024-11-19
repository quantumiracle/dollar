import os

def delete_images_in_folder(folder_path):
    """
    Recursively deletes all .jpg and .gif files in a folder and its subfolders.
    Args:
        folder_path (str): Path to the root folder.
    """
    for root, _, files in os.walk(folder_path):
        for filename in files:
            # Check if the file is a .jpg or .gif
            if filename.lower().endswith((".jpg", ".gif")):
                file_path = os.path.join(root, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")

# Specify the root folder containing files
root_folder = "./"  # Replace with your folder path
delete_images_in_folder(root_folder)
