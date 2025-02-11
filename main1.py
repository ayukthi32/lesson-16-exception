#activity2 
try:
    num1 , num2 = eval(input("Enter two numbers separated by a comma"))
    result = num1 / num2
    print("Result is" , result)
except ZeroDivisionError:
    print("Division by zero is error")
except SyntaxError:
    print("comma is missing. Enter numbers separated by a comma like this 6 , 9")
except:
    print("Wrong input")
else:
    print("No exceptions")
finally:
    print("This will excute no matter what")