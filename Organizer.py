import os

import shutil

# Dictionary to map file extensions to their respective folder names

EXTENSIONS = {

    ".mp4": "Videos",

    ".mp3": "Audio",

    ".pdf": "Books",

    # Add more extensions and folder names as needed

}

# Path to the Downloads folder

DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

def organize_files():

    for filename in os.listdir(DOWNLOADS_PATH):

        file_path = os.path.join(DOWNLOADS_PATH, filename)

        if os.path.isfile(file_path):

            # Get the file extension

            _, extension = os.path.splitext(filename)

            # Check if the file extension is in the dictionary

            if extension in EXTENSIONS:

                # Get the folder name for the extension

                folder_name = EXTENSIONS[extension]

                # Create the folder if it doesn't exist

                folder_path = os.path.join(DOWNLOADS_PATH, folder_name)

                if not os.path.exists(folder_path):

                    os.makedirs(folder_path)

                # Move the file to the folder

                new_file_path = os.path.join(folder_path, filename)

                shutil.move(file_path, new_file_path)

if __name__ == "__main__":

    organize_files()

    print("Files organized successfully!")

