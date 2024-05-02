# Import module 
import sqlite3

# Task 1: Connect to the hotel_booking.db database and name the connection object con
con = sqlite3.connect("hotel_booking.db")

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
print(cur.execute('''SELECT * FROM booking_summary''').fetchone())

# Task 4: View first ten rows of booking_summary 
print(cur.execute('''SELECT * FROM booking_summary LIMIT 10''').fetchall())

# Task 5: Pull all records with BRA (Brazil) as country of origin
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = 'BRA';''').fetchall()
# Print the first five rows of bra
print(bra[:5])

# Task 6: Create a new table named bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
                   num INTEGER,
                   hotel TEXT,
                   is_cancelled INTEGER,
                   lead_time INTEGER,
                   arrival_date_year INTEGER,
                   arrival_date_month INTEGER,
                   arrival_date_day_of_month INTEGER,
                   adults INTEGER,
                   children INTEGER,
                   country TEXT,
                   adr REAL,
                   special_requests INTEGER)''')

# Task 7: Insert the object bra into the table bra_customers
cur.executemany('''INSERT INTO bra_customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''', bra)

# Task 8: View the first 10 rows of bra_customers
print(cur.execute('''SELECT * FROM bra_customers LIMIT 10''').fetchall())

# Task 9: Retrieve lead_time rows where the customer cancelled their booking
lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1''').fetchall()

# Task 10: Calculate the average lead time for those who cancelled
cancelled_lead_time_avg = sum(x[0] for x in lead_time_can) / len(lead_time_can)
print("Average lead time for canceled bookings:", cancelled_lead_time_avg)

# Task 11: Retrieve lead_time rows where the customer did NOT cancel their booking
lead_time_not_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0''').fetchall()

# Task 12: Calculate the average lead time for those who did NOT cancel
not_cancelled_lead_time_avg = sum(x[0] for x in lead_time_not_can) / len(lead_time_not_can)
print("Average lead time for non-canceled bookings:", not_cancelled_lead_time_avg)

# Task 13: Retrieve special_requests field for cancelled bookings
cancelled_special_requests = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1''').fetchall()

# Task 14: Calculate the total amount of special requests for cancelled bookings
total_cancelled_special_requests = sum(x[0] for x in cancelled_special_requests)
print("Total special requests for canceled bookings:", total_cancelled_special_requests)

# Task 15: Retrieve special_requests field for non-cancelled bookings
not_cancelled_special_requests = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0''').fetchall()

# Task 16: Calculate the total amount of special requests for non-cancelled bookings
total_not_cancelled_special_requests = sum(x[0] for x in not_cancelled_special_requests)
print("Total special requests for non-canceled bookings:", total_not_cancelled_special_requests)

# Task 17: Commit changes and close the connection
con.commit()
con.close()
