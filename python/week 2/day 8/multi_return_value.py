def min_max(numbers):
    return min(numbers), max(numbers)

lo, hi= min_max([1,5,4,3,2,6,7,5,8,8,8,555,765,3657,22])
print(f"Min={lo}, Max={hi}")
