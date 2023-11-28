import mysql.connector
import json
from flask import make_response
class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="root",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection sucessful")
        except:
            print("Connnection error")

        
    def user_signup_model(self):
        return "This is user signup model"
    
    def user_getall_model(self):
        self.cur.execute("SELECT * from users")

        result=self.cur.fetchall()
        if len(result)>0:
            #  return json.dumps(result)
            res=make_response({"payload":result},200)
            res.headers['Access-Control-Allow-Origin']='*'

            return res
            # return make_response({"payload":result},200)

        else:
            #  return "NO DATA FOUND"
            return make_response({"message":"NO DATA FOUND"},204)

        print(result)
    def user_addone_model(self,user):
        self.cur.execute("INSERT INTO users(name, email, phone, role, password) VALUES(%s, %s, %s, %s, %s)",
                (user.name, user.email, user.phone, user.role, user.password))
        # self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        # self.cur.execute(f"INSERT into users(name,email,phone,role,password) values ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
         
        return  make_response({"message":"User created sucessfully"},200)
    
    def user_update_model(self, user,user_id):
        self.cur.execute("UPDATE users SET name=%s, email=%s, phone=%s, role=%s, password=%s WHERE id=%s",
                     (user.name, user.email, user.phone, user.role, user.password, user_id))
         # Check if any rows were affected by the update
        if self.cur.rowcount > 0:
            # return "User updated successfully"
             return  {"message":"User updated sucessfully"}
        else:
            return  {"message":"Nothing to update"}
        
    def user_delete_model(self, user_id):
        self.cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
        # Check if any rows were affected by the delete
        if self.cur.rowcount > 0:
            return {"message":"User deleted successfully"} 
        else:
            return  {"message":"User not found or no changes made"} 
        

    def user_patch_model(self,data, user_id):
       
        qry="UPDATE users SET "

        for key in data:
            qry +=f"{key}='{data[key]}',"

        qry =qry[:-1] + f" WHERE id={user_id}"

        print(qry)

        self.cur.execute(qry)

        if self.cur.rowcount > 0:
            # return "User updated successfully"
             return make_response({"message":"User updated sucessfully"},200) 
        else:
            return make_response({"message":"Nothing to update"},202) 
        
    def user_pagination_model(self,limit,page):

        limit=int(limit)

        page=int(page)

        start=(page*limit)-limit

        qry=f"SELECT * from users LIMIT {start},{limit}"
        self.cur.execute(qry)

        result=self.cur.fetchall()
        if len(result)>0:
            #  return json.dumps(result)
            res=make_response({"payload":result,"page_no":page,"limit":limit},200)
            res.headers['Access-Control-Allow-Origin']='*'

            return res
            # return make_response({"payload":result},200)

        else:
            #  return "NO DATA FOUND"
            return make_response({"message":"NO DATA FOUND"},204)

        print(result)
    def user_upload_avatar_model(self,user_id,filepath):

        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id='{user_id}'")

        if self.cur.rowcount > 0:
            # return "User updated successfully"
             return make_response({"message":"FILE_UPLOADED_SECESSFULLY"},200) 
        else:
            return make_response({"message":"Nothing to update"},202) 
        
     

       

      