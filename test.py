#local 
from Calculate.calculate import CALCULATE

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    operator = data['operator']

    return CALCULATE(num1, num2, operator)

if __name__ == '__main__':
    app.run()
