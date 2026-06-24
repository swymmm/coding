nums=[3,2,5,4,7,3,6,5]
print(nums)

nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)

#sorted() returns new list original remains unchanged
original=[23,65,34]
sorted=sorted(original)
print(original)
print(sorted)