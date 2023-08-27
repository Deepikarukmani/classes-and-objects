# Make a Mini Calculator.get input 2 numbers A and B out of 100.
#get input from user whether to add/sub/mul/div
#if user selects add then the two numbers and print the result.

a = int(input("A: "))
b = int(input("B: "))
operation = input("add/sub/mul/div/mod/float: ")
if operation=="add":
    print(a+b)
elif operation=="sub":
    print(a-b)
elif operation=="mul":
    print(a*b)
elif operation=="div":
    print(a/b)
elif operation=="mod":
    print(a%b)
elif operation=="float":
    print(a//b)
else:
    print("invalid operation")

