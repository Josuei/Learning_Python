# Write your code below:
import itertools

max_money = 15
options = []
cat_toys = [('laser', 1.99), ('fountain', 5.99), ('scratcher', 10.99), ('catnip', 15.99)]

cat_toy_iterator = iter(cat_toys)
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))
print(next(cat_toy_iterator))

#State 4
toy_combos = list(itertools.combinations(cat_toys, 2))
print("\n"+ str(toy_combos) + "\n")

for combo in toy_combos:
  print(combo)
  sum_toys = 0
  for i in range(len(combo)):
    sum_toys += combo[i][1]
  if sum_toys <= 15:
    options.append(combo)

print("\n" + str(options))