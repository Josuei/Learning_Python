from collections import UserList
from collections import UserString
data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!
class ListSorter(UserList):
  def append(self, item):
    self.data.append(item)
    self.data.sort()

sorted_list = ListSorter(data)
print(sorted_list)
sorted_list.append(2)
print(sorted_list)

#UserStringExercise
str_name = 'python powered patterned products'
str_word = 'patterned '

# Write your code below!
class SubtractString(UserString):
  def __sub__(self, other):
    if other in self.data:
      self.data = self.data.replace(other, '')

subtract_string = SubtractString(str_name)
subtract_string - str_word
print(subtract_string)