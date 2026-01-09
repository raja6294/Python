#A tuple is:
#✔ Ordered
#✔ Indexed
#✔ Can store multiple values
#❌ Cannot be changed (immutable)
my_tuple = (10, 20, 30)
print(my_tuple)

print(my_tuple[0])   # 10
print(my_tuple[1])   # 20

#my_tuple[0] = 100   # ❌ ERROR tuples are immutable
#print(my_tuple)

t = (5,)   # comma is must
print(type(t))
print(t)

student = ("Raja", 21, "IT")

name, age, dept = student

print(name)   # Raja
print(age)    # 21
print(dept)   # IT

#Swapping Values (No temp variable)
a = 10
b = 20
a, b = b, a
print("a:", a)   # 20
print("b:", b)   # 10

# Tuple Functions Program
# Creating a tuple
my_tuple = (50, 20, 30, 40, 20, 10)
print("Original Tuple:", my_tuple)
# 1. count() → Count occurrences
count_20 = my_tuple.count(20)
print("Count of 20:", count_20)

#Tuple inside List (Database style)
records = [
    (1, "Raja", 21),
    (2, "Anita", 22),
    (3, "Suresh", 20)
]
for record in records:
    print("ID:", record[0], "Name:", record[1], "Age:", record[2])
    
#4. Returning Multiple Values from Function
    
    
def calc(a, b):
    return a+b, a-b, a*b

result = calc(10, 5)
print(result)        # (15, 5, 50)

s, d, m = calc(10,5)
print(s, d, m)
