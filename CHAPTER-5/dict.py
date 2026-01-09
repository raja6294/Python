marks={
    "Raja": 56,
    "Anita": 78,
    "Suresh": 89
}
print(marks["Raja"])

#properties of python dectionary
#it is unordered
#it is mutable
#it is indexed
#it can store multiple values
#cannot store duplicate keys
#dictionary functions program

print(marks.items())  #prints all key value pairs as tuple inside list
print(marks.values()) 
print(marks.keys())
marks.update({"Raja": 90})  #updates value of key
print(marks)

print(marks.get("Anita"))  #fetches value of key
print(marks.get("Vikram"))  #returns None if key not found

#pop() removes key value pair
marks.pop("Suresh")
print(marks)


