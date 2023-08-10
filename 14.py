
try:
    a = int(input("please enter number: "))
    b = int(input("please enter number: "))
    print(a / b)
except ZeroDivisionError as e:
    print("you tried to divide by zero, nu nu nu")
    print(e.args)
except ValueError as e:
    print("bad input")
    print(e.args)
print("aviran")