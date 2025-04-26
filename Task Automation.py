import os
import shutil

# Set your download directory path
DOWNLOADS_DIR = "C:\\Users\\ba299\\Downloads"

# Define the folders and associated file types
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "PDFs": [".pdf"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Documents": [".docx", ".doc", ".txt", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi"],
}

def organize_files():
    # Get list of all files in downloads
    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)
        
        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        moved = False
        # Check each category
        for folder_name, extensions in FILE_CATEGORIES.items():
            if ext in extensions:
                destination_folder = os.path.join(DOWNLOADS_DIR, folder_name)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved: {filename} -> {folder_name}/")
                moved = True
                break
        
        # If file doesn't match any category
        if not moved:
            others_folder = os.path.join(DOWNLOADS_DIR, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} -> Others/")

if __name__ == "__main__":
    organize_files()
