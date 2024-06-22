load_file_in_context("script.py")
import sqlite3


try:
  # Attempt to access a variable identifier:
  
  curs
  # Write more tests here:
  # there rows are 
  user_rows = curs.execute('''SELECT * FROM titanic''').fetchmany(10)
  
  # actual rows
  con_test = sqlite3.connect("titanic.db")
  con_test_cursor = con_test.cursor()
  test_rows = con_test_cursor.execute('''SELECT * FROM titanic''').fetchmany(10)
  
  if user_rows != test_rows:
    fail_tests("Did you attach the connection object to the `.cursor()` method like, `con.cursor()`?")
	
except NameError:
  fail_tests("Expected `curs` to be defined.")
	

pass_tests()

