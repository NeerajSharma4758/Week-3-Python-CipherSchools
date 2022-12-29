#word counter
d={'h':2, 'a':1, 'h':2}
print(d)
{'h': 2, 'a': 1}
def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count
print(word_counter("isha"))
{'i': 1, 's': 1, 'h': 1, 'a': 1}