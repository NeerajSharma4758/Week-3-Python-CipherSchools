def add(a,b):
    return a+b
# but we cannot add more than 2 number
def new(*args):
    #1,2,3,4
    #gather values as a tuple
    total=0
    for num in args:
        total +=num
    return total
print(new(1,2,4,6))
13
# args gives tuple
#kwargs gives dictionary
def new(*args):
    total=0
    for num in args:
        total += num
    return total
l=[1,2,3,4]
print(new(*l)) #unpacking
10
def new(*args):
    total=0
    for num in args:
        total += num
    return total
l=(1,2,3,4)
print(new(*l))
10
# kwargs
def func(**kwargs):
    print(kwargs)
func(name='isha',age=19)
    
{'name': 'isha', 'age': 19}
# all functions
# parameter
# args 
# default parameter
# kwargs
# this is the order
# PADK paramert, args, default parameter , kwargs
 
 