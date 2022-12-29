 # generators
# generators are iterators

# iterator , iterable
l=[1,2,3] #iterable
for i in l:
    print(i)
print(map(lambda a:a**2, l)) # iterator 
1
2
3

# how loop actually works
l=[1,2,3] #iterable
i=iter(l) # first changes into iter function
print(next(i))# then the next step
print(next(i))# then next
print(next(i))# then next
1
2
3
l=[1,5,7]
for num in map(lambda a:a**2, l):
    print(num)
1
25
49
# l=[1,2,3,4]
# memory -----[..............] stored in the memory, list
#memory ---(1) # only 1 will be used 
# when we will demand for the next number then will have to call it too
# memory is used less
# performance is increased
# one at a time
# list is used when we have to call again and again
 
 
 