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
gt_p = Path(gt_folder)

# Loop through images in the interim folders (images and ground truths)
for cutout_image in c_p.glob("*.tif"):
    img = cv2.imread(cutout_image.as_posix(), cv2.IMREAD_GRAYSCALE)
    img_id = str(cutout_image.stem)
    fsgt_path = fsgt_p / (img_id+".tif")
    fsgt = cv2.imread(fsgt_path.as_posix(), cv2.IMREAD_GRAYSCALE)
    img_copy = img.copy()
    fsgt_copy = fsgt.copy()

    print(f"Subdividing in tiles image {img_id}...")

    n_tiles = [dim//512 for dim in img.shape]
    pad = [(dim%512)//2 for dim in img.shape]

    print(f"Image will have {n_tiles[0]} x and {n_tiles[1]} y tiles")

    for tile_y in range(n_tiles[1]):
        for tile_x in range(n_tiles[0]):
            # print(f"Cutting tile [{tile_x}, {tile_y}]")
            start_x, start_y = pad[0]+512*tile_x, pad[1]+512*tile_y
            end_x, end_y = pad[0]+512*(tile_x + 1), pad[1]+512*(tile_y + 1)
            tile_img = img_copy[start_x:end_x, start_y:end_y]
            tile_gt = fsgt_copy[start_x:end_x, start_y:end_y]
            cv2.imwrite(str(img_p / (img_id+"_x"+str(tile_x)+"_y"+str(tile_y)+".tif")), tile_img)
            cv2.imwrite(str(gt_p / (img_id+"_x"+str(tile_x)+"_y"+str(tile_y)+".tif")), tile_gt)

    # FOR DEBUG PURPOSES
    # img = cv2.imread(cutout_image.as_posix())
    # cv2.imshow("original", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
