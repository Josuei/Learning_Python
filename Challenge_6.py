def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i1 in lst1:
        sum1 += i1
    for i2 in lst2:
        sum2 += i2
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
print(larger_sum([1, 9, 5], [2, 3, 7]))
#-----------------------------------------------------------------------------------------------
def over_nine_thousand(lst):
  var = 0
  for num in lst:
    var += num
    if var > 9000:
      break
  return var
print(over_nine_thousand([8000, 900, 120, 5000]))
#-----------------------------------------------------------------------------------------------
def max_num(nums):
  max_value = nums[0]
  for num in nums:
    if num > nums[0]:
      max_value = num
  return max_value
print(max_num([50, -10, 0, 75, 20]))
#-----------------------------------------------------------------------------------------------
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
#-----------------------------------------------------------------------------------------------
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[- 1 - index]:
      return False
  return True
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))