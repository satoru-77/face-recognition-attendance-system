from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Jerry")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        

        # ============ Variables =================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_cnum=StringVar()
        self.var_email=StringVar()
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()
        self.var_cpwd=StringVar()
        self.var_check=IntVar()

        
        self.img_1 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\jerry.png')

        # Create a label with the image
        label_image = Label(root, image=self.img_1,bg='white')
        label_image.place(x=0, y=50)

        frame= Frame(self.root,bg="white")
        frame.place(x=450,y=0,width=905,height=500)
        

        get_str = Label(frame,text="Sign Up",font=("Roboto",30,"bold"),fg="#57a1f8",bg="white")
        get_str.place(x=0,y=10)

        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("Roboto",13,"bold"),fg="#808080",bg="White")
        fname.place(x=0,y=70)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_fname,font=("Roboto",13,"bold"))
        self.txtuser.place(x=0,y=100,width=200)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        lname.place(x=250,y=70)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_lname,font=("Roboto",13,"bold"))
        self.txtpwd.place(x=250,y=100,width=200)

        # ==================== section 2 -------- 2nd Columan===================

        #label1 
        cnum =lb1= Label(frame,text="Contact No:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        cnum.place(x=0,y=140)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_cnum,font=("Roboto",13,"bold"))
        self.txtuser.place(x=0,y=170,width=200)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        email.place(x=0,y=205)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("Roboto",13,"bold"))
        self.txtpwd.place(x=0,y=235,width=200)

        # ========================= Section 3 --- 1 Columan=================

        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        ssq.place(x=0,y=270)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_ssq,font=("Roboto",13,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=0,y=300,width=200)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        sa.place(x=250,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("Roboto",13,"bold"))
        self.txtpwd.place(x=250,y=300,width=200)

        # ========================= Section 4-----Column 2=============================

        #label1 
        pwd =lb1= Label(frame,text="Password:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        pwd.place(x=250,y=140)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pwd,font=("Roboto",13,"bold"))
        self.txtuser.place(x=250,y=170,width=200)


        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("Roboto",13,"bold"),fg="#808080",bg="white")
        cpwd.place(x=250,y=205)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpwd,font=("Roboto",13,"bold"))
        self.txtpwd.place(x=250,y=235,width=200)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("Roboto",13,"bold"),fg="#3399ff",bg="white")
        checkbtn.place(x=0,y=350,width=270)


        # Creating Button Register
        loginbtn=Button(frame,command=self.reg,text="Register",font=("Roboto",13,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#00cc66",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=0,y=400,width=260,height=30)

        # Creating Button Login
        loginbtn=Button(frame,text="Login instead?",font=("Roboto",13,"bold"),bd=0,relief=RIDGE,fg="red",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=270,y=400,width=200,height=35)




    def reg(self):
        if (self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_cnum.get()=="" or self.var_email.get()=="" or self.var_ssq.get()=="Select" or self.var_sa.get()=="" or self.var_pwd.get()=="" or self.var_cpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.var_pwd.get() != self.var_cpwd.get()):
            messagebox.showerror("Error","Please Enter Password & Confirm Password are Same!")
        elif(self.var_check.get()==0):
            messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
        else:
            # messagebox.showinfo("Successfully","Successfully Register!")
            try:
                conn = mysql.connector.connect(user='root', password='Mark42#1',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                query=("select * from regteach where email=%s")
                value=(self.var_email.get(),)
                mycursor.execute(query,value)
                row=mycursor.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist,please try another email")
                else:
                    mycursor.execute("insert into regteach values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_cnum.get(),
                    self.var_email.get(),
                    self.var_ssq.get(),
                    self.var_sa.get(),
                    self.var_pwd.get()
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)




if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()