#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:parameter>")
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route("/count/<int:parameter>")
def count(parameter):
    nums = ""
    for x in range(0,parameter):
        nums += f"{x}\n"
    return nums

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1,operation,num2):
    result = None
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "div":
        result = num1 / num2
    elif operation == "%":
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)