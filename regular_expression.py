import re

# pattern = re.compile('this')
pattern = re.compile('search inside of this text')
word = 'search inside of this text! Jimwell Gersalia'

# a = re.search('this', word)
# print(a)
# print(a.span()) #returns index
# print(a.start()) # returns start of index where it occurs
# print(a.end())  # returns end of index where it occurs
# print(a.group())    # returns part of string where there was a match

# same as re.search but we now using the compile
a = pattern.search(word)
# return a list, of how many it occurs in the given argument
b = pattern.findall(word)
# return an object if it fully matches the string of the given argument. Very useful in checking password
c = pattern.fullmatch(word)
# return an object even if the last part is not same.as long as it same on the first
d = pattern.match(word)

print(a)
print(b)
print(c)
print(d)