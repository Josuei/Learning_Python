class School:
  def __init__(self, name, level, numberOfStudents):
    self.__name = name
    self.__level = level
    self.__numberOfStudents = numberOfStudents

  def get_name(self):
    return self.__name

  def get_level(self):
    return self.__level

  def get_numberOfStudents(self):
    return self.__numberOfStudents

  def set_numberOfStudents(self, numberOfStudents):
    self.__numberOfStudents = numberOfStudents

  def __repr__(self):
    return f"The {self.__name} {self.__level} school has {self.__numberOfStudents} students"

class PrimarySchool(School):
  def __init__(self, name, level, numberOfStudents, pickupPolicy):
    super().__init__(name, "Primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return self.pickupPolicy

  def __repr__(self):
    return f"\n{super().__repr__()} and the policy is {self.pickupPolicy}"

class HighSchool(School):
  def __init__(self, name, level, numberOfStudents, sportsTeams):
    super().__init__(name, "High", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    return f"\n{super().__repr__()} and the sports teams are {self.sportsTeams}"

san_antonio = School("San Antonio", "High", 2000)
print(san_antonio)
print(san_antonio.get_name())
print(san_antonio.get_level())
print(san_antonio.get_numberOfStudents())

san_antonio.set_numberOfStudents(2030)
print(san_antonio.get_numberOfStudents())

jean_piaget = PrimarySchool("Jean Piaget", "Primary", 200, "Pickup after 14:00 o'clock.")
print(jean_piaget)
print(jean_piaget.get_name())
print(jean_piaget.get_level())
print(jean_piaget.get_numberOfStudents())
print(jean_piaget.get_pickupPolicy())

san_antonio_high = HighSchool("San Antonio de Huamanga", "whateva", 400, ["Female Basket", "Female Voley", "Male Basket", "Male Voley", "Dance"])
print(san_antonio_high)
print(san_antonio_high.get_name())
print(san_antonio_high.get_level())
print(san_antonio_high.get_numberOfStudents())
print(san_antonio_high.get_sportsTeams())