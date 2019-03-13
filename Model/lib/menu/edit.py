# admin
    # đọc database
def ad_read(conn):
    print("Reading...")

    pointer= conn.cursor()
    pointer.execute("select * from mailsv")

    for row in pointer:
        print(f'row= {row}')

    print()

#Thêm dữ liệu mới
def ad_write(connc):
    pass

#xóa dữ liệu
def ad_drop(connc):
    pass

#cập nhật dữ liệu
def ad_update(connc):
    pass

#user

def urs_read(connc):
    print("Reading...")

    pointer= connc.cursor()
    pointer.execute("select * from mailsv")

    for row in pointer:
        print(f'row= {row}')

    print()

def urs_write(connc):
    pass

def urs_drop(connc):
    pass

def urs_update(connc):
    pass