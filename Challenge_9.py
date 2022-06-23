username = ""
def username_generator(first_name, last_name):
  if len(first_name) > 2 and len(last_name) > 3:
    username = first_name[:3] + last_name[:4]
    return username
  else:
    username = first_name + last_name
    return username
print(username_generator("Abe", "Simpson"))

def password_generator(username):
  return username[-1] + username[:-1]
print(password_generator("AbeSimp"))

def password_generator1(username):
  password = ""
  for index in range(len(username)):
    password += username[index - 1]
  return password
print(password_generator1("AbeSimp"))
"".join("Hello World")
#-----------------------------------------------------------------------------------------------
def author_last_names(lst):
  author_last_names = []
  for index in range(len(lst)):
    lst[index].split()
    author_last_names.append()
#-----------------------------------------------------------------------------------------------

highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)
#Crear una lista con la información de cada poemario
highlighted_poems_list = highlighted_poems.split(",")
print(highlighted_poems_list)

#Limpiar la lista de los espacios innecesarios
highlighted_poems_stripped = [poems.strip() for poems in highlighted_poems_list]
print(highlighted_poems_stripped)
#Alternativa: for poems in highlighted_poems_list: | highlighted_poems_stripped.append(poems.strip())
#highlighted_poems_stripped = [highlighted_poems_list[index].strip() for index in range(len(highlighted_poems_list))]

#Crear sublistas que contengan Poema, autor y año. Se separan por los ":"
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))
print(highlighted_poems_details)
#Alternativa: highlighted_poems_details = [poem.split(":") for poems in highlighted_poems_stripped]
#highlighted_poems_details = [highlighted_poems_stripped[index].split(":") for index in range(len(highlighted_poems_stripped))]

#Separar en listas distintas los títulos, los autores y las fechas
titles = [highlighted_poems_details[index][0] for index in range(len(highlighted_poems_details))]
print(titles)
poets = [highlighted_poems_details[index][1] for index in range(len(highlighted_poems_details))]
print(poets)
dates = [highlighted_poems_details[index][2] for index in range(len(highlighted_poems_details))]
print(dates)

for index in range(len(titles)):
  description = "The poem {title} was published by {poet} in {date}".format(title = titles[index], poet = poets[index], date = dates[index])
  print(description)