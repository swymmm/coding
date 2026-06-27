#3. Two sets: students who submitted Assignment 1, and students who submitted Assignment 2. 
#Find: (a) students who submitted both, (b) students who submitted only Assignment 1, 
#(c) all students total.

ass1={"Alice","Bob","John","Mary"}
ass2={"Bob","Charlie","David","Eve"}
print(f"students who submitted both: {ass1 & ass2}")
print(f"students who submitted only assignment 1: {ass1 - ass2}")
print(f"all students total: {len(ass1 | ass2)}")