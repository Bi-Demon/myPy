from View.menu.mainbox import *
import Controller.control as do

class mainButton(mainbox):

    def __init__(self,parent):

        mainbox.__init__(self, parent)
        self.parent= parent
        self.buttonform()

    def buttonform(self):

        myfont= Font(family='Time New Roman Bold', size= 16, weight='bold')
        
        lb1= Label(self, text='Registered User',font=myfont)
        lb1.place(x=400, y=100)

        lb2= Label(self, text='Create New User',font=myfont)
        lb2.place(x=70, y= 100)

        RegisButton= Button(self, text='Sign Up',font=myfont, bg='white', fg='midnight blue', command= lambda:do.makesignup(self))
        RegisButton.place(x=100, y=150)

        loginButton= Button(self, text='Sign In',font=myfont, bg='midnight blue', fg='white', command= lambda:do.makelogin(self))
        loginButton.place(x=430, y=150)

        QuitButton= Button(self, text='Quit',font=myfont, bg='firebrick1', fg='white', command= self.quit)
        QuitButton.place(x= 560, y=300)



class loginButton(signinbox):
    def __init__(self, parent):
        signinbox.__init__(self, parent)

        self.parent= parent
        self.buttonform()

    def buttonform(self):

        loginwinButton= ttk.Button(self.window, text='Log In',command= lambda:do.getuser(self.username.get(), self.password.get()))
        loginwinButton.pack(ipadx=30, ipady=10, pady= 30) 



# def makelogin(command):
#     loginButton(command)

# def makesignup(command):
#     signupbox(command)

# def getuser(username, password):
#     print(username, password)


# root= Tk()
# root.geometry('640x350+600+300')
# app= mainButton(root)
# root.mainloop()