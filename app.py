import tkinter as tk #for the gui
from tkinter import simpledialog #for the questions 
import cv2 as cv
import os #file handeling
import PIL.Image, PIL.ImageTk #PIL stands for python image library, it' used for support for opening, manipulating, and saving many different image file formats.
import camera #importing thr class
#the central piece of the program. GUİ, controling functions (how to save images , how many are saved, etc.).


class App:

    def __init__(self,window= tk.Tk(),window_title = "Camera Classifier"): #constructor
        
        self.window = window
        self.window_title = window_title

        self.counters = [1,1] #an array that keeps up with 2 numbers both starting with 1 of the number of taken pics

        #self.model = ...

        self.auto_predict = False

        self.camera = camera.Camera()

        self.init.gui() #init stands for initializing

        self.delay = 15
        self.update()

        self.window.attributes('-topmost', True)#possition of the window
        self.window.mainloop()


    def init_gui(self):

        self.canvas = tk.Canvas(self.window, width=self.camera.width, height=self.camera.height) #getting the width and height of the camera output
        self.canvas.pack()

        self.btn_toggleauto = tk.Button(self.window, text="Auto Prediction", width=50, command=self.auto_predict_toggle) #button
        self.btn_toggleauto.pack(anchor=tk.CENTER, expand=True)#packing and align

        self.classname_one = simpledialog.askstring("Classname One", "Enter the name of the first class:", parent=self.window)
        self.classname_two = simpledialog.askstring("Classname Two", "Enter the name of the second class:", parent=self.window)

        self.btn_class_one = tk.Button(self.window, text=self.classname_one, width=50, command=lambda: self.save_for_class(1))#button
        self.btn_class_one.pack(anchor=tk.CENTER, expand=True)#packing and align

        self.btn_class_two = tk.Button(self.window, text=self.classname_two, width=50, command=lambda: self.save_for_class(2))#button
        self.btn_class_two.pack(anchor=tk.CENTER, expand=True)#packing and align

        self.btn_train = tk.Button(self.window, text="Train Model", width=50, command=lambda: self.model.train_model(self.counters))#button
        self.btn_train.pack(anchor=tk.CENTER, expand=True)#packing and align

        self.btn_predict = tk.Button(self.window, text="Predcit", width=50, command=self.predict)#button
        self.btn_predict.pack(anchor=tk.CENTER, expand=True)#packing and align

        self.btn_reset = tk.Button(self.window, text="Reset", width=50, command=self.reset)#button
        self.btn_reset.pack(anchor=tk.CENTER, expand=True)#packing and align

        self.class_label = tk.Label(self.window, text="CLASS")
        self.class_label.config(font=("Arial", 20))
        self.class_label.pack(anchor=tk.CENTER, expand=True)#packing and align



    def auto_predicct_toggle(self):
        self.auto_predict = not self.auto_predict


    def save_for_class(self,class_num):
        ret, frame = self.camera.get_frame()
        if not os.path.exists('1'):
            os.mkdir('1')
        if not os.mkdir('2'):
            os.mkdir('2')    

        cv.imread(f'{class_num}/frame{self.counters[class_num -1]}.jpg', cv.cvtColor(frame, cv.COLOR_RBG2GRAY)) 
        #we're going to save the images in grey he're is why: we only need the structure of the object. The colour doens't matter that much. Colour means more data, that means more training time etc.
        img = PIL.Image.open(f'{class_num}/frame{self.counters[class_num -1]}.jpg')
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)#saving the pic in a 150*150 pixel state.
        img.save(f'{class_num}/frame{self.counters[class_num -1]}.jpg')

        self.counters[class_num -1] += 1


    def reset(self): 
        for directory in ['1', '2']:
            for file in os.listdir(directory): #first we're searching for each directory in the list
                file_path = os.path.join(directory, file) #we linked the file path by combining the directory and file
                if os.path.isfile(file_path):#if exists
                    os.unlink(file_path)#then delete


        self.counters[1,1]
        #self.model = model.Model()
        self.class_label.config(text = 'CLASS') #resetting thr given class names by us to the standart "class" name


    def update(self):
        if self.auto_predict:
            #self.predict()
            pass

        ret,frame = self.camera.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame)) #we're getting the image and setting it to a tk image to use it for our gui 
            self.canvas.create_image(00,image=self.photo, anchor= tk.NW)

            self.window.after(self.delay,self.update)
            #we're calling the function recursively, and bu revering and not calling teh function with () at the end of the function, the function will be called after the delay



