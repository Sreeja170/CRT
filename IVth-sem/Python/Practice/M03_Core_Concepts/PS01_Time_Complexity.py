'''
Time complexity:
Definition: Time complexity can be measured based upon the input.
n = 10
o(1)-->Constant time
o(n)-->single loops
o(n^2)-->two loops
o(logn)-->binary search
o(nlogn)-->linearithmic
o(2^n)-->recursions

print("Time complexity:")
arr = [1,2,3,4,5]
for i in arr:
    print(i,j)

    #Brute Force--->step by step execute, high complexity, neglects the efficiency
            #Optimal Solution--->needs thinking, low complexity
'''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search([10, 20, 30, 58, 46],10))
print(linear_search([10, 20, 30, 58, 46],46))
print(linear_search([10, 20, 30, 58, 46],30))
