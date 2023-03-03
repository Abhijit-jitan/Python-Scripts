## Takes Image-directory path & saves image in desired extension


## Required Libraries
#!pip3 install pillow-heif
#!pip install joblib


## Input: in_dir:Raw-Image Directory; out_dir:Modified-Image Directory; old_extension:old extension name ; new_extension:modified extension name 
## Output

import os 
from PIL import Image
from pillow_heif import register_heif_opener
from joblib import Parallel,delayed


register_heif_opener()

def change_extension(image,out_dir,new_extension): 
    image_name=image.split(".")[0]
    out_img_name=image_name+"."+new_extension       # generate new image name
    img=Image.open(os.path.join(in_dir,image))      # load image
    img.save(os.path.join(out_dir,out_img_name))    # save image


if __name__ == '__main__':
    in_dir=r"D:New_folder"        ## Raw-Image Directory Path
    out_dir=r"D:Random"             ## Modified-Image Directory Path 
    old_extension="jpg" ## heif,jpg,jpeg,png
    new_extension="jpeg" ## jpg,jpeg,png 

    Parallel(n_jobs=-1)(delayed(change_extension)(img,out_dir,new_extension) for img in os.listdir(in_dir))
    