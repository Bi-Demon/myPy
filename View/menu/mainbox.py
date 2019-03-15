# from tkinter import Canvas,BOTH, W, RAISED
# from tkinter.ttk import Frame, Label, Entry, Style, Button, Combobox

from tkinter.font import Font
from ttkthemes import ThemedTk
from tkinter import scrolledtext

from tkinter.ttk import*
from tkinter import *

class mainbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)

        self.parent= parent
        self.form()

    #----Tạo form Quản Lý Sinh Viên------------------------------------
    def form(self):
        self.parent.title('STUDENT MANAGEMENT')
        self.pack(fill= BOTH, expand= True)
        
        self.style= Style()
        self.style.theme_use('clam')

        betweenline= Canvas(self)
        betweenline.create_line(320, 70, 320, 300)
        betweenline.pack(fill= BOTH, expand= 1)

#-----------cho đăng nhập---------------------------------------------------
class signinbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.loginwindow()

    def loginwindow(self):

        window= ThemedTk(theme='auqa')
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

        self.username= entryuser
        self.password= entrypassword
        self.window= window
        # loginwinButton= ttk.Button(window, text='Log In', command= lambda:getuser(entryuser.get(), entrypassword.get()))
        # loginwinButton.pack(ipadx=30, ipady=10, pady= 30) 

    
# --------cho đăng ký-------------------------------------------------------
class signupbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent
        self.signupwindow()

    def signupwindow(self):
        window= ThemedTk(theme='auqa')
        window.title('Sign Up')
        window.geometry('720x800')

        window.config(bg='light grey')

        labelfont= Font(family='Consolas', size= 14, weight='bold')

        # entry.grid(row, column, rowspan, columnspan, ipadx, ipady)

        label1=Label(window,
                    height='2',
                    width='10',
                    text='First Name*', 
                    font= labelfont)

        label1.grid(row=0, column=0, stick= W)
        
        firstname=Entry(window)
        firstname.grid(row=0, column=1, ipady= 10, ipadx= 40)

        lable2=Label(window,
                    height='2',
                    width='10',
                    text='Last Name*', 
                    font= labelfont)

        lable2.grid(row=0, column=3)

        lastname= Entry(window)
        lastname.grid(row=0, column= 4, ipady= 10, ipadx= 40)

        lable3=Label(window,
                    height='2',
                    width='10',
                    text='Email*', 
                    font= labelfont)

        lable3.grid(row=2, column=0)

        email= Entry(window)
        email.grid(row=2, column=1,ipady=10, ipadx= 40)

        lable4=Label(window,
                    height='2',
                    width='10',
                    text='PassWord*', 
                    font= labelfont)

        lable4.grid(row=2, column=3)

        password= Entry(window)
        password.grid(row=2, column=4,ipady=10, ipadx= 40)

        lable5=Label(window,
                    height='2',
                    width='10',
                    text='Address*', 
                    font= labelfont)

        lable5.grid(row=4, column=0)

        address= scrolledtext.ScrolledText(window, height= 10, width= 40)
        address.grid(row=4, column= 1, columnspan= 3)

        lable6=Label(window,
                    height='2',
                    width='10',
                    text='Phone*', 
                    font= labelfont)

        lable6.grid(row=6, column=0)

        phone= Entry(window)
        phone.grid(row=6, column=1,ipady=10, ipadx= 40)

        lable7=Label(window,
                    height='2',
                    width='10',
                    text='Sex*', 
                    font= labelfont)

        lable7.grid(row=6, column=3)

        Sexcombo= Combobox(window, state='readonly',value= ['Male','Female','Other'])
        Sexcombo.grid(row=6, column=4)

        Sexcombo.current(1)
        Sexcombo.bind('<<ComboboxSelected>>', lambda e:self.callbackSexFunc())

        
    


        Label(window, height='2', width='5',font= labelfont, bg='light grey').grid(row=0, column=2)
        
        Label(window, height='2', width='5',font= labelfont, bg='light grey').grid(row=1, column=0)

        Label(window, height='2', width='5',font= labelfont, bg='light grey').grid(row=2, column=2)

        Label(window, height='2', width='5',font= labelfont, bg='light grey').grid(row=3, column=0)

        Label(window, height='2', width='5',font= labelfont, bg='light grey').grid(row=5, column=0)

        Label(window, height='2', width='5',font= labelfont, bg='light grey').grid(row=6, column=2)

    def callbackSexFunc(self):
        print("New Sex Selected")

        # Label(window, text='Last Name*', font= labelfont).place(x=40, y=0)
        # lastname= Entry(window)
        # lastname.place(x=41, y=0)
    #     firstname= self.creatlabel(window, 'FirstName*', labelfont, 0,0,5,1,0,0)
    #     entryfirstname= self.createntry(window, 0,1,5,5,10,0)

    #     lastname= self.creatlabel(window, 'LastName*', labelfont,0,8,5,1,0,0)
    #     entrylastname= self.createntry(window,0,9,2,5,10,0)

    #     email= self.creatlabel(window,'Email', labelfont, 6,0,5,1,0,0)
    #     entryemail= self.createntry(window,6,1,2,3,30,2)


    # def creatlabel(self,window, textname, fontype, x, y, spanx, spany, px, py):
    #     name= Label(window,text= textname,font= fontype, bg='light grey')
    #     name.grid(row=x, column= y, rowspan= spanx, columnspan= spany, ipadx= px, ipady= py)

    #     return name

    # def createntry(self, window,x, y, spanx, spany, px, py):
    #     name= Entry(window)
    #     name.grid(row= x, column= y,rowspan= spanx, columnspan= spany, ipadx= px, ipady= py)

    #     return name




