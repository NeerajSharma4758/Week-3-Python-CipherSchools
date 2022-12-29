#we can create a list in one line
#create a list of squares from 1 to 10
squares=[]
for i in range(1,11):
    squares.append(i**2)
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
squares=[i**2 for i in range(1,11)]
print(squares)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
neg=[]
for i in range(1,11):
    neg.append(-i)
print(neg)
[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
neg=[-i for i in range(1,11)]
print(neg)
[-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
names=['Isha','Yatin','Athira']
new=[]
for name in names:
    new.append(name[0])
print(new)
['I', 'Y', 'A']
names=['Isha','Yatin','Athira']
new=[name[0] for name in names]
print(new)
['I', 'Y', 'A']