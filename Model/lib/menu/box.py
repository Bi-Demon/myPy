from tkinter import Frame, LEFT, Tk, BOTH, TOP, BOTTOM, RIGHT,RAISED, StringVar
from tkinter.ttk import Frame, Label, Entry, Style, Button

class menu(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent= parent
		self.form()
		
	def form(self):
		self.parent.title('Quản lý sinh viên')
		self.pack(fill= BOTH, expand=True)
		self.style= Style()
		self.style.theme_use('vista')

		frame1= Frame(self)
		frame1.pack(side= TOP )

		lb1= Label(frame1, text='Tài khoản', width= 10)
		lb1.pack(side= LEFT,expand=True)

		entry1= Entry(frame1)
		entry1.pack(ipadx= 70,pady= 50,ipady=5, expand=True)

		frame2= Frame(self)
		frame2.pack(side= TOP)

		lb2= Label(frame2, text='Mật khẩu', width= 10)
		lb2.pack(side= LEFT, expand= True)

		entry2= Entry(frame2)
		entry2.pack(ipadx= 70, ipady=5, expand= True)

		frame3= Frame(self)
		frame3.pack(fill= BOTH)

		regisButton= Button(frame3, text='Đăng Ký', width= 15, command= lambda: self.catch_ID(entry1.get(), entry2.get()))#commnad)
		regisButton.pack(side= TOP,pady= 20)

		logButton= Button(frame3, text='Đăng Nhập', width= 15, command= lambda: self.catch_ID(entry1.get(), entry2.get()))#commnad)
		logButton.pack(side= TOP)

		frame4= Frame(self)
		frame4.pack(fill= BOTH)
		quitButton= Button(frame4, text= 'Thoát', width= 15, command= self.quit)
		quitButton.pack(side= TOP, pady= 30)

	def catch_ID(self,username, password):
		self.username= username
		self.password= password

		print(self.username,self.password)



root= Tk()
root.geometry('640x350+600+300')
app= menu(root)
root.mainloop()