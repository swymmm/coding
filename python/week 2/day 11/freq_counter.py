text="apple banana mango banana apple orange apple"
words=text.split()
freq={}

for word in words:
    freq[word]=freq.get(word,0)+1

print(freq)

#sort by key
for word,count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    print(f"{word} : {count}")