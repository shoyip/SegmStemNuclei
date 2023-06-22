from decouple import config
import csv
from pathlib import Path

data_src_folder = config("DATA_SRC_FOLDER")
folder_ref = config("FOLDER_REF")

with open(folder_ref, newline="") as csvfile:
    next(csvfile)
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row in reader:
        data_src_subfolder = data_src_folder + row[0]
        p = Path(data_src_subfolder)
        start_t = int(row[1])
        stop_t = int(row[2])
        file_ids = [filename.stem for filename in p.glob("*.tif")]
        all_timesteps = [int(file_id.split("T")[0][1:]) for file_id in file_ids]
        good_timesteps = [timestep for timestep in all_timesteps if (timestep >= start_t) & (timestep < stop_t)]
        print(good_timesteps)
        break

# TODO: sample images and move them to data folder
