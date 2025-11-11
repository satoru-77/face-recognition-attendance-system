from tkinter import *
from tkinter import messagebox

main_window = Tk()
main_window.title('Developers Panel')
main_window.geometry('925x500+300+200')
main_window.configure(bg="#fff")
main_window.resizable(False, False)

frame_1 = Frame(main_window, width=350, height=50, bg='white')
frame_1.place(x=290, y=50)

heading = Label(frame_1, text='Developers', fg='#57a1f8', bg='white', font=('Arial', 23, 'bold'))
heading.place(x=90, y=2)

############################
frame_1a = Frame(main_window, width=150, height=250, bg='White')
frame_1a.place(x=50, y=100)

img1 = PhotoImage(file='D:/CODE/PythonProjects/ModernGUI/images/IndrAjitDas.png')
image_label1 = Label(frame_1a, image=img1, bg='white')
image_label1.photo = img1  # Store reference to the image
image_label1.place(x=0, y=0)


Button(frame_1a, width=21, pady=7, text = 'Hasiba Hasde zara', bg = '#57a1f8', fg='White', border=0).place(x=0, y = 155)
####################################
frame_2 = Frame(main_window, width=150, height=250, bg='white')
frame_2.place(x=220, y=100)

img2 = PhotoImage(file='D:/CODE/PythonProjects/ModernGUI/images/IndrAjitDas.png')
image_label2 = Label(frame_2, image=img2, bg='white')
image_label2.photo = img2  # Store reference to the image
image_label2.place(x=0, y=0)

Button(frame_2, width=21, pady=7, text = 'Jiya Bhai', bg = '#57a1f8', fg='White', border=0).place(x=0, y = 155)
####################################
frame_3 = Frame(main_window, width=150, height=250, bg='white')
frame_3.place(x=390, y=100)

img3 = PhotoImage(file='D:/CODE/PythonProjects/ModernGUI/images/IndrAjitDas.png')
image_label3 = Label(frame_3, image=img3, bg='white')
image_label3.photo = img3  # Store reference to the image
image_label3.place(x=0, y=0)

Button(frame_3, width=21, pady=7, text = 'Satoru', bg = '#57a1f8', fg='White', border=0).place(x=0, y = 155)
######################################
frame_4 = Frame(main_window, width=150, height=250, bg='white')
frame_4.place(x=560, y=100)

img4 = PhotoImage(file='D:/CODE/PythonProjects/ModernGUI/images/IndrAjitDas.png')
image_label4 = Label(frame_4, image=img4, bg='white')
image_label4.photo = img4  # Store reference to the image
image_label4.place(x=0, y=0)

Button(frame_4, width=21, pady=7, text = 'Narbu Musk', bg = '#57a1f8', fg='White', border=0).place(x=0, y = 155)
#######################################
frame_5 = Frame(main_window, width=150, height=250, bg='white')
frame_5.place(x=730, y=100)

img5 = PhotoImage(file='D:/CODE/PythonProjects/ModernGUI/images/IndrAjitDas.png')
image_label5 = Label(frame_5, image=img5, bg='white')
image_label5.photo = img5  # Store reference to the image
image_label5.place(x=0, y=0)

Button(frame_5, width=21, pady=7, text = 'Kartik bhai', bg = '#57a1f8', fg='White', border=0).place(x=0, y = 155)

main_window.mainloop()
