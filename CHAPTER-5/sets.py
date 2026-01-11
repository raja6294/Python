#What is a Set in Python?

#A set is a collection that is:

#✔ Unordered
#✔ Mutable (can change)
#✔ Stores unique values only
#✔ Written using { }

my_set = {1, 2, 3, 4}
print(my_set)

letters = set(["a", "b", "c"])
print(letters)

#Creating an Empty Set
empty_set = set()
print(empty_set)

#Duplicate values removed
numbers = {1, 2, 2, 3, 4, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

#Accessing Set Items
for item in my_set:
    print(item)
#Check if an item exists in a set
print(3 in my_set)  # Output: True
print(5 in my_set)  # Output: False

#Adding Items to a Set
my_set.add(5)
print(my_set)
my_set.update([6, 7, 8])
print(my_set)

#Removing Items from a Set
my_set.remove(3)  #Raises an error if 3 is not found
print(my_set)

my_set.discard(10)  # Does not raise an error if 10 is not found
print(my_set)
popped_item = my_set.pop()  #Removes and returns an arbitrary item

print(popped_item)

#Set Operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
#Union
set_union = set_a.union(set_b)
print(set_union)  # Output: {1, 2, 3, 4, 5, 6}

#Intersection
set_intersection = set_a.intersection(set_b)
print(set_intersection)  # Output: {3, 4}

#Difference
set_difference = set_a.difference(set_b)
print(set_difference)  # Output: {1, 2}
set_difference_ba = set_b.difference(set_a) 
print(set_difference_ba)  # Output: {5, 6}

A = {1,2,3,4}
B = {3,4,5,6}

print("Union:", A | B)
print("Common:", A & B)
print("In A not in B:", A - B)
print("In B not in A:", B - A)
