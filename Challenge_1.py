# Write your large_power function here:
def large_power(base, exponent):
  result = base ** exponent
  if result > 5000:
    return True
  else:
    return False
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False
#-----------------------------------------------------------------------------------------------
# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (food_bill + electricity_bill + internet_bill + rent) > budget:
    return True
  else:
    return False
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True
#-----------------------------------------------------------------------------------------------
# Write your twice_as_large function here:
def twice_as_large(num1, num2):
    if num2 * 2 < num1:
      return True
    else:
      return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True
#-----------------------------------------------------------------------------------------------
# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False
#-----------------------------------------------------------------------------------------------
# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if num1 + num2 != 10:
    return True
  else:
    return False
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False
#-----------------------------------------------------------------------------------------------