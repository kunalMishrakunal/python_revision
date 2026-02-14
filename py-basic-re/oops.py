#class = A class is a blueprint(template) used to create objects.
#object = An object is an instance of a class. It is a real-world entity that has state and behavior.
# class = Blueprint of car
# object = Actual car created from blueprint = color, model, speed


class Student:
    name = "Kunal"#class variable

s1 = Student()#object of class student
print(s1.name)

# constructor(init method) = A constructor is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the object.
#constructor automatically call hota hai jab bhi object create hota hai
#constructor ka naam hamesha __init__ hota hai
#self = self is a reference to the current instance of the class. It is used
#to access the attributes and methods of the class.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Kunal", 22)
print(s1.name, s1.age)

#instance Method = instance method wo method hota hai jo class ke object(instance) ke saath use hota hai, aur jo boject ke data(variables) ko access aur modify kar sakta hai.
#instance method ko call karne ke liye hume object ka reference dena padta
#instance method me self parameter hota hai, jiska use object ke data ko access karne ke liye kiya jata hai.

class Student:
    def greet(self):#instance method
        print("Hello babu")#instance method me self parameter hota hai, jiska use object ke data ko access karne ke liye kiya jata hai.
        
s1 = Student()#object of class student
s1.greet()#instance method ko call karne ke liye hume object ka reference dena padta

#Inheritance = Inheritance is a fundamental object-oriented programming (OOP) concept that allows a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.
#inheritance = ek class dusri class ke properties use kar sakti hai, aur usme apne properties bhi add kar sakti hai

class Parent:
    def show(self):
        print("Parent class")

class child(Parent):
    def display(self):
        print("Child class")
        
c = child()#object of child class
c.show()#child class ne parent class ke method ko inherit kiya hai, isliye hum child class ke object se parent class ke method ko call kar sakte hai
c.display()#child class ka apna method hai, isliye hum child class ke object se child class ke method ko call kar sakte hai

#Encapsulation = Encapsulation is a fundamental principle of object-oriented programming (OOP) that involves bundling data (attributes) and methods (functions) that operate on the data into a single unit, called a class. It also restricts direct access to some of the object's components, which is a means of preventing accidental interference and misuse of the data. This is typically achieved through the use of access modifiers (like private, protected, and public) to control the visibility of class members.
#Encapsulation = data hiding, data ko hide karna, aur usko access karne ke liye method provide karna
#Encapsulation = data hiding, data ko hide karna, aur usko access karne ke liye method provide karna
# = Data ko protect karna, aur usko access karne ke liye method provide karna

class Student:
    def __init__(self):
        self.__name = "Kunal"
    
s = Student()
#print(s.__name) #AttributeError: 'Student' object has no attribute '__name' 

#Polymorphism = Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables a single interface to represent different underlying data types or classes. Polymorphism allows for flexibility and extensibility in code, as it enables the same method or function to work with different types of objects, providing a way to perform the same operation on different data types without needing to know their specific class.
#Polymorphism = ek method ya function ko different classes ke objects ke saath use karna, bina unke specific class ke baare me jaane
#Same function different behavior = Polymorphism

class Dog:
    def sound(self):
        print("Bark")
        
class Cat:
    def sound(self):
        print("Meow")
        
for animal in (Dog(), Cat()):
    animal.sound()
        
        
        
#Self keyword(interviw Favourite)
#self = self is a reference to the current instance of the class. It is used to access the attributes and methods of the class. It is a convention to use self as the name of the first parameter of instance methods, but you can use any name you like. However, it is recommended to use self for better readability and consistency in code.
#self = current object reference

class Test:
    def show(self):
        print(self)
        
t = Test()
t.show()


#Very Important Interview Questions 🔥

#Prepare these answers:

#What is OOP?

#What is class?

#What is object?

#What is constructor?

#What is inheritance?

#What is polymorphism?

#What is encapsulation?

#What is abstraction?
        

        