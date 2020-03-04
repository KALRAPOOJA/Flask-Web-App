import mysql.connector as mysql

class Database_Login:
    def __init__(self):
        self.db=mysql.connect(host="localhost",
                user="root",
                database="testdb"
                )
    def get_all_info(self):
        cursor=self.db.cursor()
        cursor.execute("SELECT * FROM INFO")
        user_info=cursor.fetchall()
        for data in user_info:
            return({'UserName': data[0], 'Password': data[1]})
    def  insert_user_info(self,info):
        cursor=self.db.cursor()
        cursor.execute("INSERT INTO INFO (UserName, Password) VALUES ('%s', '%s')" % (info['UserName'], info['Password']))
        self.db.commit()
        print(cursor.rowcount, "row inserted.")
        return {
                'status': 'success',
                'message': 'Data Inserted Successfully'
            }
    def get_particular_user(self,name_of_user):
        cursor=self.db.cursor()
        cursor.execute("SELECT * FROM INFO WHERE UserName= '{}'".format(name_of_user))
        User_info=cursor.fetchall()
        for data_user in User_info:
            return ({'UserName': data_user[0], 'Password': data_user[1]})



            
