class Employee:
    language = "PY"
    salary = 120000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")
        
    
    
kunal = Employee()
#kunal.language = "JavaScript" #This is an instance attribute, it will override the class attribute for this instance only
#print(kunal.language) #Output: JavaScript

kunal.getInfo()
