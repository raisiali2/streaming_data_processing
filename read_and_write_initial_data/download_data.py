# import pandas as pd 
# import os
import subprocess

def download_file(url, destinaiton_folder):

    try:
        #construc the wget command to download the file
        command = [ url, "-P", destinaiton_folder]

        #execute the command
        subprocess.run(command, check=True)
        print(f"file downloaded successfully to {destinaiton_folder}")
    except subprocess.CalledProcessError:
        print("an error occured while downloading the file.")

url = "https://github.com/dogukannulu/datasets/raw/master/sensors_instrumented_in_an_office_building_dataset.zip"
destinaiton_folder = '/home/ali/train/datasets'
download_file(url, destinaiton_folder)