numbers=list(range(1,11))
#[1,2,3,4,5,6,7,,8,9,10]
#even numbers output
nums=[]
for i in numbers:
    if i%2==0:
        nums.append(i)
print(nums)
        
[2, 4, 6, 8, 10]
numbers=list(range(1,11))
even_nums=[i for i in numbers if i%2==0]
print(even_nums)
[2, 4, 6, 8, 10]
even_nums=[i for i in range(1,11) if i%2==0]
print(even_nums)
[2, 4, 6, 8, 10]
odd=[i for i in range(1,11) if i%2 != 0]
print(odd)
[1, 3, 5, 7, 9]