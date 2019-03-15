# from View.menu.mainbox import signupbox, signinbox, mainbox
# from View.menu.buttonbox import loginButton, mainButton

from View.menu.buttonbox import *

def makelogin(command):
    loginButton(command)

def makesignup(command):
    signupbox(command)

def getuser(username, password):
    print(username, password)