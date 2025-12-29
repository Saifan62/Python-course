try:
    num1,num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result of division is:", result)
except ZeroDivisionError:
    print("division by zero is not allowed")

except SyntaxError:
    print("Invalid input! Please enter two numbers separated by a comma.")

except:
    print("wrong input")

else:
    print("Division performed successfully.")

finally:
    print("Execution completed.")