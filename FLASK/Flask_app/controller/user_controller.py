from app import app
from flask import request,jsonify,send_file
from model.user_model import user_model

from datetime import datetime

class User:
    def __init__(self,name, email, phone, role, password):
        # self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role
        self.password = password

obj=user_model()
@app.route('/user/signup')

def user_signup_controller():
    # return "This is a signup operation"
     return obj.user_signup_model()

@app.route('/user/getall')

def user_getall_controller():
    # return "This is a signup operation"
     return obj.user_getall_model()

@app.route("/user/addone",methods=["POST"])

def user_addone_controller():
    data = request.json
    
    new_user = User(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        role=data['role'],
        password=data['password']
    )
    # print(request.form)
    
    return obj.user_addone_model(new_user)

@app.route("/user/update/<int:user_id>", methods=["PUT"])
def user_update_controller(user_id):
    try:
        data = request.json

        updated_user = User(
              # Assuming you provide the user_id for identifying the user to update
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            role=data['role'],
            password=data['password']
        )
        result = obj.user_update_model(updated_user,user_id)
        return jsonify({"message": result}), 200  # 200 OK status code
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request status code
    
@app.route("/user/delete/<int:user_id>", methods=["DELETE"])
def user_delete_controller(user_id):
    try:
        result = obj.user_delete_model(user_id)

        return jsonify({"message": result}), 200  # 200 OK status code
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request status code


@app.route("/user/patch/<int:user_id>", methods=["PATCH"])
def user_patch_controller(user_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        result = obj.user_patch_model(data,user_id)

        return jsonify({"message": 'User updated successfully'}), 200  # 200 OK status code
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 400 Bad Request status code
    

@app.route('/user/getall/limit/<limit>/page/<page>',methods=["GET"])
def user_pagination_controller(limit,page):
    # return "This is a signup operation"
     return obj.user_pagination_model(limit,page)

@app.route('/user/<user_id>/upload/avatar',methods=["PUT"])
def user_upload_avatar_controller(user_id):

    print(request.files['avatar'])

    file=request.files['avatar']

    # file.save(file.filename)

    # file.save(f"uploads/{file.filename}")

    uniqueFileName=str(datetime.now().timestamp()).replace(".","")
    fileNameSplit=file.filename.split(".")

    ext=fileNameSplit[len(fileNameSplit)-1]
    finalFilePath=f"uploads/{uniqueFileName}.{ext}"

    file.save(f"uploads/{uniqueFileName}.{ext}")

    
    print(f"uploads/{uniqueFileName}.{ext}")

    return obj.user_upload_avatar_model(user_id,finalFilePath)

@app.route('/uploads/<filename>')
def user_getavatar_model(filename):
    return send_file(f"uploads/{filename}")
