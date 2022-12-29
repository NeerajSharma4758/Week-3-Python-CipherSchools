numbers=[1,2,3,4] #iterables
squares=map(lambda a:a**2, numbers) #iterator
print(squares)
for i in numbers:
    print(i)
for j in squares:
    print(j)

1
2
3
4
1
4
9
16
# iterables == lists , tuples , strings
# for loop
# step 1 call iter function
#iter(number) ---> iterator
# next(iter(numbers))
# this is how for loop works
numbers=[1,2,3,4] #iterables
squares=map(lambda a:a**2, numbers)
number_iter=iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(iter(numbers))
1
2
3
4

numbers=[1,2,3,4] #iterables
squares=map(lambda a:a**2, numbers) #iterator
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
1
4
9
16
 