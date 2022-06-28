from operator import itemgetter
data = [['Derek', 7], ['Carrie', 7], ['Bob', 6], ['Aaron', 9]]
data.sort(key=itemgetter(1, 0))
print(data)
print(data[0],[0])
for item in data:
    print(item[0], end='')
    print()
things = [1, 2, 3]
things.append('a')
print(things)
things.extend(['b', 'c'])
print(things)
words = 'this is a test'.split()
print(words)
words_2 = 'Tony,15/01/2000,0111111111' .split(' ,')
print(words_2)