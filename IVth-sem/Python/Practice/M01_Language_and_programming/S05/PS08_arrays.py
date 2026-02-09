'''import numpy as np
arr = np.array([10,20,30])
print(arr) 
print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers list is:",np.arange(2,10,2))
print("Odd numbers list is:",np.arange(1,10,2))

n = int(input("Enter the size"))
ele = list(map(int, input("enter ele").split()))
print("Array Ele are:",np.array(ele))
import numpy as np
arr = np.array([24,18])
print(np.sum(arr))
3
import numpy as np
arr = np.array([3,2,1])
unique_arr = np.unique(arr)
unique_arr = np.sort(unique_arr)[::-1]
if unique_arr.size >= 3:
    print("Third maximum:", unique_arr[2])
else:
    print("Maximum:", unique_arr[0])
    or

nums = list(map(int, input("Enter nums").split()))
if len(set(nums)) >= 3:
    print(sorted(set(nums))[-3])
else:
    print(max(nums))
'''
nums = list(map(int, input("Enter nums").split()))
inc = True
dec = True
for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        dec = False
    if nums[i] < nums[i-1]:
        inc = False
if inc or dec:
    print("Monotonic Array")
else:
    print("not monotonic array")
