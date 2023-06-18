import requests

def calculate(num1, num2, operator):
    payload = {'num1': num1, 'num2': num2, 'operator': operator}
    req = requests.post('http://localhost:5000/calculate', json=payload)
    return req.json()


result = calculate(5, 3, '+')
print(f'5 + 3 = {result}')

result = calculate(10, 7, '-')
print(f'10 - 7 = {result}')

result = calculate(4, 6, '*')
print(f'4 * 6 = {result}')

result = calculate(8, 2, '/')
print(f'8 / 2 = {result}')
