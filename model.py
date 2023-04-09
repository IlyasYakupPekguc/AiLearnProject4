from sklearn.svm import LinearSVC #the neural network just like tensorflow NOTE: it's not the best neural network, but it's enough for our small project
import numpy as np
import cv2 as cv
import PIL

class Model:

    def __init__(self): #constructor
        self.model = LinearSVC()

    def train_model(self, counters): #we need the images to be in np arrays so they can be processed, we also want to change the data to labeled data so we can train it
        img_list = np.array([])
        class_list = np.array([]) #empty np lists

        for i in range(1, counters[0]):
            img = cv.imread(f'1/femae{i}.jpg')[:,:,0]
            img = img.reshape(16800) #150x112 resulotion ,if the resulutoin is different multiply that 2 numbers and change the reshape value
            img_list = np.append(img_list,[img])
            class_list = np.append(class_list, 1)


        for i in range(1, counters[1]):
            img = cv.imread(f'2/femae{i}.jpg')[:,:,0]
            img = img.reshape(16800) #150x112 resulotion ,if the resulutoin is different multiply that 2 numbers and change the reshape value
            img_list = np.append(img_list,[img])
            class_list = np.append(class_list, 2)

        img_list = img_list.reshape(counters[0]-1 + counters[1],1 , 16800)
        self.model.fit(img_list,class_list)
        print("Model succesfully trained")
        

    def predict(self,frame):
        frame = frame[1]
        cv.imwrite('frame.jpg', cv.cvtColor(cv.COLOR_RGB2GRAY))
        img = PIL.Image.open('frame.jpg')
        img.thumbnail((150,150), PIL.Image.ANTIALIAS)#saving the pic in a 150*150 pixel state.
        img.save('frame.jpg')

        img = cv.imread('frame.jpg')[:,:,0]
        img = img.reshape(16800)
        prediction = self.model.predict([img])

        return prediction[0]