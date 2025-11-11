from tkinter import *
from PIL import Image, ImageTk
import webbrowser

def open_website(url):
    new = 1
    webbrowser.open(url, new=new)

root = Tk()
root.geometry("925x500+300+200")
root.title("Help Support")
root.configure(bg="white")
root.resizable(False, False)

#title section
title_lb1 = Label(root, text="Help Support", font=("MS Serif", 30, "bold"), bg="white", fg="#000000")
title_lb1.place(x=300, y=20, width=350, height=45)

Frame(root, width=400, height=2, bg='black').place(x=290, y=70)

# Create buttons below the section 
# ------------------------------------------------------------------------------------------------------------------- 
# student button 1
std_img_btn = Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\www.png")
std_img_btn = std_img_btn.resize((180, 180), Image.LANCZOS)
std_img1 = ImageTk.PhotoImage(std_img_btn)

std_b1 = Button(root, command=lambda: open_website("https://www.google.com/"), image=std_img1, cursor="hand2", bg="white", bd=0)
std_b1.place(x=40, y=160, width=180, height=180)

std_b1_1 = Button(root, command=lambda: open_website("https://www.google.com/"), text="Our Website", cursor="hand2", font=("tahoma", 15, "bold"), bg="#00cc66", bd=0, fg="white")
std_b1_1.place(x=40, y=350, width=180, height=45)

# Detect Face  button 2
det_img_btn = Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\facebook.png")
det_img_btn = det_img_btn.resize((180, 180), Image.LANCZOS)
det_img1 = ImageTk.PhotoImage(det_img_btn)

det_b1 = Button(root, command=lambda: open_website("https://www.facebook.com/"), image=det_img1, cursor="hand2", bg="white", bd=0)
det_b1.place(x=270, y=150, width=180, height=180)

det_b1_1 = Button(root, command=lambda: open_website("https://www.facebook.com/"), text="Facebook", cursor="hand2", font=("tahoma", 15, "bold"), bg="#00cc66", bd=0, fg="white")
det_b1_1.place(x=280, y=350, width=180, height=45)

# Attendance System  button 3
att_img_btn = Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\youtube.png")
att_img_btn = att_img_btn.resize((180, 180), Image.LANCZOS)
att_img1 = ImageTk.PhotoImage(att_img_btn)

att_b1 = Button(root, command=lambda: open_website("https://www.youtube.com/"), image=att_img1, cursor="hand2", bg="white", bd=0)
att_b1.place(x=510, y=160, width=180, height=180)

att_b1_1 = Button(root, command=lambda: open_website("https://www.youtube.com/"), text="Youtube", cursor="hand2", font=("tahoma", 15, "bold"), bg="#00cc66", bd=0, fg="white")
att_b1_1.place(x=510, y=350, width=180, height=45)

# Help  Support  button 4
hlp_img_btn = Image.open(r"C:\Users\indra\Documents\Python_Test_Projects\Images_GUI\gmail.png")
hlp_img_btn = hlp_img_btn.resize((180, 180), Image.LANCZOS)
hlp_img1 = ImageTk.PhotoImage(hlp_img_btn)

hlp_b1 = Button(root, command=lambda: open_website("https://www.gmail.com"), image=hlp_img1, cursor="hand2", bg="white", bd=0)
hlp_b1.place(x=730, y=160, width=180, height=180)

hlp_b1_1 = Button(root, command=lambda: open_website("https://www.gmail.com"), text="Gmail", cursor="hand2", font=("tahoma", 15, "bold"), bg="#00cc66", bd=0, fg="white")
hlp_b1_1.place(x=730, y=350, width=180, height=45)

root.mainloop()
