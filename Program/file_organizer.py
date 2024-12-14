import os
import shutil

# Function to organize the files
def organize_files(directory):
    # List all files in the directory
    files = os.listdir(directory)
    
    # Iterate over the found files
    for file in files:
        # Get the full path of the file
        file_path = os.path.join(directory, file)
        
        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            # Get the file extension
            extension = file.split('.')[-1]
            
            # Create a folder for the extension, if it doesn't exist
            destination_folder = os.path.join(directory, extension)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Move the file to the corresponding folder
            shutil.move(file_path, os.path.join(destination_folder, file))
            print(f'File {file} moved to the {extension} folder')

# Define the directory to be organized
directory = 'path/to/your/directory'  # Replace with the desired directory
organize_files(directory)
