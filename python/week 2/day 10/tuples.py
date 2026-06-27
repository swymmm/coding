co_ords=(13.43, 32.06)
rgb=(255, 0, 0)
single=(42,)  #when single value is there, we need to put a comma at the end to make it a tuple
empty=()

#accessing tuple values
print(co_ords[0])
print(rgb[-1])
print(len(co_ords))

#iterate same as list
for c in co_ords:
    print(c)