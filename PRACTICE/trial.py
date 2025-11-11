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
def create_developer_frame(x, y, image_path, name):
    frame = Frame(main_window, width=150, height=150, bg='red')
    frame.place(x=x, y=y)

    img = PhotoImage(file=image_path)
    image_label = Label(frame, image=img, bg='white')
    image_label.photo = img  # Store reference to the image
    image_label.place(x=0, y=0)

    # Add a label for the developer's name below the frame
    name_label = Label(main_window, text=name, font=('Arial', 12), bg='white')
    name_label.place(x=x + 75 - len(name) * 4, y=y + 150)

# Example usage:
create_developer_frame(50, 100, 'D:/CODE/PythonProjects/ModernGUI/images/IndrAjitDas.png', 'IndrAjit Das')
create_developer_frame(220, 100, 'D:/CODE/PythonProjects/ModernGUI/images/AnotherDeveloper.png', 'Another Developer')
create_developer_frame(390, 100, 'D:/CODE/PythonProjects/ModernGUI/images/ThirdDeveloper.png', 'Third Developer')
create_developer_frame(560, 100, 'D:/CODE/PythonProjects/ModernGUI/images/FourthDeveloper.png', 'Fourth Developer')
create_developer_frame(730, 100, 'D:/CODE/PythonProjects/ModernGUI/images/FifthDeveloper.png', 'Fifth Developer')

main_window.mainloop()
