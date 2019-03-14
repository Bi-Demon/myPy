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

# cho đăng nhập
class signinbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.loginwindow()

    def loginwindow(self):

        window= ThemedTk(theme='equilux')
        window.title('Login')
        window.geometry('640x350')

        window.config(bg='light grey')

        labelfont= Font(family='Consolas', size= 14, weight='bold')

        labeluser= Label(window,text='User',font= labelfont, bg='light grey')
        labeluser.place(x=130, y=50)

        entryuser= Entry(window)
        entryuser.pack(ipadx=60,ipady=5, pady= 50)

        labelpass= Label(window,text='Password', font= labelfont, bg='light grey')
        labelpass.place(x=90, y=170)

        entrypassword= Entry(window)
        entrypassword.pack(ipadx=60, ipady=5, pady=40)

        loginwinButton= ttk.Button(window, text='Log In', command= lambda:self.getuser(entryuser.get(), entrypassword.get()))
        loginwinButton.pack(ipadx=30, ipady=10, pady= 30) 

    def getuser(self, username, password):
        self.user= username
        self.password= password

        print(self.user, self.password)

# cho đăng ký
class signupbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.signupwindow()

    def signupwindow(self):
        window= ThemedTk(theme='equilux')
        window.title('Sign Up')
        window.geometry('720x800')

        window.config(bg='light grey')

        labelfont= Font(family='Consolas', size= 14, weight='bold')

        firstname= self.creatlabel(window, 'FirstName*', labelfont, 0,0)
        entryfirstname= self.createntry(window, 0,1)

        lastname= self.creatlabel(window, 'LastName*', labelfont,0,3)
        entrylastname= self.createntry(window,0,4)



    def creatlabel(self,window, textname, fontype, x, y):
        name= Label(window,text= textname,font= fontype, bg='light grey')
        name.grid(row=x, column= y)

        return name

    def createntry(self, window,x,y):
        name= Entry(window)
        name.grid(row= x, column= y)

        return name




