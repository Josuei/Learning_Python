grade_list = [3.5, 3.7, 2.6, 95, 87]
# assign the result of your map function to the variable grades_100scale
grades_100scale = map(lambda grade: grade * 25 if grade <= 4 else grade, grade_list)
# convert grades_100scale to a list and save it as updated_grade_list
updated_grade_list = list(grades_100scale)
# print updated_grade_list
print(updated_grade_list)

books = [["Burgess", 1985],
 ["Orwell", "Nineteen Eighty-four"],
  ["Murakami", "1Q85"],
   ["Orwell", 1984],
    ["Burgess", "Nineteen Eighty-five"],
     ["Murakami", 1985]]
# assign the result of your filter function to the variable  string_titles
string_titles = filter(lambda book: type(book[1]) is str, books)
# convert your filter object to a list stored in the variable string_titles_list
string_titles_list = list(string_titles)
# print the list string_titles_list
print(string_titles_list)

letters = ['r', 'e', 'd', 'u', 'c', 'e']
# remember to import the reduce function
from functools import reduce
# store the result of your reduce function in the variable word
word = reduce(lambda x, y: x+y, letters)
# print word
print(word)
