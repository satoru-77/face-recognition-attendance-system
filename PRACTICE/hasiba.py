from tkinter import *
from tkinter import ttk
from tkinter import messagebox



root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="white")
# root.resizable(False, False)

# Load the image and store it as an attribute
img_1 = PhotoImage(file=r'C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\signIN.png')

# Create a label with the image
label_image = Label(root, image=img_1, bg='white')
label_image.place(x=60, y=80)

frame1 = Frame(root, bg="white")
frame1.place(x=450, y=30, width=450, height=450)

get_str = Label(frame1, text="Welcome!", font=("Roboto", 30, "bold"), fg="#57a1f8", bg="white")
get_str.place(x=100, y=10)

# Label and Entry for Email
label_email = Label(frame1, text="E-mail address:", font=("Roboto", 15, "bold"), fg="#808080", bg="white")
label_email.place(x=99, y=95)
entry_email = ttk.Entry(frame1, font=('Roboto', 17))
entry_email.place(x=100, y=130, width=270)

# Label and Entry for Password
label_password = Label(frame1, text="Password:", font=("Roboto", 15, "bold"), fg="#808080", bg="white")
label_password.place(x=99, y=185)
entry_password = ttk.Entry(frame1, font=("times new roman", 15, "bold"), show="*")
entry_password.place(x=100, y=220, width=270, height=40)

# Button for Login
login_btn = Button(frame1,  text="Login", font=("Roboto", 15, "bold"), bd=0, relief=RIDGE, fg="#002B53",
                   bg="#00cc66", activeforeground="white", activebackground="#007ACC")
login_btn.place(x=100, y=300, width=200, height=35)

# Button for Registration
register_btn = Button(frame1,  text="Register", font=("Roboto", 12, "bold"), bd=0, relief=RIDGE,
                      fg="#57a1f8", bg="white", activeforeground="orange", activebackground="#002B53")
register_btn.place(x=310, y=370, width=80, height=30)

# Button for Forgot Password
forgot_pwd_btn = Button(frame1,  text="Forgot password?", font=("Roboto", 12, "bold"), bd=0,
                        relief=RIDGE, fg="#808080", bg="white", activeforeground="orange", activebackground="#002B53")
forgot_pwd_btn.place(x=95, y=370, width=180, height=30)

root.mainloop()
