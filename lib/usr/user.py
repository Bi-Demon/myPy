import Server.Server as sv
import module.register as contact
class user:
    def __init__(self, username, password):
        self.username= username
        self.password= password

    def user_connect(self):
        connection= sv.Getconnect()

        result= self.register()
        connection.close()

    def register(self):
         username, password, ma, ho, ten, birth, sex, address, phone= contact.signup()

         return 0
