square=[]
for i in range(1,11):
    square.append(i**2)
print(square)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
square=[i**2 for i in range(1,11)]
print(square)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# if 
even=[i for i in range(1,11) if i%2==0]
print(even)
[2, 4, 6, 8, 10]
#if else 
odd_even=[i*2 if(i%2==0) else -i for i in range(1,11)]
print(odd_even)
[-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
#nested

new=[[ i for i in range(1,4)] for j in range(3)]
print(new)
[[1, 2, 3], [1, 2, 3], [1, 2, 3]]