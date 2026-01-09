#erter 5 fruits by user and store them in a list.
fruits=[]
for i in range(5):
    fruit=input("enter the name of fruit: ")
    fruits.append(fruit)
print("the fruits you entered are: ")
for fruit in fruits:
    print(fruit)
    
fruits.sort()
print("the fruits in alphabetical order are: ")
for fruit in fruits:
    print(fruit)
