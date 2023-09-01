# Error Handling:

#Compile time Error: or Syntax Error:
print("hi")
print("bye")
printt("hey") # this error printt


# LogicaL Error:
a=10
b=20
c=(a+a)   # input ah olunga kudukala
print(c)

#Run time Error:
a = int(input())
b = int(input())
print(a+b)   #-----> #this input comes output


a = int(input())
b = input()
print(a+b)  #-----># this input doesnt comes output itha handle panna tah try and exception podarom


#try and Except and Finally

try:
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b/c)
    print(d)    # illatha oru variable assume panna name error

except TypeError as e:
    print("TypeError",e)
except ValueError as e:
    print("valueerror",e)
except NameError as e:
    print("NameError",e)
finally:
    print("Done")