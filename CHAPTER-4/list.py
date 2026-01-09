friends = ["Alice", "Bob","568.22", "Charlie", "Diana"]
print(friends[3])

#unlike strings, lists are mutable
friends[3]="raja"

print(friends[3])

print(friends [1:4])  #slicing


# Python List Functions Program


# Creating a list
my_list = [10, 20, 30, 40]
print("Original List:", my_list)

# 1. append() → Add element at end
my_list.append(50)
print("After append(50):", my_list)

# 2. extend() → Add multiple elements
my_list.extend([60, 70])
print("After extend([60,70]):", my_list)

# 3. insert() → Add at specific position
my_list.insert(1, 15)  # Insert 15 at index 1
print("After insert(1,15):", my_list)

# 4. remove() → Remove specific value
my_list.remove(30)
print("After remove(30):", my_list)

# 5. pop() → Remove last element
my_list.pop()
print("After pop():", my_list)

# pop(index) → Remove element from index
my_list.pop(2)
print("After pop(2):", my_list)


# 7. count() → Count occurrences
my_list.append(20)
print("After adding 20 again:", my_list)
print("Count of 20:", my_list.count(20))

# 8. sort() → Sort list
my_list.sort()
print("After sort():", my_list)

# Sort in descending order
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)

# 9. reverse() → Reverse list order
my_list.reverse()
print("After reverse():", my_list)

# 10. copy() → Copy list
new_list = my_list.copy()
print("Copied List:", new_list)

# 11. clear() → Remove all elements
new_list.clear()
print("After clear():", new_list)

# 12. len() → Length of list
print("Length of my_list:", len(my_list))

# 13. max() → Maximum value
print("Maximum:", max(my_list))

# 14. min() → Minimum value
print("Minimum:", min(my_list))

# 15. sum() → Sum of values
print("Sum:", sum(my_list))

# 16. Slicing
print("Slicing [1:3]:", my_list[1:3])
print("First two:", my_list[:2])
print("Last two:", my_list[-2:])

# 17. Check element exists
if 20 in my_list:
    print("20 is present in list")

# 18. Join two lists
a = [1, 2]
b = [3, 4]
c = a + b
print("Joined list:", c)

# 19. List comprehension
squares = [x*x for x in range(5)]
print("Squares:", squares)



