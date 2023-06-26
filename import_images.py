from decouple import config
from pathlib import Path
import shutil
import pandas as pd

# Importing environment variables
data_src_folder = config("DATA_SRC_FOLDER")
raw_folder = config("RAW_FOLDER")
folder_ref = config("FOLDER_REF")

# Initialising DataFrame with references about folders to be imported
folder_ref_df = pd.read_csv(folder_ref)

# Function to extract list of filename stems
def get_tiff_file(row):
    p = Path(data_src_folder + row["data_subfolder"])
    stems_list = [f.stem for f in p.glob("*.tif")]
    return stems_list

# Function to extract timestep from filename stem
def get_tiff_time(row):
    timestep = int(row["tiff_stem"].split("T")[0][1:])
    return timestep

def copy_images(df, src_folder, dst_folder):
    tot_files = len(df)
    for idx, row in df.iterrows():
        src_tiff_fullpath = src_folder + row["data_subfolder"] + row["tiff_stem"] + ".tif"
        shutil.copy2(src_tiff_fullpath, dst_folder)
        progress = int(idx * 100. / tot_files)
        print(f'The copy process is {progress}% done...')

# Extract list of files in folder and explode for the list of filename stems
folder_ref_df["tiff_stem"] = folder_ref_df.apply(get_tiff_file, axis=1)
folder_ref_df = folder_ref_df.explode(["tiff_stem"])

# Extract integer timestep from filename stem
folder_ref_df["tiff_time"] = folder_ref_df.apply(get_tiff_time, axis=1)

# Get only entries that respect the condition
# (we select images that have enough cells but are not confluent)
folder_ref_df = folder_ref_df.query("tiff_time >= t_start and tiff_time < t_stop").reset_index(drop=True)

# Select 45 images, one every 30 images
folder_ref_df = folder_ref_df.iloc[::45].reset_index(drop=True)
print(f'{len(folder_ref_df)} images have been selected and will be imported in the destination folder.')

# Copy the images to the destination folder
print("Performing copy...")
copy_images(folder_ref_df, data_src_folder, raw_folder)
print("Copy successful!")
