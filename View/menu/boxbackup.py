# from tkinter import Frame, Tk, Canvas, LEFT, BOTH, TOP, BOTTOM, RIGHT, CENTER,RAISED
from tkinter.ttk import Frame, Label, Entry, Style, Button
from tkinter.font import Font
from ttkthemes import ThemedTk

from tkinter import *

class mainbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)

        self.parent= parent
        self.form()

    # Tạo form Quản Lý Sinh Viên
    def form(self):
        self.parent.title('STUDENT MANAGEMENT')
        self.pack(fill= BOTH, expand= True)
        
        self.style= Style()
        self.style.theme_use('clam')

        betweenline= Canvas(self)
        betweenline.create_line(320, 70, 320, 300)
        betweenline.pack(fill= BOTH, expand= 1)

        myfont= Font(family='Time New Roman Bold', size= 16, weight='bold')
        
        lb1= Label(self, text='Registerd User',font=myfont)
        lb1.place(x=400, y=100)

        lb2= Label(self, text='Create New User',font=myfont)
        lb2.place(x=70, y= 100)

        RegisButton= Button(self, text='Sign Up',font=myfont, bg='white', fg='midnight blue')
        RegisButton.place(x=100, y=150)

        loginButton= Button(self, text='Sign In',font=myfont, bg='midnight blue', fg='white', command= self.loginwindow)
        loginButton.place(x=430, y=150)

        QuitButton= Button(self, text='Quit',font=myfont, bg='firebrick1', fg='white', command= self.quit)
        QuitButton.place(x= 560, y=300)

    def loginwindow(self):

        window= ThemedTk(theme='aqua')
        window.title('Login')
        window.geometry('640x350')

        window.config(bg='light grey')

        labelfont= Font(family='Consolas', size= 14, weight='bold')

        labeluser= Label(window,text='User',font= labelfont)
        labeluser.place(x=130, y=50)

        entryuser= Entry(window)
        # entryuser.pack(weight= 20)
        entryuser.pack(ipadx=60,ipady=5, pady= 50)
        # entryuser.place(x=80,y=50)

        labeluser= Label(window,text='Password', font= labelfont)
        labeluser.place(x=90, y=170)

        entrypassword= Entry(window)
        entrypassword.pack(ipadx=60, ipady=5, pady=40)

        loginwinButton= ttk.Button(window, text='Log In', command= lambda:self.getuser(entryuser.get(), entrypassword.get()))
        loginwinButton.pack(ipadx=30, ipady=10, pady= 30) 

    def getuser(self, username, password):
        self.user= username
        self.password= password

        print(self.user, self.password)





root= Tk()
root.geometry('640x350+600+300')
app= mainbox(root)
root.mainloop()