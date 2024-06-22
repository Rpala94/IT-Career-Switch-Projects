load_file_in_context("exercise9.py") # type: ignore

try:
  # Attempt to access a variable identifier:
  trees # type: ignore
  if trees[-1] != (31, 20.6, 87, 77.0): # type: ignore
    fail_tests("Does your `map()` correctly import the data and store them in the appropriate fields?1") # type: ignore
  elif trees[1] != (2, 8.6, 65, 10.3): # type: ignore
    fail_tests("Does your `map()` correctly import the data and store them in the appropriate fields?2") # type: ignore
  
except NameError:
  fail_tests("Expected `trees` to be defined.") # type: ignore

pass_tests() # type: ignore
