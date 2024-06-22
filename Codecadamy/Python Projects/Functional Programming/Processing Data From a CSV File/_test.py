import csv


load_file_in_context("exercise10.py") # type: ignore

with open('trees.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(reader)
    mapper = map(lambda x: tree(int(x[0].strip()), float(x[1].strip()), int(x[2].strip()), float(x[3].strip())), reader) # type: ignore
    correct_trees = tuple(filter(lambda x: x > 75, mapper))

try:
  # Attempt to access a variable identifier:
  if trees != correct_trees: # type: ignore
    fail_tests("Did you use `filter()` to remove trees with heigh less than 75? Did you use `tuple()` to store all those trees in a tuple?") # type: ignore
  # Write more tests here:
  
except NameError:
  fail_tests("Expected `trees` to be defined.") # type: ignore

pass_tests() # type: ignore
