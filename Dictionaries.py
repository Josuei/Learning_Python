letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#15. Agregar letras minúsuclas
letters_lower = [letter.lower() for letter in letters]
letters += letters_lower
points_lower = [number for number in points]
points += points_lower

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
print(letter_to_points)

#Función para calcular el puntaje de un palabra
def score_word(word):
  score = 0
  for letter in word:
    if letter in letter_to_points.keys():
      score += letter_to_points.get(letter)
    else:
      score += 0
  return score
brownie_points = score_word("BROWNIE")
print(brownie_points)

#Diccionario con palabras jugadas por jugador
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

#Diccionario con el puntaje total de las palabras jugadas por cada jugador
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points
print(player_to_points)

#Función para agregar palabras jugadas
def play_word(player, word):
  player_to_words[player].append(word)
play_word("player1", "CHESS")
print(player_to_words)

#Función para actualizar el puntaje con palabras nueva jugadas
def update_point_totals(player, word):
  play_word(player, word)
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points
  return player_to_points
print(update_point_totals("wordNerd", "CUP"))
print(player_to_words)