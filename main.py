from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1080x720+250+70")
        self.root.title("Face_Recogonition_Systm")
        self.root.configure(bg="#fff")

        #title section
        title_lb1 = Label(root,text="Attendance Management Using Face Recognition",font=("Roboto",30,"bold"),bg="white",fg="#57a1f8")
        title_lb1.place(x=50,y=20,width=1020,height=50)

        Frame(root, width=900, height=2, bg='black').place(x=100, y=70)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        std_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\student_icon.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(root,command=self.student_pannels,image=self.std_img1,cursor="hand2",bd=0)
        std_b1.place(x=150,y=100,width=180,height=180)

        std_b1_1 = Button(root,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        std_b1_1.place(x=150,y=280,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\face_scan.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(root,command=self.face_rec,image=self.det_img1,cursor="hand2",bd=0)
        det_b1.place(x=370,y=100,width=180,height=180)

        det_b1_1 = Button(root,command=self.face_rec,text="Face Detector",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        det_b1_1.place(x=370,y=280,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\attendance_check.jpg")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(root,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",bd=0)
        att_b1.place(x=570,y=100,width=180,height=180)

        att_b1_1 = Button(root,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        att_b1_1.place(x=570,y=280,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\hlp.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(root,command=self.helpSupport,image=self.hlp_img1,cursor="hand2",bd=0)
        hlp_b1.place(x=770,y=100,width=180,height=180)

        hlp_b1_1 = Button(root,command=self.helpSupport,text="Help Support",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        hlp_b1_1.place(x=770,y=280,width=180,height=45)

        # Top 4 buttons end.......
        # ---------------------------------------------------------------------------------------------------------------------------
        # Start below buttons.........
         # Train   button 5
        tra_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\face_train.jpg")
        tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        tra_b1 = Button(root,command=self.train_pannels,image=self.tra_img1,cursor="hand2",bd=0)
        tra_b1.place(x=150,y=360,width=180,height=180)

        tra_b1_1 = Button(root,command=self.train_pannels,text="Data Train",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        tra_b1_1.place(x=150,y=540,width=180,height=45)

        # Photo   button 6
        pho_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\gallery_icon.jpg")
        pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
        self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        pho_b1 = Button(root,command=self.open_img,image=self.pho_img1,cursor="hand2",bd=0)
        pho_b1.place(x=370,y=360,width=180,height=180)

        pho_b1_1 = Button(root,command=self.open_img,text="Photo Gallery",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        pho_b1_1.place(x=370,y=540,width=180,height=45)

        # Developers   button 7
        dev_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\developericon.jpg")
        dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
        self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        dev_b1 = Button(root,command=self.developr,image=self.dev_img1,cursor="hand2",bd=0)
        dev_b1.place(x=570,y=360,width=180,height=180)

        dev_b1_1 = Button(root,command=self.developr,text="Developers",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        dev_b1_1.place(x=570,y=540,width=180,height=45)

        # exit   button 8
        exi_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\logout.png")
        exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        exi_b1 = Button(root,command=self.Close,image=self.exi_img1,cursor="hand2",bd=0)
        exi_b1.place(x=770,y=360,width=180,height=180)

        exi_b1_1 = Button(root,command=self.Close,text="Exit",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        exi_b1_1.place(x=770,y=540,width=180,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("data_img")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def Close(self):
        root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
