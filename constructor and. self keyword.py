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
