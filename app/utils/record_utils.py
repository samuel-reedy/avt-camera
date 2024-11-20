import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_recording_folder(base_folder_name):
    base_path = os.path.join("Recordings", base_folder_name)
    folder_path = base_path + "_1"
    counter = 1

    logging.info(f"Creating recording folder with base path: {base_path}")

    # Check if the folder exists and if it's not empty, increment the name
    while os.path.exists(folder_path) and os.listdir(folder_path):
        logging.info(f"Folder {folder_path} already exists and is not empty. Incrementing counter.")
        counter += 1
        folder_path = f"{base_path}_{counter}"

    # Create the folder
    os.makedirs(folder_path, exist_ok=True)
    logging.info(f"Folder created at path: {folder_path}")
    return folder_path