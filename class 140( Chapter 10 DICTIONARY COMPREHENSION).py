#square={1:1,2:4,3:9}
square={num:num**2 for num in range(1,11)}
print(square)
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
square={f'Square of{num} is':num**2 for num in range(1,11)}
print(square)
{'Square of1 is': 1, 'Square of2 is': 4, 'Square of3 is': 9, 'Square of4 is': 16, 'Square of5 is': 25, 'Square of6 is': 36, 'Square of7 is': 49, 'Square of8 is': 64, 'Square of9 is': 81, 'Square of10 is': 100}
square={f'Square of{num} is':num**2 for num in range(1,11)}
for k,v in square.items():
    print(f'{k}:{v}')
Square of1 is:1
Square of2 is:4
Square of3 is:9
Square of4 is:16
Square of5 is:25
Square of6 is:36
Square of7 is:49
Square of8 is:64
Square of9 is:81
Square of10 is:100
str1="isha"
word_count={char:str1.count(char) for char in str1}
print(word_count)
{'i': 1, 's': 1, 'h': 1, 'a': 1}
# IF ELSE
#d={1:'odd',2:"even"}
odd_even={i:('even' if i%2==0 else 'odd') for i in range(1,11)}
print(odd_even)
{1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd', 6: 'even', 7: 'odd', 8: 'even', 9: 'odd', 10: 'even'}
 