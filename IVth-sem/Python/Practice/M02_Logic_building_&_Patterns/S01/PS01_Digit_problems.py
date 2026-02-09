'''
Docstring for IVth-sem.Python.Practice.M02_Logic_building_&_Patterns.S01.PS01_Digit_problems
1. write a python code to count the digits of a number
ex. 15678-->output: 5
2. sum of the digits of a number?
ex.12345-->1+2+3+4+5 = 15
3. Product of the digits of a number?
4. Reverse the number?
5. Count the even and odd digits


n = int(input())
count = 0
while n > 0:
    count += 1
    n //= 10
print("Number of digits:", count)

n = int(input())
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
    print("Number of digits:", sum)

num = int(input("Enter a number:"))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)

'''
n = int(input("enter n"))
even = 0
odd = 0
while n > 0:
    d = n % 10
    if d % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
print(even)
print(odd)