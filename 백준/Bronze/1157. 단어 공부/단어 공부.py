word = input().upper()
newSet = list(set(word))
word_count = []
for i in newSet:
    word_count.append(word.count(i))

if word_count.count(max(word_count)) >= 2:
    print('?')
else:
    print(newSet[word_count.index(max(word_count))])
