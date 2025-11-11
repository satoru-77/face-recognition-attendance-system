from tkinter import* 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import mysql.connector
# --------------------------
from train import Train
from student import Student
from train import Train
import face_recognition
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from helpsupport import Helpsupport
import os


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()


        # Load the image and store it as an attribute
        self.img_1 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\signIN.png')

        # Create a label with the image
        label_image = Label(root, image=self.img_1,bg='white')
        label_image.place(x=60, y=80)


        frame1 = Frame(self.root, bg="white")
        frame1.place(x=450, y=30, width=450, height=450)
        

        get_str = Label(frame1,text="Welcome!",font=("Roboto",30,"bold"),fg="#57a1f8",bg="white")
        get_str.place(x=100,y=10)

        #label1 
        username =lb1= Label(frame1,text="E-mail address:",font=("Roboto",15,"bold"),fg="#808080",bg="white")
        username.place(x=99,y=95)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font = ('Roboto',17))
        self.txtuser.place(x=100,y=130,width=270)

        # Frame(frame1, width=295, height=2, bg='black').place(x=95, y=185)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("Roboto",15,"bold"),fg="#808080",bg="white")
        pwd.place(x=99,y=185)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=100,y=220,width=270,height=40)

        # Frame(frame1, width=295, height=2, bg='black').place(x=95, y=290)


        # Creating Button Login}"[;PLOKIJUHYG TFRDESWQA]"
        loginbtn=Button(frame1,command=self.login,text="Login",font=("Roboto",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="#00cc66",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=100,y=300,width=200,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("Roboto",12,"bold"),bd=0,relief=RIDGE,fg="#57a1f8",bg="white",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=310,y=370,width=80,height=30)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forgot password?",font=("Roboto",12,"bold"),bd=0,relief=RIDGE,fg="#808080",bg="white",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=95,y=370,width=180,height=30)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            conn = mysql.connector.connect(user='root', password='Mark42#1',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            mycursor.execute("select * from regteach where email=%s and pwd=%s",(
                self.txtuser.get(),
                self.txtpwd.get()
            ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password!")
            else:
                open_min=messagebox.askyesno("YesNo","Access only Admin")
                if open_min>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_min:
                        return
            conn.commit()
            conn.close()
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = mysql.connector.connect(user='root', password='Mark42#1',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s and ss_que=%s and s_ans=%s")
            value=(self.txtuser.get(),self.var_ssq.get(),self.var_sa.get())
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Correct Answer!",parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(user='root', password='Mark42#1',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("885x360+320+280")
                self.root2.configure(bg="white")
                self.root2.resizable(False, False)
                l=Label(self.root2,text="Forgot Password?",font=("Roboto",25,"bold"),fg="#57a1f8",bg="white")
                l.place(x=0,y=5,width=400)


                self.img_1 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\forgot.png')

                # Create a label with the image
                label_image_1 = Label(self.root2, image=self.img_1,bg='white')
                label_image_1.place(x=450, y=5)


                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("Roboto",15,"bold"),fg="#002B53",bg="white")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("Roboto",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("Roboto",15,"bold"),fg="#002B53",bg="white")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("Roboto",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("Roboto",15,"bold"),fg="#002B53",bg="white")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("Roboto",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("Roboto",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#4d4dff",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================

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

        pho_b1_1 = Button(root,command=self.open_img,text="Face Data",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
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
    
    


        # # Create a white image
        # white_image = Image.new("RGB", (1366, 768), "white")

        # # Convert the white image to a PhotoImage
        # self.photo_white = ImageTk.PhotoImage(white_image)

        # # Set white image as label
        # bg_img = Label(self.root, image=self.photo_white)
        # bg_img.place(x=0, y=40, width=1366, height=800)

        # #title section
        # title_lb1 = Label(bg_img,text="Attendance Management Using Face Recognition",font=("Microsoft YaHei UI Light",30,"bold"),bg="#57a1f8",fg="white")
        # title_lb1.place(x=50,y=2,width=1000,height=50)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # # student button 1
        # std_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\student_icon.jpg")
        # std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        # self.std_img1=ImageTk.PhotoImage(std_img_btn)

        # std_b1 = Button(bg_img,command=self.student_pannels,image=self.std_img1,cursor="hand2",bd=0)
        # std_b1.place(x=150,y=100,width=180,height=180)

        # std_b1_1 = Button(bg_img,command=self.student_pannels,text="Student Pannel",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # std_b1_1.place(x=150,y=280,width=180,height=45)

        # # Detect Face  button 2
        # det_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\face_scan.jpg")
        # det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        # self.det_img1=ImageTk.PhotoImage(det_img_btn)

        # det_b1 = Button(bg_img,command=self.face_rec,image=self.det_img1,cursor="hand2",bd=0)
        # det_b1.place(x=370,y=100,width=180,height=180)

        # det_b1_1 = Button(bg_img,command=self.face_rec,text="Face Detector",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # det_b1_1.place(x=370,y=280,width=180,height=45)

        #  # Attendance System  button 3
        # att_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\attendance_check.jpg")
        # att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        # self.att_img1=ImageTk.PhotoImage(att_img_btn)

        # att_b1 = Button(bg_img,command=self.attendance_pannel,image=self.att_img1,cursor="hand2",bd=0)
        # att_b1.place(x=570,y=100,width=180,height=180)

        # att_b1_1 = Button(bg_img,command=self.attendance_pannel,text="Attendance",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # att_b1_1.place(x=570,y=280,width=180,height=45)

        #  # Help  Support  button 4
        # hlp_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\hlp.jpg")
        # hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        # self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        # hlp_b1 = Button(bg_img,command=self.help_pannel,image=self.hlp_img1,cursor="hand2",bd=0)
        # hlp_b1.place(x=770,y=100,width=180,height=180)

        # hlp_b1_1 = Button(bg_img,command=self.help_pannel,text="Help Support",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # hlp_b1_1.place(x=770,y=280,width=180,height=45)

        # # Top 4 buttons end.......
        # # ---------------------------------------------------------------------------------------------------------------------------
        # # Start below buttons.........
        #  # Train   button 5
        # tra_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\face_train.jpg")
        # tra_img_btn=tra_img_btn.resize((180,180),Image.LANCZOS)
        # self.tra_img1=ImageTk.PhotoImage(tra_img_btn)

        # tra_b1 = Button(bg_img,command=self.train_pannels,image=self.tra_img1,cursor="hand2",bd=0)
        # tra_b1.place(x=150,y=360,width=180,height=180)

        # tra_b1_1 = Button(bg_img,command=self.train_pannels,text="Train Face Data",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # tra_b1_1.place(x=150,y=540,width=180,height=45)

        # # Photo   button 6
        # pho_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\gallery_icon.jpg")
        # pho_img_btn=pho_img_btn.resize((180,180),Image.LANCZOS)
        # self.pho_img1=ImageTk.PhotoImage(pho_img_btn)

        # pho_b1 = Button(bg_img,command=self.open_img,image=self.pho_img1,cursor="hand2",bd=0)
        # pho_b1.place(x=370,y=360,width=180,height=180)

        # pho_b1_1 = Button(bg_img,command=self.open_img,text="QR-Codes",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # pho_b1_1.place(x=370,y=540,width=180,height=45)

        # # Developers   button 7
        # dev_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\developericon.jpg")
        # dev_img_btn=dev_img_btn.resize((180,180),Image.LANCZOS)
        # self.dev_img1=ImageTk.PhotoImage(dev_img_btn)

        # dev_b1 = Button(bg_img,command=self.developr,image=self.dev_img1,cursor="hand2",bd=0)
        # dev_b1.place(x=570,y=360,width=180,height=180)

        # dev_b1_1 = Button(bg_img,command=self.developr,text="Developers",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # dev_b1_1.place(x=570,y=540,width=180,height=45)

        # # exit   button 8
        # exi_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\logout.png")
        # exi_img_btn=exi_img_btn.resize((180,180),Image.LANCZOS)
        # self.exi_img1=ImageTk.PhotoImage(exi_img_btn)

        # exi_b1 = Button(bg_img,image=self.exi_img1,cursor="hand2",bd=0)
        # exi_b1.place(x=770,y=360,width=180,height=180)

        # exi_b1_1 = Button(bg_img,text="Exit",cursor="hand2",font=("Microsoft YaHei UI Light",15,"bold"),bg="#339966",bd=0,fg="white")
        # exi_b1_1.place(x=770,y=540,width=180,height=45)

    

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
    
    def help_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def open_img(self):
        os.startfile("data_img")
    
  




if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()