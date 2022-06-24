# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah',
         'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita',
         'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September',
          'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977,
         1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005,
         2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160,
                       175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175,
                       180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast','Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'],
                  ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'],
                  ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'],
                  ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
                  ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M',
           '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B',
           '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B',
           '1.01B', '125B', '12B', '29.4B', '1.76B',
           '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def floater(lst):
    for e in lst:
        if 'B' in e:
            lst[lst.index(e)] = float(e.replace('B', '')) * 1000000000
        elif 'M' in e:
            lst[lst.index(e)] = float(e.replace('M', '')) * 1000000
        else:
            lst[lst.index(e)] = -1.0 #Must have the string value 'Damages not recorded'
    return lst
damages_fixed = floater(damages)

# write your construct hurricane dictionary function here:
def build_dict(names, months, years, max_sustained_wind, areas_affected, damage, death):
    new_dict = {}
    for i in range(len(names)):
        new_dict[names[i]] = {'Name': names[i], 'Month': months[i], 'Years': years[i],
                              'Max Sustained Wind': max_sustained_wind[i], 'Areas Affected': areas_affected[i],
                              'Damage': damage[i], 'Deaths': death[i]}
    return new_dict
hurricane_dictionary = build_dict(names, months, years, max_sustained_winds, areas_affected, damages_fixed, deaths)
print(hurricane_dictionary)
i = 1
for h in hurricane_dictionary.items():
    print(f'{i}. {h}')
    i += 1
print()

# write your construct hurricane by year dictionary function here:
def dict_by_years(dict):
    new_dict = {}
    for key, value in dict.items():
        if value['Years'] not in new_dict:
            new_dict[value['Years']] = [value]
        else:
            new_dict[value['Years']].append(value)
    return new_dict
hurricane_by_years_dict = dict_by_years(hurricane_dictionary)
print(hurricane_by_years_dict)
print()

# write your count affected areas function here:
def count_affected_areas(dict):
    new_dict = {}
    for e in dict.values():
        for area in e['Areas Affected']:
            if area not in new_dict:
                new_dict[area] = 1
            else:
                new_dict[area] += 1
    return new_dict
counting_affected_areas = count_affected_areas(hurricane_dictionary)
print(counting_affected_areas)
print()

# write your find most affected area function here:
def most_affected(dict):
    most_affected_region = ""
    times_affected = 0
    for region in dict:
        if dict[region] > times_affected:
            times_affected = dict[region]
            most_affected_region = region
    return f'The area affected by the most hurricanes is {most_affected_region}, it had {times_affected} hurricanes.'
print(most_affected(counting_affected_areas))
print()

# write your greatest number of deaths function here:
def deathly_hurricane(dict):
    deathly_hurricane = ""
    deaths = 0
    for hurricane in dict.items():
        if hurricane[1]['Deaths'] > deaths:
            deaths = hurricane[1]['Deaths']
            deathly_hurricane = hurricane[0]
    return f'The most deathly hurricane is {deathly_hurricane}, with {deaths} victims.'
print(deathly_hurricane(hurricane_dictionary))
print()

# write a categorization by mortality function here:
def mortality_scale(dict):
    new_dict = {1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in dict.items():
        if hurricane[1]['Deaths'] <= 100:
            new_dict[1].append(hurricane[0])
        elif hurricane[1]['Deaths'] <= 500:
            new_dict[2].append(hurricane[0])
        elif hurricane[1]['Deaths'] <= 1000:
            new_dict[3].append(hurricane[0])
        elif hurricane[1]['Deaths'] <= 10000:
            new_dict[4].append(hurricane[0])
        else:
            new_dict[5].append(hurricane[0])
    return new_dict
mortality_scale_dict = mortality_scale(hurricane_dictionary)
print(mortality_scale_dict)
print()

# write your greatest damage function here:
def greatest_damage(dict):
    greatest_damage = 0
    greatest_damage_hurricane = ""
    for hurricane in dict.items():
        if hurricane[1]['Damage'] > greatest_damage:
            greatest_damage = hurricane[1]['Damage']
            greatest_damage_hurricane = hurricane[0]
    return f'The most damage caused by a hurricane is ${greatest_damage} dollars by the hurricane {greatest_damage_hurricane}.'
print(greatest_damage(hurricane_dictionary))
print()

# write a categorization by damage function here:
def damage_scale(dict):
    new_dict = {'Damages not recorded': [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in dict.items():
        if hurricane[1]['Damage'] < 0:
            new_dict['Damages not recorded'].append(hurricane[0])
        elif hurricane[1]['Damage'] <= 100000000:
            new_dict[1].append(hurricane[0])
        elif hurricane[1]['Damage'] <= 1000000000:
            new_dict[2].append(hurricane[0])
        elif hurricane[1]['Damage'] <= 1000000000000:
            new_dict[3].append(hurricane[0])
        elif hurricane[1]['Damage'] <= 1000000000000000:
            new_dict[4].append(hurricane[0])
        else:
            new_dict[5].append(hurricane[0])
    return new_dict
damage_scale_dict = damage_scale(hurricane_dictionary)
print(damage_scale_dict)