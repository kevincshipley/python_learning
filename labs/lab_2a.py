'''Lab 2a: Use string concatenation and the indexing operator to construct
3 words from the string name. Print each word.
'''

print(__doc__)

name = 'grace hopper'
# g r a c e _ h o p p  e  r
# 0 1 2 3 4 5 6 7 8 9 10 11

# pace
# 8, 2, 3, 4
print(name[8] + name[2] + name[3] + name[4])

# chore
# 3, 6, 7, 11, 10
print(name[3] + name[6] + name[7] + name[11] + name[10])

# pepper
# 8, 4, 8, 9, 10, 1
print(name[8] + name[4] + name[8] + name[9] + name[10] + name[1])
