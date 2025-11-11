from tkinter import*
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    if username  == 'admin' and password == '1234':
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='White')

        Label(screen, text = 'WELCOME', bg = '#fff', font = ('Calibri(Body)',50, 'bold')).pack(expand=True)

        screen.mainloop()

    elif username != 'admin' and password != '1234':
        messagebox.showerror("Invalid", "invalid username and password")
    elif password != '1234':
        messagebox.showerror("Invalid","invalid password")
    elif username != 'admin':
        messagebox.showerror("Invalid","invalid username or password")


frame = Frame(root, width = 350, height=350, bg = 'white')
frame.place(x=480, y = 70)

img = PhotoImage(file='D:/CODE/PythonProjects/ModernGUI/images/login.png')
Label(root, image = img, bg='white').place(x=50,y=50)

heading = Label(frame, text ='Sign in', fg = '#57a1f8', bg = 'White', font = ('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=2)

#######################################
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name = user.get()
    if name =='':
        user.insert(0, 'Username')

user = Entry(frame, width = 25, fg = 'black', border = 0, bg ='White',font = ('Microsoft YaHei UI Light',17))
user.place(x=30, y=80)
user.insert(0, 'Username/email')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=117)
#######################################
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name = code.get()
    if name =='':
        code.insert(0, 'Password')

code = Entry(frame, width = 25, fg = 'black', border = 0, bg ='White',font = ('Microsoft YaHei UI Light',17))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=187)
######################################

Button(frame, width=39, pady=7, text = 'Sign in', bg = '#57a1f8', fg='White', border=0,command=signin).place(x=35, y = 205)
label = Label(frame, text = "Don't have an account?", fg ='black', bg = 'White', font = ('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up = Button(frame, width = 6, text = 'Sign Up', border = 0, bg ='White', cursor = 'hand2',fg='#57a1f8')
sign_up.place(x=215, y = 270)



root.mainloop()