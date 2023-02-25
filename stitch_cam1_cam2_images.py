import cv2,os,datetime
import numpy as np
from joblib import Parallel,delayed
    
# inputp: imgW: output image width; imH= output image height; cam1_img_directory: 1st image directory; cam2_img_directory: 2nd image directory; out_img_dirrectory: Output image directory
# process: takes images> do preprocess> stitches them to one> write image 
# output:


def stack_2_cam(index):
    cam1_img=cv2.imread(os.path.join(cam1_img_directory,cam1_img_list[index]))
    cam1_img=cv2.resize(cam1_img,(imgW,imH))
    
    cam2_img=cv2.imread(os.path.join(cam1_img_directory,cam2_img_list[index]))
    cam2_img=cv2.resize(cam2_img,(imgW,imH))

    stack=cv2.hconcat([cam1_img,cam2_img])
    cv2.imwrite(os.path.join(out_img_dirrectory,str(index)+".jpg"),stack)



 
if __name__ == '__main__':
    tic=datetime.datetime.now()

    imgW,imH=640,800
    cam1_img_directory=r"D:\Left_cam_frame"
    cam2_img_directory=r"D:\Right_cam_frame"
    out_img_dirrectory=r"D:\merged_frame"

    cam1_img_list=os.listdir(cam1_img_directory)
    cam2_img_list=os.listdir(cam2_img_directory)    
    

    
    Parallel(n_jobs=-1)(delayed(stack_2_cam)(index) for index in range(len(cam1_img_list)))

    toc=datetime.datetime.now()
    print("Total time taken:",toc-tic) 




