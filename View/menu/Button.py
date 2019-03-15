from View.menu.Labelbox import *
# from tkinter import *
import Controller.control as do

class mainButton(mainView):
    def __init__(self, parent):
        mainView.__init__(self, parent)

        self.parent= parent
        self.theButton()

    def theButton(self):
        register= Button(self, text= 'Sign Up', 
                               font= self.font, 
                               bg= 'dark green', 
                               fg= 'white', 
                               relief= FLAT,
                               command= do.makesignup)
        register.place(x=100, y=150)

        login= Button(self, text= 'Log In', 
                            font= self.font, 
                            bg= 'white', 
                            fg= 'dark green', 
                            relief= FLAT, 
                            command= do.makelogin)
        login.place(x=430, y=150)

        Exit= Button(self, text='Quit',
                           font= self.font, 
                           bg='firebrick1', 
                           fg='white', 
                           relief= FLAT, 
                           command= self.quit)
        Exit.place(x= 560, y=300)

class loginButton(loginView):
    def __init__(self, parent):
        loginView.__init__(self, parent)

        self.parent= parent
        self.theButton()

    def theButton(self):
        
        login= Button(self, text= 'Log In', 
                            font= self.font,
                            bg='bisque4', 
                            fg='white', 
                            relief= FLAT,
                            command= lambda:do.getuser(self.username.get(),self.password.get()))
        login.pack(ipadx=30, ipady=10, pady= 30) 