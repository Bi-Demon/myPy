from time import sleep
import re
import lib.menu.information as infom

# Đăng ký tài khoản
def signup():
    print('REGISTER')
    
    print('Email: ', end='', flush=True)
    username= input()

    n_username= compare(username)

    print('Pass: ', end='', flush=True)
    password= input()

    ma, ho, ten, birth, sex, address, phone= infom.regis_inform() 

    return n_username, password, ma, ho, ten, birth, sex, address, phone 

    

#Kiểm tra acc hợp lệ
def compare(userid):
    while True:
        re_obj= re.match(r'[^@]+@[a-zA-z]+\.[a-zA-Z]+(\.[a-zA-Z])*', userid)

        if not re_obj:
            print('Invalid Email!')
            print('Email: ', end='', flush=True)
            userid= input()

        else:
            break
            

    return userid

# Kiểm tra acc đã đăng ký
def checkacc(uid, pid):
    
    
    pass

#Quản lý thông tin
def info(dta):
    pass    