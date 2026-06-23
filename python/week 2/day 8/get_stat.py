def get_stat(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers), sum(numbers)

lo, hi, avg, sum= get_stat([1,5,3,4,6,3,7,9,3,8,3,5,7])

print(f"Min={lo}, Max={hi}, Average={avg}, Sum={sum}")

