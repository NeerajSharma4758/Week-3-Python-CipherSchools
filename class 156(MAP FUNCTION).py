num=[1,2,3,4]
def square(a):
    return a**2
[square(1),sqyare(2)]
#map function
num=[1,2,3,4]
def square(a):
    return a**2
print(map(square, num))

num=[1,2,3,4]
def square(a):
    return a**2
square=list(map(square,num))
print(square)
[1, 4, 9, 16]
num=[1,2,3,4]
square=list(map(lambda a:a**2,num))
print(square)
[1, 4, 9, 16]
# list comp
num=[1,2,3,4]
square=[i**2 for i in num]
print(square)
[1, 4, 9, 16]
numbers=[1,2,3,4]
l=[]
for num in numbers:
    l.append(num**2)
print(l)
[1, 4, 9, 16]
names=['abc','abcd','abcde']
length=map(len,names)
for i in length:
    print(i)
for j in names:
    print(j)
     
3
4
5
abc
abcd
abcde
 
 