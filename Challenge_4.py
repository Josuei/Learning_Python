#Write your function here
def every_three_nums(start):
  return list(range(start, 101, 3))
print(every_three_nums(91))
#---------------------------------------------------------------------------------------------------
#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end + 1:]
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
#---------------------------------------------------------------------------------------------------
#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
#---------------------------------------------------------------------------------------------------
# Write your function here
# ⚠️En esta solución la forma lst[index] = lst[index] *2 modifica la lista incluso fuera de la función.
def double_index(lst, index):
  # Validar condición de que index !> del total de elementos.
  if index < len(lst):
    # Duplicar elemento del índice
    lst[index] = lst[index] * 2
    return lst
  else:
    return lst
print(double_index([3, 8, -10, 12], 2))
print(double_index([3, 8, -10, 12], 4))

def double_index2(lst, index):
  if index < len(lst):
    new_lst = lst[:index]
    new_lst.append(lst[index] * 2)
    new_lst = new_lst + lst[index + 1:]
    return new_lst
  else:
    return lst
print(double_index2([3, 8, -10, 12], 2))
print(double_index2([3, 8, -10, 12], 4))
#---------------------------------------------------------------------------------------------------
#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    element_1 = lst[int(len(lst) / 2)]
    element_2 = lst[int(len(lst) / 2 - 1)]
    return (element_1 + element_2) / 2
  else:
    return lst[int((len(lst) - 1) / 2)]
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
#---------------------------------------------------------------------------------------------------