# Write your count_first_letter function here:
def count_first_letter(names):
  ln_dict = {}
  for last_name in names:
    if last_name[0] not in ln_dict:
      ln_dict[last_name[0]] = 0
    ln_dict[last_name[0]] += len(names[last_name])
  return ln_dict

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}

def add_tax(total):
  tax = total * 0.06
  new_total = total + tax
  return new_total

def add_tip(total):
  tip = total * .2
  new_total = total + tip
  return new_total


def total_bill(func, value):
  total = func(value)
  return "The total amount owed is $" + str(total) + ". Thank you! :)"


print(total_bill(add_tax, 100))
print(total_bill(add_tip, 100))

bills = [115, 120, 42]

def total_bills(func, list):
  # This list will store all the new bill values
  new_bills = []

  # This loop will iterate through our bills
  for a in list:
    # Here we apply the function to each element of the list!
    total = func(a)
    new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")

  return new_bills


bills = [115, 120, 42]

bills_w_tax = total_bills(add_tax, bills)
bills_w_tip = total_bills(add_tip, bills)
print(bills_w_tax)
print(bills_w_tip)

Book = "La Orden del Fénix"
if type(Book) is str:
  print("This is a string")