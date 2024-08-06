import pandas as pd
import tarfile
import zipfile
from tqdm import tqdm
import re
import time
tqdm.pandas()

# OPTION THREE TRY TO CONVERT IT INTO A ZIP FILE AND THEN READ THROUGH IT
def convert_tar_to_zip(tar_path, zip_path):
    while True:
        try:
            with tarfile.open(tar_path, 'r') as tar:
                with zipfile.ZipFile(zip_path, 'w') as zipf:
                    for member in tqdm(tar.getmembers()):
                        file_obj = tar.extractfile(member)
                        if file_obj is not None:
                            zipf.writestr(member.name, file_obj.read())
            # If the conversion is successful, break out of the loop
            print("Conversion successful!")
            break
        except Exception as e:
            # Print the error and retry after a short delay
            print(f"Error: {e}")
            print("Retrying...")
            time.sleep(5)  # Wait for 5 seconds before retrying

# Define file paths
#/media/gregory178/Elements/Zip_Files_BI
#/media/gregory178/Elements/Zip_Files_BI
tar_file_path = '/media/gregory178/Thunderpacks/Dropbox/zz_EHR_Thunderpacks/BIDMC/BIDMC_Deidentified_Notes_March14th2024/bidmc_notes_2010.tar'
zip_file_path = '/media/gregory178/Elements/Zip_Files_BI/bidmc_notes_2010.zip'

# Convert tar to zip
convert_tar_to_zip(tar_file_path, zip_file_path)