from View.menu.Framebox import *

class mainView(mainbox):
    def __init__(self, parent):
        mainbox.__init__(self, parent)

        self.parent= parent
        self.theLabel()

    def theLabel(self):

        signuplabel= Label(self, text= 'Create New User', font= self.font)
        signuplabel.place(x= 70, y=100)

        loginlabel= Label(self, text= 'Have a Account', font= self.font)
        loginlabel.place(x= 400, y= 100)

class loginView(loginbox):
    def __init__(self, parent):
        loginbox.__init__(self, parent)

        self.parent= parent
        self.theLabel()

    def theLabel(self):

        theUser= Label(self, text= 'Username', font= self.font)
        theUser.place(x= 110, y=50)

        username= Entry(self)
        username.pack(ipadx=60,ipady=5, pady= 50)

        thePassword= Label(self, text= 'PassWord', font= self.font)
        thePassword.place(x=110, y=175)

        password= Entry(self)
        password.pack(ipadx=60, ipady=5, pady=40)

        self.username= username
        self.password= password


class signupView(signupbox):
    def __init__(self, parent):
        signupbox.__init__(self, parent)

        self.parent= parent
        self.theLabel()

    def theLabel(self):

        theFirstName=Label(self, height='2',
                                 width='10',
                                 text='First Name*', 
                                 font= self.font)
        theFirstName.grid(row=0, column=0, stick= W)
                
        firstname=Entry(self)
        firstname.grid(row=0, column=1, ipady= 10, ipadx= 40)

        theLastName=Label(self, height='2',
                                width='10',
                                text='Last Name*', 
                                font= self.font)
        theLastName.grid(row=0, column=3)

        lastname= Entry(self)
        lastname.grid(row=0, column= 4, ipady= 10, ipadx= 40)

        theEmail=Label(self, height='2',
                             width='10',
                             text='Email*', 
                             font= self.font)
        theEmail.grid(row=2, column=0)

        email= Entry(self)
        email.grid(row=2, column=1,ipady=10, ipadx= 40)

        thePassword=Label(self, height='2',
                                width='10',
                                text='PassWord*', 
                                font= self.font)
        thePassword.grid(row=2, column=3)

        password= Entry(self)
        password.grid(row=2, column=4,ipady=10, ipadx= 40)

        theAddress=Label(self, height='2',
                               width='10',
                               text='Address*', 
                               font= self.font)
        theAddress.grid(row=4, column=0)

        address= scrolledtext.ScrolledText(self, height= 10, width= 40)
        address.grid(row=4, column= 1, columnspan= 3)

        thePhone=Label(self, height='2',
                             width='10',
                             text='Phone*', 
                             font= self.font)
        thePhone.grid(row=6, column=0)

        phone= Entry(self)
        phone.grid(row=6, column=1,ipady=10, ipadx= 40)

        theSex=Label(self, height='2',
                           width='10',
                           text='Sex*', 
                           font= self.font)
        theSex.grid(row=6, column=3)

        sex= Combobox(self, state='readonly',value= ['Male','Female','Other'])
        sex.grid(row=6, column=4)

        sex.current(1)
        sex.bind('<<ComboboxSelected>>', lambda e:self.callbackSexFunc())


        Label(self, height='2', width='5',font= self.font).grid(row=0, column=2)
        
        Label(self, height='2', width='5',font= self.font).grid(row=1, column=0)

        Label(self, height='2', width='5',font= self.font).grid(row=2, column=2)

        Label(self, height='2', width='5',font= self.font).grid(row=3, column=0)

        Label(self, height='2', width='5',font= self.font).grid(row=5, column=0)

        Label(self, height='2', width='5',font= self.font).grid(row=6, column=2)

    def callbackSexFunc(self):
        print("New Sex Selected")