country_capitals ={
  "Germany": "Berlin",
  "France": "Paris",
  "Spain": "Delhi",
}
country_capitals["Italy"] = "Rome" # adding a new key-value pair

print(country_capitals)

country_capitals["spain"]= "Madrid" # updating the value for the key "Spain"
print(country_capitals)

#print directory value one by one
for country, capital in country_capitals.items():
    print("The capital of", country, "is", capital)
    