from View.menu.Button import *

# ----log in box----------------------------
def makelogin():
    doing= Tk()
    doing.geometry('640x350+150+90')

    loginButton(doing)

def getuser(username, password):
    print(username, password)

# --------sign up box------------------------
def makesignup():
    doing= Tk()
    doing.geometry('720x800')

    signupView(doing)


    