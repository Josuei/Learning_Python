import itertools
from iter_roster import student_roster

class ClassroomOrganizer:
  def __init__(self):
    self.sorted_names = self._sort_alphabetically(student_roster)
# Open Task 3: Define __iter__() and __next__() protocol within ClassroomOrganizar
  def __iter__(self):
    self.index = 0
    return self

  def __next__(self):
    each_student = self.sorted_names[self.index]
    self.index += 1
    if self.index > len(self.sorted_names):
      raise StopIteration
    return each_student
# Close Task 3: Define __iter__() and __next__() protocol within ClassroomOrganizar
  def _sort_alphabetically(self, students):
    names = []
    for student_info in students:
      name = student_info['name']
      names.append(name)
    return sorted(names)

  def get_students_with_subject(self, subject):
    selected_students = []
    for student in student_roster:
      if student['favorite_subject'] == subject:
        selected_students.append((student['name'], subject))
    return selected_students
# Open Task 4: Method to  retrieve a list of tuples with a combination of 2 students
  def groups_of_2(self):
    groups_of_2 = list(itertools.combinations(self.sorted_names, 2))
    return groups_of_2
# Close Task 4


clase = ClassroomOrganizer()