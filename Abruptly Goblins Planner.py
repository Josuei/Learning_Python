gamers = []
def add_gamer(gamer, gamers_list):
  if "name" in gamer and "availability" in gamer:
      gamers_list.append(gamer)
  return gamers_list
kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
add_gamer(kimberly, gamers)

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def build_daily_frequency_table():
  return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for player in gamers_list:
        for day in player["availability"]:
            available_frequency[day] += 1

calculate_availability(gamers, count_availability)
print(count_availability)

def find_best_night(availability_table):
    best_value = 0
    best_day = ""
    for day in availability_table:
        if availability_table[day] > best_value:
            best_value = availability_table[day]
            best_day = day
    return best_day

game_night = find_best_night(count_availability)
print(game_night)

def available_on_night(gamers_list, day):
    availability_list = []
    for player in gamers_list:
        for d in player["availability"]:
            if d == day:
                availability_list.append(player["name"])
    return availability_list

attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = """
Dear {name},

The Sorcery Society is happy to invite you to our {game} night, we really hope to have you. Come by on {day_of_week} and have a blast!

Magically yours,
The Sorcery Society
"""

def send_email(gamers_who_can_attend, day, game):
  for player in gamers_who_can_attend:
      print(form_email.format(name=player, day_of_week=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")

players_unable_to_attend_best_night = [gamer["name"] for gamer in gamers if gamer["name"] not in attending_game_night]
print(players_unable_to_attend_best_night)

unable_to_attend_best_night = [gamer for gamer in gamers if gamer["name"] not in attending_game_night]
second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")