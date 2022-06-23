alphabet = "abcdefghijklmnopqrstuvwxyz"
symbols = " '!.?!"
message_coded = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
message_keyword = "friends"

#Crear una réplica del mensaje encriptado con la palabra clave
message_trial = "La Orden del Fenix! Mestizos! con Ron"
keyword_trial = "Hagrid"
message_repeat_keyword_trial = ""
print(message_trial)

def counter_symbols(characters):
  num_symbols = 0
  for c in characters:
    if c in symbols:
      num_symbols += 1
  return num_symbols

for index in range(len(message_trial)):
  if message_trial[index] not in symbols:
    if index - counter_symbols(message_trial[:index]) < len(keyword_trial):
      message_repeat_keyword_trial += keyword_trial[index - counter_symbols(message_trial[:index])]
    else:
      message_repeat_keyword_trial += keyword_trial[(index - counter_symbols(message_trial[:index])) % len(keyword_trial)]
  else:
    message_repeat_keyword_trial += message_trial[index]
print(message_repeat_keyword_trial)

#Descifrador Vigènere
def vigenere_decorder(message, keyword):
  keyword_message = ""
  decipher_code = ""
  for index in range(len(message)):
    if index - counter_symbols(message[:index]) < len(keyword):
      keyword_message += keyword[index - counter_symbols(message[:index])]
    else:
      keyword_message += keyword[(index - counter_symbols(message[:index])) % len(keyword)]
  else:
    keyword_message += message[index]
  for index in range(len(message)):
    if message[index] not in symbols:
      index_l1 = alphabet.find(message[index])
      index_l2 = alphabet.find(keyword_message[index])
      dec_letter = alphabet[index_l1 - index_l2]
      decipher_code += dec_letter
    else:
      decipher_code += message[index]
  return decipher_code
print(vigenere_decorder(message_coded, message_keyword))


def vigenere_decoder_alt(coded_message, keyword):
  letter_pointer = 0
  keyword_final = ''
  for i in range(0, len(coded_message)):
    if coded_message[i] in symbols:
      keyword_final += coded_message[i]
    else:
      keyword_final += keyword[letter_pointer]
      letter_pointer = (letter_pointer + 1) % len(keyword)
  return keyword_final
print(vigenere_decoder_alt(message_trial, keyword_trial))


def find_best_night(availability_table):
  day = max(availability_table, key = lambda day: availability_table[day])
  return day

class Student:
  # Class variable
  school_name = 'ABC School '

  def __init__(self, name, roll_no):
    self.name = name
    self.roll_no = roll_no

# create first object
s1 = Student('Emma', 10)
print(s1.name, s1.roll_no, Student.school_name)
# access class variable

# create second object
s2 = Student('Jessa', 20)
# access class variable
print(s2.name, s2.roll_no, Student.school_name)


class Coffee:  # Class names should Capitalized.

  coffeelist = []  # Class attribute to track instance names.

  def __init__(self, name, origin, price):
    self.name = name
    self.origin = origin
    self.price = price
    self.coffeelist.append(self.name)

  def print_coffeelist(self):
    print(self.coffeelist)


c1 = Coffee("blackcoffee", "tanz", 55)
c1.print_coffeelist()  # -> ['blackcoffee']
c2 = Coffee("fineroasted", "ken", 60)
c1.print_coffeelist()  # -> ['blackcoffee', 'fineroasted']

# Can also access attribute directly through the class:
print(Coffee.coffeelist)  # -> ['blackcoffee', 'fineroasted']

sentence = "hola coca cola"
print(list(range(10, -1, -1)))

# Define the DriveBot class here!
class DriveBot:
    def __init__(self, motor_speed=0, direction=0, sensor_range=0):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range


robot_1 = DriveBot(5, 90, 10)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)