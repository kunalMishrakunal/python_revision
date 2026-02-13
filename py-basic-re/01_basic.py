var_1 = 10 # int
var_2 = 3.14 # float
var_3 = "Hello, World!" # str
var_4 = True # bool
var_5 = None # NoneType
var_6 = [1, 2, 3, 4, 5] # list
var_7 = (1, 2, 3) # tuple
var_8 = {'name': 'Alice', 'age': 30} # dict
var_9 = {1, 2, 3} # set
print(type(var_1)) # <class 'int'>
print(type(var_2)) # <class 'float'>
print(type(var_3)) # <class 'str'>
print(type(var_4)) # <class 'bool'>
print(type(var_5)) # <class 'NoneType'>
print(type(var_6)) # <class 'list'>
print(type(var_7)) # <class 'tuple'>
print(type(var_8)) # <class 'dict'>
print(type(var_9)) # <class 'set'>
print(var_6.append(6)) # None
print(var_6) # [1, 2, 3, 4, 5, 6]
print(var_7[0]) # 1
d = {"a":1, "b":2}
print(d.get("c"))

#print(var_7[0]= 10) # TypeError: 'tuple' object does not support item assignment
