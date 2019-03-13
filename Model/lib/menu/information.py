import re

# Đăng ký thông tin cá nhân
def win(name):
    print(name, end='', flush=True)

def regis_inform():
    win('mã sinh viên: ')
    maid= input()
    n_maid= test(r'[a-zA-z0-9]+', maid)

    win('Họ: ')
    hoid= input()
    n_hoid= test(r'[a-zA-Z]+', hoid)

    win('Tên: ')
    tenid= input()
    n_tenid= test(r'[a-zA-Z]+', tenid)

    win('Ngày sinh: ')
    birth= input()

    win('Giới tính\nNam:0 Nữ:1\n')
    sex= input()

    win('Địa chỉ: ')
    address= input()

    win('Số điện thoại: ')
    phone= input()
    n_phone= test(r'0\d{9}', phone) 

    return n_maid, n_hoid, n_tenid, birth, sex, address, n_phone

# kiểm tra hợp lệ
def test(intp, outp):
    while True:
        if not re.match(intp, outp):
            print("Không hợp lệ")
            outp= input()

        else:
            break  

    return outp

 