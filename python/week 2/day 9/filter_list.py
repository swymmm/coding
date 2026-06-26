list=[15,8,23,4,42,16,3,99]
a=[l for l in list if l>10]
b=[l**2 for l in list]
c=[l for l in list if l%2==0]

print(f"Greater than 10: {a}")
print(f"Squares: {b}")
print(f"Even numbers: {c}")