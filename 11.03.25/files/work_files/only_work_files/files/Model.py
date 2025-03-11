def plus(num1, num2, show_result_func):
    result = num1 + num2
    show_result_func(result)

def minus(num1, num2, show_result_func):
    result = num1 - num2
    show_result_func(result)

def multiply(num1, num2, show_result_func):
    result = num1 * num2
    show_result_func(result)

def divide(num1, num2, show_result_func):
    result = num1 / num2
    show_result_func(result)

def square(num1, num2, show_result_func):
    result = num1 * num2
    result2 = str(result)
    result2 = result2 + "²"
    show_result_func(result2)

def volume(num1, num2, num3, show_result_func):
    result = num1 * num2 * num3
    result2 = str(result)
    result2 = result2 + "³"
    show_result_func(result2)
