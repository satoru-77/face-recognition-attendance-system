from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.title("Jerry")
root.geometry("925x500+300+200")
root.configure(bg="white")
root.resizable(False, False)

var_fname = StringVar()
var_lname = StringVar()
var_cnum = StringVar()
var_email = StringVar()
var_pwd = StringVar()
var_cpwd = StringVar()

# Load image
img_1 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\jerry.png')

# Create a label with the image
label_image = Label(root, image=img_1, bg='white')
label_image.place(x=0, y=50)

frame = Frame(root, bg="white")
frame.place(x=450, y=0, width=905, height=500)

get_str = Label(frame, text="Sign Up", font=("Roboto", 30, "bold"), fg="#57a1f8", bg="white")
get_str.place(x=0, y=10)
######################################################
fname = Label(frame, text="First Name:", font=("Roboto", 13, "bold"), fg="#808080", bg="White")
fname.place(x=0, y=70)
txtuser = ttk.Entry(frame, textvariable=var_fname, font=("Roboto", 13, "bold"))
txtuser.place(x=0, y=100, width=200)

lname = Label(frame, text="Last Name:", font=("Roboto", 13, "bold"), fg="#808080", bg="white")
lname.place(x=250, y=70)
txtpwd = ttk.Entry(frame, textvariable=var_lname, font=("Roboto", 13, "bold"))
txtpwd.place(x=250, y=100, width=200)

cnum = Label(frame, text="Contact No:", font=("Roboto", 13, "bold"), fg="#808080", bg="white")
cnum.place(x=0, y=140)
txtuser = ttk.Entry(frame, textvariable=var_cnum, font=("Roboto", 13, "bold"))
txtuser.place(x=0, y=170, width=200)

email = Label(frame, text="Email:", font=("Roboto", 13, "bold"), fg="#808080", bg="white")
email.place(x=250, y=140)
txtpwd = ttk.Entry(frame, textvariable=var_email, font=("Roboto", 13, "bold"))
txtpwd.place(x=250, y=170, width=200)

pwd = Label(frame, text="Password:", font=("Roboto", 13, "bold"), fg="#808080", bg="white")
pwd.place(x=0, y=205)
txtuser = ttk.Entry(frame, textvariable=var_pwd, font=("Roboto", 13, "bold"), show="*")
txtuser.place(x=0, y=235, width=200)

cpwd = Label(frame, text="Confirm Password:", font=("Roboto", 13, "bold"), fg="#808080", bg="white")
cpwd.place(x=250, y=205)
txtpwd = ttk.Entry(frame, textvariable=var_cpwd, font=("Roboto", 13, "bold"), show="*")
txtpwd.place(x=250, y=235, width=200)
################################################

loginbtn = Button(frame, text="Register", font=("Roboto", 13, "bold"), bd=0, relief=RIDGE,
                  fg="#fff", bg="#00cc66", activeforeground="white", activebackground="#007ACC")
loginbtn.place(x=0, y=400, width=260, height=30)

loginbtn = Button(frame, text="Login instead?", font=("Roboto", 13, "bold"), bd=0, relief=RIDGE, fg="red",
                  bg="white", activeforeground="white", activebackground="#007ACC")
loginbtn.place(x=270, y=400, width=200, height=35)
############################################################
root.mainloop()
