import tkinter as tk #for the gui
from tkinter import simpledialog #for the questions 
import cv2 as cv
import os #file handeling
import PIL.Image, PIL.ImageTk
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
        #self.update()

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

