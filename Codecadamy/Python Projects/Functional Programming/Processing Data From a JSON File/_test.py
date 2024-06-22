import json


load_file_in_context("exercise11.py") # type: ignore


with open('cities.json') as json_file:
  data = json.load(json_file) 
  cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"]) # type: ignore
  correct_asia = tuple(filter(lambda q: q.continent == "Asia", cities))    
              

try:
  # Attempt to access a variable identifier:
  if asia != correct_asia: # type: ignore
    fail_tests("Did you use `filter()` to obtain all cities that are on the continent of Asia? Did you use `tuple()` to generate a tuple of all of these countries") # type: ignore
  # Write more tests here:
  
except NameError:
  fail_tests("Expected `asia` to be defined.") # type: ignore

pass_tests() # type: ignore
