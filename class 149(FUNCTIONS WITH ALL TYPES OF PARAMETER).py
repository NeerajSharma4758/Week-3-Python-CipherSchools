#paramters
# *args
# default parametrs
# **kwargs
# this is the sequence
# default
def func(name='unknown',age=19):
    print(name,age)
func('isha',20)
isha 20
def func(name='unknown',age=19):
    print(name)
    print(age)
func('isha',20)
isha
20
def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)
func("isha",1,2,3,a=1,b=2)
isha
(1, 2, 3)
unknown
{'a': 1, 'b': 2}
 