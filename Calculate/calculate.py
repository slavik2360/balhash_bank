#local
from database.Loger.Loger import Logger

@Logger.log
def CALCULATE(num1: float, num2: float, operator: str):

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return {"error" : "На ноль делить нельзя!"}
        result = num1 / num2

    return str(result)