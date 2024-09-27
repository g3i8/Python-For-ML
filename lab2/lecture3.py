
sen = input("enter sentence:").strip().split(' ')
counter = {}
for word in sen:
    counter[word] = counter.get(word, 0)+1
print(sorted(counter))

