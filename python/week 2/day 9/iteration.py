scores=[89,67,78,70,67]

#basic iteration
for s in scores:
    print(s)

#with index using enumerate
for i, s in enumerate(scores, 1):
    print(f"Student {i}: {s}")

#check if item exists
if 66 in scores:
    print("67 is available")