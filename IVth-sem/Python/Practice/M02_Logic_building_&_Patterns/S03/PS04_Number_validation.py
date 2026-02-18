'''
n = int(input())
l = len(str(n))
res = 0
for i in str(n):
    res += int(i) ** l
if n == res:
    print("Armstrong")
else:
    print("not Armstrong")

#Perfect number
n = int(input())
s = 0
for i in range(1, n//2 + 1):
    if n % i == 0:
        s += i
print("perfect" if n == s else "not perfect")
'''
def factorial(n):
    if n < 0:
        print()

