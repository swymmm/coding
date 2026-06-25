num=[]
for i in range(0, 5):
    n=int(input(f"Enter {i+1} number: "))
    num.append(n)

print(sum(num))
avg=sum(num)/len(num)
print(avg)
print(min(num))
print(max(num))
sorted_num=sorted(num)
print(num)
print(sorted_num)