import mysql.connector

connection = mysql.connector.connect(host='172.20.241.9',
                                         database='measurements',
                                         user='dbaccess_ro',
                                         password='vsdjkvwselkvwe234wv234vsdfas')
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM rawdata WHERE groupid = 61")
       
        myresult = mycursor.fetchall()
        #print(myresult)
   



