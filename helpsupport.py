from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("925x500+300+200")
        self.root.title("Face_Recogonition_System")
        self.root.configure(bg="white")
        self.root.resizable(False, False)



        #title section
        title_lb1 = Label(root,text="Help Support",font=("MS Serif",30,"bold"),bg="white",fg="#000000")
        title_lb1.place(x=300,y=20,width=350,height=45)

        Frame(root, width=400, height=2, bg='black').place(x=290, y=70)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\www.png")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(root,command=self.website,image=self.std_img1,cursor="hand2",bg="white",bd=0)
        std_b1.place(x=40,y=160,width=180,height=180)

        std_b1_1 = Button(root,command=self.website,text="Our Website",cursor="hand2",font=("tahoma",15,"bold"),bg="#00cc66",bd=0,fg="white")
        std_b1_1.place(x=40,y=350,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\facebook.png")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(root,command=self.facebook,image=self.det_img1,cursor="hand2",bg="white",bd=0)
        det_b1.place(x=270,y=150,width=180,height=180)

        det_b1_1 = Button(root,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="#00cc66",bd=0,fg="white")
        det_b1_1.place(x=280,y=350,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\youtube.png")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(root,command=self.youtube,image=self.att_img1,cursor="hand2",bg="white",bd=0)
        att_b1.place(x=510,y=160,width=180,height=180)

        att_b1_1 = Button(root,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="#00cc66",bd=0,fg="white")
        att_b1_1.place(x=510,y=350,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(root,command=self.gmail,image=self.hlp_img1,cursor="hand2",bg="white",bd=0)
        hlp_b1.place(x=730,y=160,width=180,height=180)

        hlp_b1_1 = Button(root,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="#00cc66",bd=0,fg="white")
        hlp_b1_1.place(x=730,y=350,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://www.google.com/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()