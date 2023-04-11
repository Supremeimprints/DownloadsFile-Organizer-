# DownloadsFile-Organizer-
Automatic file organizer for files in the downloads folder
The script defines a dictionary EXTENSIONS that maps file extensions to their respective folder names.

The script defines a constant DOWNLOADS_PATH that contains the path to the Downloads folder.

The organize_files function loops through all files in the Downloads folder and checks if each file is a file (not a folder) and if its extension is in the EXTENSIONS dictionary.

If the file matches, the function gets the folder name for the extension from the EXTENSIONS dictionary and creates the folder if it doesn't already exist.

Finally, the function moves the file to the appropriate folder.

You can run this script from the command line by navigating to the directory containing the script and running python script_name.py.
