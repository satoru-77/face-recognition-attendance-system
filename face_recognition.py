from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
class Face_Recognition:

    def __init__(self,root):
        self.root=root
        self.root.geometry("925x500+300+200")
        self.root.title("Train Pannel")
        self.root.configure(bg="white")
        self.root.resizable(False, False)


        #title section
        title_lb1 = Label(root,text="Welcome to face recognition",font=("Roboto",30,"bold"),bg="white",fg="#00cc66")
        title_lb1.place(x=100,y=15,width=700,height=50)

        Frame(root, width=700, height=2, bg='black').place(x=120, y=70)

        
        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # Training button 1
        std_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\face_train.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(root, command=self.face_recog, image=self.std_img1, cursor="hand2", bd=0)
        std_b1.place(x=400,y=160,width=180,height=180)

        std_b1_1 = Button(root,command=self.face_recog,text="Detect Face",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#00cc66",bd=0,fg="white")
        std_b1_1.place(x=390,y=340,width=180,height=45)
    #=====================Attendance===================
            # Initialize a set to store unique IDs for faces marked on the current day
        self.marked_faces_today = set()

    def mark_attendance(self, i, r, n):
        # Check if the date has changed since the last marking
        today = datetime.now().strftime("%d/%m/%Y")
        if today != getattr(self, "current_date", None):
            self.marked_faces_today = set()
            self.current_date = today

        with open("attendance.csv", "a+", newline="\n") as f:
            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")

            if i != "Unknown" and i not in self.marked_faces_today:
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
                
                # Add the face ID to the set to avoid marking it again on the same day
                self.marked_faces_today.add(i)




    #================face recognition==================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            featuers=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in featuers:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='Mark42#1',host='localhost',database='face_recognition',port=3306)
                cursor = conn.cursor()

                cursor.execute("select Student_ID from student where Student_ID=" + str(id))
                result = cursor.fetchone()
                if result is not None:
                    i = str(result[0])
                else:
                    i = "Unknown"

                cursor.execute("select Name from student where Student_ID=" + str(id))
                result = cursor.fetchone()
                if result is not None:
                    n = str(result[0])
                else:
                    n = "Unknown"

                cursor.execute("select Roll_No from student where Student_ID=" + str(id))
                result = cursor.fetchone()
                if result is not None:
                    r = str(result[0])
                else:
                    r = "Unknown"





                if confidence > 77:
                    cv2.putText(img,f"Student_ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll-No:{r}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    self.mark_attendance(i,r,n)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,0),3)    

                coord=[x,y,w,y]
            
            return coord    


        #==========
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Face Detector",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()