#Function = reusable block of code

def greet():
    print("Hello")
    print("Welcome to Python")
greet() # Hello Welcome to Python
print(greet) # <function greet at 0x7f8c8c8c8c8>
print(greet()) # Hello Welcome to Python None

#function with return value
def add(a,b):
    return a + b
result = add(3, 4)
print(result)


#default parameter
def green(name = "Camron" ):
    print("Hello", name + " babu")
green()

green("Kunalal")

#*args = multiple values passs karne ke liye
def add(*number):
    print(number)
add("Ram", "Shayam", "Mohan")

#**kwargltiple key value pair pass karne ke liye
def info(**data):
    print(data)
info(Name = "Radha", Age = 25, City = "Delhi")


#Recursion = function calling itself

def factorial(n):
    if n == 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))


