'''
Lab 10: Create two sets. The intersection, union, difference, and symmetric
difference of the two sets should not be empty sets.
'''

print(__doc__)

set1 = {"pony", True, 24, (1, 2, 3), "P"}

set2 = set("Python") # {'h', 'M', 't', 'P', 'o', 'n', 'y', ' '}

''' Perform the four operations listed above to verify they do not result in an
empty set.'''

# intersection: &
# return elements common to both sets
print(set1 & set2) # {'P'}

# union: |
# return elements in both sets
print(set1 | set2)

# difference: -
# return elements in set a that are not in set b
print(set1 - set2)

# symmetric difference: ^
# return elements in set a and set b, but not in both
print(set1 ^ set2)
