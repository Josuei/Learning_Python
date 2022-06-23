#Write your function here
def divisible_by_ten(nums):
  nums_div_ten = [num for num in nums if num % 10 == 0]
  return len(nums_div_ten)
print(divisible_by_ten([20, 25, 30, 35, 40]))

def divisible_by_ten_2(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
  return count
print(divisible_by_ten_2([20, 25, 30, 35, 40]))
#-----------------------------------------------------------------------------------------------
#Write your function here
def add_greetings(names):
  lst_names = ["Hello, " + name for name in names]
  return lst_names
print(add_greetings(["Owen", "Max", "Sophie"]))
#Solución sugerida
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list
#-----------------------------------------------------------------------------------------------
#Write your function here
def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

def delete_starting_evens2(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst.pop(0)
  return lst

print(delete_starting_evens2([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens2([4, 8, 10]))
#-----------------------------------------------------------------------------------------------
#Write your function here
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst
print(odd_indices([4, 3, 7, 10, 11, -2]))
#-----------------------------------------------------------------------------------------------
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
print(exponents([2, 3, 4], [1, 2, 3]))
#-----------------------------------------------------------------------------------------------