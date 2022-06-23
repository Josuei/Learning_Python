guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  val = None
  while True:
    if val is not None:
      line_data = val.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    #Tast 1: Yield the name and age of each guest
    val = yield name, age

#Task 1.1: Call generator function to read the file
guest_list = read_guestlist('guest_list.txt')
#Task 1.2: Print ten first guests
for guest in range(10):
  print(next(guest_list))
#Task 2: Add a new guest 'Jane, 35' using send()
print(guest_list.send('Jane, 35'))
#Task 2.1: Print all the guests
for guest in guest_list:
    print(guest)

#Task 4: Generator expression to recover all guests over 21
print() # Just to print a new line
guests_over_21 = (guest for guest in guests if guests[guest] >= 21)
for guest in guests_over_21:
    print(guest)

#Task 5: Genertor functions to assign meals to each table and seats at the tables
def table_one_chicken():
  for i in range(1,6):
    yield ("Chicken", "Table 1", f"Seat {i}")

def table_two_beef():
  for i in range(1,6):
    yield ("Beef", "Table 2", f"Seat {i}")

def table_three_fish():
  for i in range(1,6):
    yield ("Fish", "Table 3", f"Seat {i}")

def combined_tables():
  yield from table_one_chicken()
  yield from table_two_beef()
  yield from table_three_fish()

table_assignment = combined_tables()

#Task 6: Generator function to assign tables and seats to each guest
def assign_table_seat(guests_list):
  for name in guests_list:
    yield (name, next(table_assignment))
#Task 6.1: Print all the guests and their assigned tables and seats
guest_assignment = assign_table_seat(guests)
for guest in guest_assignment:
  print(guest)