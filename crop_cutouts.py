from decouple import config
from pathlib import Path
import cv2

# Setting the paths for interim folders
cutout_folder = config("CUTOUT_FOLDER")
fullsizegt_folder = config("FULLSIZEGT_FOLDER")

c_p = Path(cutout_folder)
fsgt_p = Path(fullsizegt_folder)

# Setting the paths for preprocessed folders
img_folder = config("IMG_FOLDER")
gt_folder = config("GT_FOLDER")

img_p = Path(img_folder)
gt_folder = Path(gt_folder)

# Loop through images in the interim folders (images and ground truths)
for cutout_image in c_p.glob("*.tif"):
    img = cv2.imread(cutout_image.as_posix(), cv2.IMREAD_GRAYSCALE)
    n_tiles = [dim//512 for dim in img.shape]
    for tile_y in n_tiles[1]:
        for tile_x in n_tiles[0]:

    # FOR DEBUG PURPOSES
    # img = cv2.imread(cutout_image.as_posix())
    # cv2.imshow("original", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    break
