class Employee:
    language = "PY"
    salary = 120000
    
    def __init__(self):# this is dunder method which is automatically called
        print("I am creating an object of Employee class")
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")
        
    
    
kunal = Employee()
kunal.name = "Kunal"
print(kunal.name, kunal.salary)
