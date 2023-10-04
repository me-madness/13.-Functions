def calculate_result(operator, num1, num2):
    return {
        'multiply': num1 * num2,
        'divide': int(num1 / num2),
        'add': num1 + num2,
        'subtact': num1 - num2
    }.get(operator, 'Invalid operator')
    
operator = input()
num1 = int(input())
num2 = int(input())
result = calculate_result(operator, num1, num2)
print(result)