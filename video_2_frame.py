### Video to images
import cv2,os

def FrameCapture(in_path,out_path,step_size=3):
    vidObj=cv2.VideoCapture(in_path)
    count,success=0,1
  
    while success:
        success,image=vidObj.read()
        image=cv2.resize(image,(imgW,imH))
        #image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
        #image=cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(out_path,str(count)+".jpg"),image) 
        count += 1
        
  
if __name__ == '__main__':
    imgW,imH=1200,1000
    in_path=r"dash.mp4"
    out_path=r"New_file"

    try:
        FrameCapture(in_path,out_path)
    except Exception:
        print("Video Has Ended !!!")