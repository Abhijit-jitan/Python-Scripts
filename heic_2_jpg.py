
#!pip3 install pillow-heif
import os 
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def HEIC_to_jpg(img_in,img_out):
    img=Image.open(img_in)
    img.save(img_out)


if __name__ == '__main__':
    in_path=r"D:\data"
    output_format=".png" #".jpg"
    out_path=r"D:\data_converted"


    for img in os.listdir(in_path):
        img_name=img.split(".")[0]

        HEIC_to_jpg(os.path.join(in_path,img),os.path.join(out_path,img_name+output_format))