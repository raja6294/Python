#wap to create a dictionary of bangali words with values as their english treanslations. provide option to user to look for a word and return its english translation. 
bangali_to_english = {
    "আম": "Mango",
    "কলা": "Banana",
    "সেতু": "Bridge",
    "বই": "Book",
    "পাখি": "Bird"
}
word = input("Enter a Bangali word to translate: ")
translation = bangali_to_english.get(word)
if translation:
    print(f"The English translation of '{word}' is '{translation}'.")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")
    