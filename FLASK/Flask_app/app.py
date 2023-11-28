from  flask import Flask

app=Flask(__name__)

@app.route('/welcome')

def welcome():
    return "Welcome Himbi"
# import controller.user_controller as user_controller
# import controller.product_controller as product_controller

# from controller import product_controller,user_controller
from controller import *
