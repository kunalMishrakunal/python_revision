#print(1: 6: 1)
for i in range(1, 6):
    print(i) # 1 2 3 4 5
    
print(i ,  "Ram")

fru = ["apple", "banana", "cherry"]
for x in fru:
    print(x) # apple banana cherry
    
x = 1
while x <= 5:
    print(x) # 1 2 3 4 5
    x += 1

y = 1
while y <= 5:
    print("Jai shree ram")
    y += 1
    
    

#print evennumbers from 1 to 20 

for  i in range (1, 22):
    if i % 2 == 0:
        print(i) # 2 4 6 8 10 12 14 16 18 20

    
#factorial of a number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact) # 120

#Reverse a number using loop

num = 2345
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num //= 10
print(rev) # 5432

#reverce using recursion

def reverse(s):
    return s[::-1]
print(reverse("ABCDEF"))




