import random

name = "Isis"
question = "¿Estaré haciendo bien monopolizando la sesión de mi compañerx?"
answer = ""
random_number = random.randint(1, 9)
print()

if random_number == 1:
  answer = "Yes - definitivamente"
elif random_number == 2:
  answer = "Es decididamente así"
elif random_number == 3:
  answer = "Sin duda"
elif random_number == 4:
  answer = "Respuesta confusa, prueba otra vez"
elif random_number == 5:
  answer = "Pregunta de nuevo después"
elif random_number == 6:
  answer = "Mejor no decirte ahora"
elif random_number == 7:
  answer = "Mis fuentes dicen que no"
elif random_number == 8:
  answer = "No se ve tan bien"
elif random_number == 9:
  answer = "Bastante dudoso"
else:
  answer = "Error"
if name == "":
  print("Pregunta: " + question)
else:
  print(name + " pregunta: " + question)
if question == "":
  print(name + " haz una pregunta, poe.")
else:
  print("El Universo dice que: ", answer)


toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
pizza_and_prices =[[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
pizza_and_prices.sort()
cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()


single_digits = range(10)
squares = []
for digit in single_digits:
  print(digit)
  squares.append(digit ** 2)
print(squares)
cubes = [cube ** 3 for cube in single_digits]
print(cubes)


hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

#Crear variable para calcular el precio total
total_price = 0

#Loop para calcular el total de los precios de cada corte
for price in prices:
  total_price = total_price + price
print(total_price)

#Calcular el promedio de cada corte
average_price = total_price / len(prices)
print("Average Haircut Price: "+ str(average_price))

#Nueva lista de precios con descueto de $5
new_prices = [price - 5 for price in prices]
print(new_prices)

#Calcular los ingresos de la última semana
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue = total_revenue + prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue))

#Promedio de ingreso por día en la última semana
average_daily_revenue = total_revenue / 7

#Crear descuento para cortes de menos de $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)