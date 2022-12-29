#kwargs( keyword argument)
#**kwargs( double star operator)
# kwargs as a parameter
def fun(**kwargs):
    print(kwargs)
    print(type(kwargs))
fun(first_name='isha',last_name="verma")
# gather in dictionary
{'first_name': 'isha', 'last_name': 'verma'}

def fun(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')
fun(first_name='isha',last_name="verma")
first_name:isha
last_name:verma
def fun(name,**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')
fun('athira',first_name='isha',last_name="verma")
first_name:isha
last_name:verma
# dictionary unpacking
def fun(**kwargs):
    for k,v in kwargs.items():
        print(f'{k}:{v}')
d={'name':"athira","age":19}
fun(**d)
name:athira
age:19