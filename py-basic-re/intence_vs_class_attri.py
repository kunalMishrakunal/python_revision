class Employee:
    language = 'py'#calss attribute
    salary = 1200000#class attribute
    
kunal = Employee()
kunal.language = 'JavaScript' #This is an instance attribute, it will override the class attribute for this instance only
print(kunal.language) #Output: JavaScript
