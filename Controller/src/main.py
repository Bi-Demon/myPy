# from lib.usr.user import user as urs
# from lib.root.r_admin import admin as root
# import module.login as lg
# import Server.Server as sv

# def login():
#     while True:
#         user=lg.login('User: ')
#         passw=lg.login('PassWord: ')

#         myad= root(user, passw)

#         result= myad.log()
#         if result== 1:
#             myad.admin_connect()

#             break

#         else:
#             myuser= urs(user,passw)
#             myuser.user_connect()

#             break 

# from View.menu.mainbox import *
from Controller.control import *

root= Tk()
root.geometry('640x350+600+300')
app= mainButton(root)
root.mainloop()



