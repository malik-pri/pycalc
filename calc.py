def compute(expression):
    num0, operator, num1 = expression.split(' ')
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None
