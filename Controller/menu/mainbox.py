from tkinter import Frame, Tk, Canvas, LEFT, BOTH, TOP, BOTTOM, RIGHT, CENTER,RAISED
from tkinter.ttk import Frame, Label, Entry, Style, Button
from tkinter.font import Font

from tkinter import *

class menu(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)

        self.parent= parent
        self.form()

    # Tạo form Quản Lý Sinh Viên
    def form(self):
        self.parent.title('STUDENT MANAGEMENT')
        self.pack(fill= BOTH, expand= True)
        
        self.style= Style()
        self.style.theme_use('vista')

        betweenline= Canvas(self)
        betweenline.create_line(320, 70, 320, 300)
        betweenline.pack(fill= BOTH, expand= 1)

        myfont1= Font(family='Time New Roman Bold', size= 16, weight='bold')
        
        lb1= Label(self, text='Registerd User',font=myfont1)
        lb1.place(x=400, y=100)

        lb2= Label(self, text='Create New User',font=myfont1)
        lb2.place(x=70, y= 100)

        RegisButton= Button(self, text='Sign Up',font=myfont1, bg='white', fg='midnight blue')
        RegisButton.place(x=100, y=150)

        loginButton= Button(self, text='Sign In',font=myfont1, bg='midnight blue', fg='white')
        loginButton.place(x=430, y=150)

        QuitButton= Button(self, text='Quit',font=myfont1, bg='firebrick1', fg='white', command= self.quit)
        QuitButton.place(x= 560, y=300)

        




root= Tk()
root.geometry('640x350+600+300')
app= menu(root)
root.mainloop()