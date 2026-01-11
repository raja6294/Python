#create a empty dictionary and allow 4 friends to enter their favourite languages as values and their names as keys. assume names are unique.
fav_languages = {}
for _ in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favourite programming language: ")
    fav_languages[name] = language
print("Favourite languages of friends:", fav_languages)
