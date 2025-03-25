import os
import subprocess
import time
import shutil


def delete_subfolders_with_fieldmap(root_folder):
    for foldername in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, foldername)
        fieldmap_file_path = os.path.join(folder_path, "lists", "pp", "FieldMap.ppg")
        if os.path.exists(fieldmap_file_path):
            print(f"Deleting subfolder: {folder_path}")
            shutil.rmtree(folder_path)
            # Uncomment the line above only when you're sure you want to delete
            # Be cautious with deleting data!
            # os.rmdir(folder_path)  # Use this if the folder is empty


input_folder = input("Enter the input folder path: ")
delete_subfolders_with_fieldmap(input_folder)

for dir in os.listdir(input_folder):
    if dir.isdigit():
       nifti_folder = os.path.join(input_folder, dir, "pdata", "1", "nifti/")
       os.makedirs(nifti_folder, exist_ok=True)
       command = ["brkraw", "tonii", input_folder, "-s", dir, "-o", nifti_folder]
       subprocess.run(command)

bids_file = os.path.join(os.path.dirname(input_folder), os.path.basename(input_folder))
json_name = os.path.join(os.path.dirname(input_folder), os.path.basename(bids_file) + ".json")  # Modified path
csv_name = os.path.join(os.path.dirname(input_folder), os.path.basename(bids_file) + ".csv")    # Modified path
command_bids = ["brkraw", "bids_helper", input_folder, bids_file, "-j"]
subprocess.run(command_bids)
time.sleep(5)

bids_folder = input_folder + "_BIDS/"
command_convert = ["brkraw", "bids_convert", input_folder, csv_name, "-j", json_name, "-o", bids_folder]
subprocess.run(command_convert)
