# we use enumerate function with for loop to track position
# item in iterable
# without enumerate
names=['abc','abcd','isha']
pos=0
for name in names:
    print(f"{pos} --> {names}")
    pos+=1
    
    
0 --> ['abc', 'abcd', 'isha']
1 --> ['abc', 'abcd', 'isha']
2 --> ['abc', 'abcd', 'isha']
# with enumerate
names=['abc','abcd','isha']
for pos,name in enumerate(names):
     print(f"{pos} --> {names}")
    
    
0 --> ['abc', 'abcd', 'isha']
1 --> ['abc', 'abcd', 'isha']
2 --> ['abc', 'abcd', 'isha']
# Define a function that take two arguments
# 1.) list containing string
# 2.) string that want to find in your list
# and this function will return the index of string in your list and

# if string is not present then return -1
names=['abc','abcd','isha']
def find_pops(l,target):
    for pops,name in enumerate(l):
        if name== target:
            return pos
        return -1
print(find_pops(names,'isha'))
    
-1
 