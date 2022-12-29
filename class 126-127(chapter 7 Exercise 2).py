class 125(word counter)users={
    'name':'isha'
    'age':19
    "fav_movies":['coco','harry potter']
    "fav_songs":['song1','song2']
}
#solution
user={}
name=input("what is your name:")
age=input("what is your age:")
fav_movies=input("what is your fav movies:").split(",")
fav_songs=input("what is your fav songs:").split(",")
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
print(user)
what is your name:isha
what is your age:19
what is your fav movies:coco,harrypotter
what is your fav songs:love
{'name': 'isha', 'age': '19', 'fav_movies': ['coco', 'harrypotter'], 'fav_songs': ['love']}
user={}
name=input("what is your name:")
age=input("what is your age:")
fav_movies=input("what is your fav movies:").split(",")
fav_songs=input("what is your fav songs:").split(",")
user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
for key,value in user.items():
    print(f"{key}:{value}")
what is your name:isha
what is your age:19
what is your fav movies:coco ,m1
what is your fav songs:m2,m3
name:isha
age:19
fav_movies:['coco ', 'm1']
fav_songs:['m2', 'm3']
 