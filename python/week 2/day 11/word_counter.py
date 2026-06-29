text=input("Enter sentence: ")
words=text.split()
freq={}
for word in words:
    freq[word]=freq.get(word, 0)+1

print(freq)
for word,count in sorted(freq.items(), key=lambda x:x[1], reverse=True):
    print(f"{word} : {count}")
