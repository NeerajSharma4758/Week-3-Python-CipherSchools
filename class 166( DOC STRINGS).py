# what are doc strings
# how to write docstring
# how to see docstring
# what is help function
 # doc string is a message we can give to the user to help the user to understand the function or the code
def add(a,b):
    ''' this fun take 2 numbers and return their sum '''
    return a+b
print(add.__doc__)    
    
 this fun take 2 numbers and return their sum 
# len , sum , min , max, sorted
print(len.__doc__)
Return the number of items in a container.
print(sum.__doc__)
Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types.
print(min.__doc__)
min(iterable, *[, default=obj, key=func]) -> value
min(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its smallest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more arguments, return the smallest argument.
print(max.__doc__)
max(iterable, *[, default=obj, key=func]) -> value
max(arg1, arg2, *args, *[, key=func]) -> value

With a single iterable argument, return its biggest item. The
default keyword-only argument specifies an object to return if
the provided iterable is empty.
With two or more arguments, return the largest argument.
print(sorted.__doc__)
Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order.
# help function
print(help(sum))
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.

None