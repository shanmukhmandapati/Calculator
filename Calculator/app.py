from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return("Welcome to Calculator")


@app.route('/add', methods=["GET"])
def add():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2
    return jsonify({'The sum of two numbers is ': result})

@app.route('/sub', methods=["GET"])
def sub():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    return jsonify({'The subtraction of two numbers is ': result})

@app.route('/multiply', methods=["GET"])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2 
    return jsonify({'The multiplication of two numbers is ': result})

@app.route('/division',methods=["GET"])
def division():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1/num2
    return jsonify("The division of two numbers are", result)





if __name__ == '__main__':
    app.run(debug=True)
