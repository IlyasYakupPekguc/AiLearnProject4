import cv2 as cv


class Camera:

    def __init__(self):
        self.camera = cv.VideoCapture(0) #the 0 stand for the webcame u use (if you have 1 webcam the standart is 0)
        if not self.camera.isOpened():
            raise ValueError("unable to open the camera") #as far as i understand this whole block is a if else like block and we're coding the catch statement -ish
        

    def __del__(self):
        if self.camera.isOpened():
            self.camera.release() #if camera is not used then close the camera


    def get_frame(self):
        if self.camera.isOpened():
            ret, frame = self.camer.read()

            if ret: #if there's a return value 
                return(ret,cv.cvtColor(frame,cv.COLOR_BGR2RGB))