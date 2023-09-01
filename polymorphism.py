#polymorphism and inheritance:

class Animal():
    def sound(self):
        print("Animal makes a sound")

class dog(Animal):
    def sound(self):
        print("Dog Barks")

class bird():
    def sound(self):
        print("Birds sing")

cow = Animal()
cow.sound()

vicky= dog()
vicky.sound()

parrot=bird()
parrot.sound()


#polymorphism and inheritance:

class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        l=10
        b=20
        print(l*b)

circle=shape()
print(circle.area())

r1=rectangle()
r1.area()


#polymorphism and inheritance:

class person():
    def __init__(self,name):
        self.name = name

class student(person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print(self.name,self.grade)

s1= student("john","A")
s1.display()


#polymorphism with inheritance:

class vechicle():
    def start(self):
        print("vechicle started")

class car(vechicle):
    def start(self):
        print("vechicle started")

bike=vechicle()
bike.start()


