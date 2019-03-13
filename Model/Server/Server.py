import pyodbc

#change your name server as your sql server name

def Getconnect():
    connection= pyodbc.connect(
    "Driver={SQL Server};"
    "Server=BIBI-PC;"
    "Database=infstudent;"

    #use window authentication
    "Trusted_Connection=True"

    #use password instead
        #UID="name"
        #PWD="pass";
    )

    return connection
