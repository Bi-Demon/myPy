import Model.Server.Server as sv
import re

class admin:
    __ad_username= 'admin'
    __ad_password= 'admin'
    
    def __init__(self, username, password):
        self.username= username
        self.password= password

    def __login(self):
        if re.match(self.__ad_username, self.username) and re.match(self.__ad_password, self.password):
            return 1
        else:
            return 0

    def log(self):
        result= self.__login()

        return result

    def admin_connect(self):
        connection= sv.Getconnect()
        print('Welcome Admin')


        connection.close()




    

        

        
        