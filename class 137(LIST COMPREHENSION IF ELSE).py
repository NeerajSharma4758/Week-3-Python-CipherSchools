# if else
# if odd then negative
#if even then multiply it with 2
nums=[1,2,3,4,5,6,7,8,9,10]
new=[]
for i in nums:
    if i%2==0:
        new.append(i*2)
    else:
        new.append(-i)
print(new)
        
[-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]
nums=[1,2,3,4,5,6,7,8,9,10]
new_list=[i*2 if(i%2==0) else -i for i in nums] 
print(new_list)
[-1, 4, -3, 8, -5, 12, -7, 16, -9, 20]