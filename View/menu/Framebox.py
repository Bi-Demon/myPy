from tkinter.font import Font
from ttkthemes import ThemedTk
from tkinter import scrolledtext

from tkinter.ttk import *
from tkinter import *


#----Tạo form Quản Lý Sinh Viên------------------------------------------
class mainbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self,parent)

        self.parent= parent

        self.font= Font(family= 'Consolas', size= 16, weight='bold')

        self.theFrame()

    def theFrame(self):

        self.parent.title('STUDENT MANAGEMENT')
        self.pack(fill= BOTH, expand= True)
        
        betweenline= Canvas(self)
        betweenline.create_line(320, 70, 320, 300)
        betweenline.pack(fill= BOTH, expand= 1)

#----------Tạo form Đăng nhập--------------------------------------------------
class loginbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent

        self.font= Font(family= 'Consolas', size= 16, weight='bold')

        self.theFrame()

    def theFrame(self):
        self.parent.title('LOGIN')
        self.pack(fill= BOTH, expand= True)

#----------Tạo form Đăng ký--------------------------------------------------
class signupbox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent= parent

        self.font= Font(family= 'Consolas', size= 14, weight='bold')

        self.theFrame()

    def theFrame(self):
        self.parent.title('SIGN UP')
        self.pack(fill= BOTH, expand= True)