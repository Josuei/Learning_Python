from iter_roster import student_roster
import iter_classroom_org

student_iterator = iter(student_roster)
for i in range(len(student_roster)):
    print(next(student_iterator))

print()

#for student in student_roster:
#    print(student)
#Task 4 & 5
clase = iter_classroom_org.ClassroomOrganizer()
print(clase.sorted_names)

iter_clase = iter(clase)
for i in range(len(clase.sorted_names)):
  print(next(iter_clase))

tables = clase.groups_of_2()
print(tables)