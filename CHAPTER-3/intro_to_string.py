#string is a data type to store sequence of characters 
s="hello raja"
print(s)
print(type(s))
print(len(s))  #length of string
print(s[0])    #first character
print(s[4]) 
#5th character
print(s[-1])   #last character
print(s[-3])  #3rd character from last

print(s[0:5])  #substring from index 0 to 4

print(s[6:])   #substring from index 6 to end

print(s[5])   #6th character (space character)

#sl =name[start index : end index -1]  last index is not included

print(s[:5])  #substring from start to index 4
print(s[:])   #full string

print(s[::2])  #print alternate characters gap one character

print(s[1::2])  #print alternate characters starting from index 1
print(s[::-1])  #print string in reverse order

a="34560955674"
print(a[1:7:3]) 

name="rajabanerjee"
print(len(name))
print(name.endswith("jee"))
print(name.startswith("ha"))
print(name.capitalize())
print(name.upper())

p="python is a good language \nbut java is also a important language " #\t is tab, 

print(p)


