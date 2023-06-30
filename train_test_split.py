import shutil
from decouple import config
from pathlib import Path
import random

random.seed(42)

# Set folder paths
img_folder = config("IMG_FOLDER")
gt_folder = config("GT_FOLDER")

train_img_folder = config("TRAIN_IMG_FOLDER")
train_gt_folder = config("TRAIN_GT_FOLDER")
test_img_folder = config("TEST_IMG_FOLDER")
test_gt_folder = config("TEST_GT_FOLDER")

img_p = Path(img_folder)
gt_p = Path(gt_folder)

train_img_p = Path(train_img_folder)
train_gt_p = Path(train_gt_folder)
test_img_p = Path(test_img_folder)
test_gt_p = Path(test_gt_folder)

# Set parameters
train_size = 0.7

print(f"Train set size is {train_size}.")

# Define list of filenames
name_list = [image_file.name for image_file in img_p.glob("*.tif")]

# Set number of files
train_size_n = int(train_size * len(name_list))

print(f"There are {train_size_n} files in the train set.")

# Choose files
train_list = random.choices(name_list, k=train_size_n)

# Define test set
test_list = list(set(name_list) - set(train_list))

# Copy files to destination folders

print(f"Copying files in the train and test folders...")

for train_name in train_list:
    shutil.copy2(img_p / train_name, train_img_p / train_name)
    shutil.copy2(gt_p / train_name, train_gt_p / train_name)

for test_name in test_list:
    shutil.copy2(img_p / test_name, test_img_p / test_name)
    shutil.copy2(gt_p / test_name, test_gt_p / test_name)
