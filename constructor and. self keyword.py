#price ,ram and processor of laptops:

class laptop:
    def __int__(self):
        self.price=0
        self.ram = ""
        self.processor = ""
    def display(self):
        print("price:",self.price)
        print("ram:", self.ram)
        print("processor:", self.processor)

hp=laptop()
dell = laptop()

hp.price = 50000
hp.ram = "8gb"
hp.processor = "i5"

dell.price = 70000
dell.ram = "16gb"
dell.processor = "i7"

hp.display()
dell.display()

#list out the class of students name and register name

class student:
    def __int__(self):
        self.name= ""
        self.register_number = ""
    def display(self):
        print("name:",self.name)
        print("register_number:", self.register_number)

student1 = student()
student2 = student()

student1.name = "deepika"
student1.register_number = "162350"

student2.name = "titikksha"
student2.register_number = "162558921"

student1.display()
student2.display()



# create a class called fruit create a variable called color using _init_ method."
#create a object called apple"pass the color variable as aparameter through object
class Fruit:
    def __int__(self,col):
        self.color=col

apple=Fruit("black")
print(apple.color)


#list out the class of teachers name and register name
class Teacher:
    def __int__(self,name,reg):
        self.name = name
        self.reg_no = reg
    def display(self):
        print("name:", self.name)
        print("regno:", self.reg_no)

t1= Teacher()
t2= Teacher()

t1.name= "deepika"
t2.regno= "162350"

t1.display()
t2.display()


# Arithmetic operations of class and objects:
class calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print("add", self.num1+self.num2)
    def sub(self):
        print("sub", self.num1-self.num2)
    def mul(self):
        print("mul", self.num1*self.num2)
    def div(self):
        print("div", self.num1/self.num2)

object1= calculator(10,2)
object1.add()
object1.sub()
object1.mul()
object1.div()




#another method not using construtor:
class calculator:
    def add(self,a,b):
        print("add",a+b)

object1= calculator()
object1.add(10,2)
