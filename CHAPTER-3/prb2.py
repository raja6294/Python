#display, dear raja you are selected

letter = '''Dear <|name|>, 
You are selected ! 
<|date|>'''

print(letter.replace("<|name|>", "Raja").replace("<|date|>","24 September 2028"))




# Original sentence
text = "Python is easy to learn. Python is powerful."

print("Before replacement:")
print(text)

# Replace 'Python' with 'Java'
updated_text = text.replace("Python", "Java")

print("\nAfter replacement:")
print(updated_text)

sentence = "I love programming in Python. Python is my favorite language."
print(sentence.replace("Python", "Java"))
print(sentence) # The original sentence remains unchanged so strings are immutable
