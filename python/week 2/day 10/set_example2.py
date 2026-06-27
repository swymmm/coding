#2. Given list with duplicates: [1, 2, 2, 3, 3, 3, 4, 4, 5]. Print unique values and count of unique values.
nums=[1, 2, 2, 3, 3, 3, 4, 4, 5]
print(nums)
unique_nums=list(set(nums))
print(unique_nums)
print(len(unique_nums))