#summary
d={'name':'isha',"age":19}
#or
d1=dict(name='isha', age=19)
#or
d2={
    'name':'isha',
    'age':19,
}
print(d)
print(d1)
print(d2)
{'name': 'isha', 'age': 19}
{'name': 'isha', 'age': 19}
{'name': 'isha', 'age': 19}
#how to acces data from the dic
#there is no order inside the dictionary
#we cannot use the indexing [0]
d1=dict(name='isha', age=19)
print(d['name'])
isha
#add data inside an empty dic
empty={}
empty['key1']='value1'
empty['key2']='value2'
print(empty)
{'key1': 'value1', 'key2': 'value2'}
#check existence of values inside dict
if  'name' in d
#how to iterate(loop) in dic
#most common method
d={'name':'isha',"age":19}
for key,value in d.items():
    print(f'key is {key} and value is {value}')


    
key is name and value is isha
key is age and value is 19
#to print all the keys
d={'name':'isha',"age":19}
for i in d:
    print(i)
name
age
#to print all the values
d={'name':'isha',"age":19}
for i in d.values():
    print(i)
isha
19
#get method
d={'name':'isha',"age":19}
print(d.get('name'))
#why we use get metthod
# to get rid of errors
isha
d={'name':'isha',"age":19}
#print(d['names']) it will show error
print(d.get("names")) #it will return none
None
# to detele
d={'name':'isha',"age":19}
pop=d.pop('name')
print(d)
{'age': 19}
d={'name':'isha',"age":19}
#popitem
popped=d.popitem()
print(d)
print(popped)
{'name': 'isha'}
('age', 19)
 