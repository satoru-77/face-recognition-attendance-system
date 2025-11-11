from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox

class Train:

    def __init__(self,root):
        self.root=root
        self.root.geometry("925x500+300+200")
        self.root.title("Train Pannel")



        #title section
        title_lb1 = Label(root,text="Welcome to Training Space",font=("Microsoft YaHei UI Light",30,"bold"),bg="#339966",bd=0,fg="white")
        title_lb1.place(x=180,y=40,width=600,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\face_scan.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(root,command=self.train_classifier,image=self.std_img1,cursor="hand2")
        std_b1.place(x=400,y=150,width=180,height=180)

        std_b1_1 = Button(root,command=self.train_classifier,text="Click to Scan",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        std_b1_1.place(x=400,y=320,width=180,height=45)

    # ==================Create Function of Traing===================
    def train_classifier(self):
        data_dir=("data_img")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # conver in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids)
        
        #=================Train Classifier=============
        classifier= cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces,ids)
        classifier.write("classifier.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset Complated!",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()