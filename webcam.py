import cv2
import dropbox
import time
import random   

startTime=time.time()

def captureImage():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName="image"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time()
        result=False
        
    return imageName
    print("Image captured !!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadImage(imageName):
    accessToken='sl.AtsYG62mExV7PMbv33WXhWMpfgQzfNFdN6lHfxnkxMhXkp9VwjRzU0lu3Ejwufp3X9LRkYsi0Wo-K8hKPW1vQfE1AhuQohZmrPnSANbkGvyXIsmHXdGigqm_pRIaWK5dkGSyfYTVOkE'
    file=imageName
    file_From=file
    file_To="/"+imageName
    dbx=dropbox.Dropbox(accessToken)
    with open(file_From,'rb')as f:
        dbx.files_upload(f.read(),file_To,mode=dropbox.files.WriteMode.overwrite)
        print("Image uploaded !!")

def main():
    while (True):
        if((time.time()-startTime)>=5):
            name=captureImage()
            uploadImage(name)

main()