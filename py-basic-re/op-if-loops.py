a = 10
b = 3
#Arithmetic Operators
print(a + b) # 13
print(a - b) # 7
print(a * b) # 30
print(a / b) # 3.3333333333333335
print(a // b) # 3 = When you want integer result only (no decimal)
print(a % b) # 1
print(a ** b) # 1000 = 10 ** 3 = 10 × 10 × 10

#Comparison Operations
print(a == b) # False
print(a != b) # True
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False

#Logical Operators
x = True
y = False
print(x and y) # False = and operator returns True if both operands are true, otherwise it returns False
print(x or y) # True = or operator returns True if at least one of the operands is true, otherwise it returns False
print(not x) # False = not operator returns the opposite of the operand's boolean value
print(not y) # True = not operator returns the opposite of the operand's boolean value

# Assignment Operators
c = 5
c += 2 # c = c + 2
print(c) # 7
c -= 3 # c = c - 3
print(c) # 4
c *= 4 # c = c * 4
print(c) # 16
c /= 2 # c = c / 2
print(c) # 8.0
c //= 3 # c = c // 3
print(c) # 2.0
c %= 2 # c = c % 2
print(c) # 0.0
c **= 3 # c = c ** 3
print(c) # 0.0

# if-elif-else

age = 18

if age < 18:
    print("You are eligicle to vote")
elif age == 18:
    print("You are just eligible to vote")
else:
    print("You are not eligible to vote")

# Loops

# for loop

for i in range(1, 6):
    print(i) # 1 2 3 4 5
    
for i in range(1, 11):
    print(i, end=' ') # 1 2 3 4 5 6 7 8 9 10

# while loop

i_1 = 1
while i_1 <= 5:
    print(i_1)
    i_1 += 1

print(i_1) # 6

#Break and continue
print("Break")

for i in range(1, 6):
    if i == 3:
        break
    print(i)
    
    
print("Continue")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
    
    
