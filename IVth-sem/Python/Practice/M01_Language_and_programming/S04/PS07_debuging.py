'''
pdb commands:
1.n-->to execute the output in a next Value 
2. p variable-->to get the value of a variable 
3. l--> list near by cod 
4. c--> continue the execution 
5. s--> to start a function 
6. r--> return from the function 
7. h--> help
8. q--> quit the execution

try:
    a = int(input("enter a number:"))
    print(10/a)
except ZeroDivisionError:
    print("can not divisible by zero.")
except ValueError:
    print("Invalid input")
'''
import pdb
def add(a, b):
    pdb.set_trace()
    return a+b
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
print(add(a,b))  