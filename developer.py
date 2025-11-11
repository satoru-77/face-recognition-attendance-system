from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x650+200+50")
        self.root.title("Developers Panel")
        self.root.configure(bg="white")
        self.root.resizable(False, False)

        #title section
        title_lb1 = Label(root,text="Meet Our Team",font=("verdana",25,"bold"),bg="white",fg="green")
        title_lb1.place(x=450,y=0,width=305,height=45)

        Frame(self.root, width=380, height=2, bg='black').place(x=420, y=50)
        
##################################

        frame1 = Frame(root, width = 200, height=450, bg = 'white')
        frame1.place(x=20, y = 100)

        self.img_1 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\Indrajit.png')
        label_image1 = Label(frame1, image=self.img_1,bg='white')
        label_image1.place(x=0, y=0)

        indrajit = Label(frame1, text="IndrAjit Das", font=("verdana", 16, "bold"), bg='#00cc66', foreground='white')
        indrajit.place(x=0, y=215)


        # Add multiline text below the image, align left
        text_content = "\u2022 Developer\n\u2022 Designer"
        text_below_image = Label(frame1, text=text_content, font=("verdana", 12, "bold"), bg='white', anchor='w', justify='left')
        text_below_image.place(x=0, y=250)


        
######################################

        frame2 = Frame(root, width = 200, height=450, bg = 'white')
        frame2.place(x=260, y = 100)

        self.img_2 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\Indrajit.png')
        label_image2 = Label(frame2, image=self.img_2,bg='white')
        label_image2.place(x=0, y=0)

        Jiya = Label(frame2, text="Jiya Gupta", font=("verdana", 16, "bold"), bg='#00cc66', foreground='white')
        Jiya.place(x=0, y=215)


        # Add multiline text below the image, align left
        text_content2 = "\u2022 Developer\n\u2022 Designer"
        text_below_image2 = Label(frame2, text=text_content2, font=("verdana", 12, "bold"), bg='white', anchor='w', justify='left')
        text_below_image2.place(x=0, y=250)

###################################

        frame3 = Frame(root, width = 200, height=450, bg = 'white')
        frame3.place(x=500, y = 100)

        self.img_3 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\Indrajit.png')
        label_image3 = Label(frame3, image=self.img_3,bg='white')
        label_image3.place(x=0, y=0)

        Narbu = Label(frame3, text="Narbu Sherpa", font=("verdana", 16, "bold"), bg='#00cc66', foreground='white')
        Narbu.place(x=0, y=215)


        # Add multiline text below the image, align left
        text_content3 = "\u2022 Developer\n\u2022 Designer"
        text_below_image3 = Label(frame3, text=text_content3, font=("verdana", 12, "bold"), bg='white', anchor='w', justify='left')
        text_below_image3.place(x=0, y=250)

##############################

        frame4 = Frame(root, width = 210, height=450, bg = 'white')
        frame4.place(x=750, y = 100)

        self.img_4 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\Indrajit.png')
        label_image4 = Label(frame4, image=self.img_4,bg='white')
        label_image4.place(x=0, y=0)

        Hasiba = Label(frame4, text="Hasiba Khatoon", font=("verdana", 16, "bold"), bg='#00cc66', foreground='white')
        Hasiba.place(x=0, y=215)


        # Add multiline text below the image, align left
        text_content4 = "\u2022 Developer\n\u2022 Designer"
        text_below_image4 = Label(frame4, text=text_content4, font=("verdana", 12, "bold"), bg='white', anchor='w', justify='left')
        text_below_image4.place(x=0, y=250)

#######################

        frame5 = Frame(root, width = 200, height=450, bg = 'white')
        frame5.place(x=980, y = 100)

        self.img_5 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\Indrajit.png')
        label_image5 = Label(frame5, image=self.img_5,bg='white')
        label_image5.place(x=0, y=0)

        Hardisk = Label(frame5, text="Soumyadep Ghosh", font=("verdana", 14, "bold"), bg='#00cc66', foreground='white',justify='left')
        Hardisk.place(x=0, y=215)


        # Add multiline text below the image, align left
        text_content5 = "\u2022 Developer\n\u2022 Designer"
        text_below_image5 = Label(frame5, text=text_content5, font=("verdana", 12, "bold"), bg='white', anchor='w', justify='left')
        text_below_image5.place(x=0, y=250)

#############################



if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()