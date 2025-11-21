try:

    num1,num2 = eval(input("Enter two numbers separated by a comma: "))

    result = num1/num2
    print("Result:", result)
except ZeroDivisionError :
    print("Division by zero is error !!")

except SyntaxError :
    print("Coma is missing, please enter two numbers separated by a comma !!")

except:
    print("wrong input !!")

else:
    print("No exceptions occurred.")

finally:
    print("Execution completed.")