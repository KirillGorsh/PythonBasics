rivers = {'nile': 'egypt', 'hudson': 'usa', 'volga': 'russia', 'mississippi': 'usa', 'thames': 'uk'}
# print('The KEY runs through VALUE')
for river, country in rivers.items():
    if country == 'usa' or country == 'uk':
        print(f"The {river.title()} runs through {country.upper()}")
    else:
        print(f"The {river.title()} runs through {country.title()}")
print('--------------------')
print('Rivers are:')
for river in rivers.keys():
    print('\t', river.title(), end = ' | ')
print('\n--------------------')
print('Countries are:')
for country in rivers.values():
    if country == 'usa' or country == 'uk':
        print('\t', country.upper(), end = ' | ')
    else:
        print('\t', country.title(), end = ' | ')
print('\n--------------------')
print()
print('-----------------6-11 Cities-------------------')
cities = {'new york': {'country': 'USA', 'population': 9.1, 'fact': 'Big Apple'},
          'istanbul': {'country': 'Turkey', 'population': 15.52, 'fact': 'Constantinople'},
          'tashkent': {'country': 'Uzbekistan', 'population': 2.5, 'fact': 'Stone City'},
          'moscow': {'country': 'Russia', 'population': 12.53, 'fact': 'Kremlin'}}
# "CITY is very beautiful city in COUNTRY. It has POPULATION population and the city is also known as FACT"

for city, info in cities.items():
    # print(city.title())
    # print(info)
    print(f"{city.title()} is very beautiful city in {info['country']}. "
          f"It has {info['population']} mln population and the city is also known as '{info['fact']}'")

# HM: print multiplication table 1-10
print('_______________HM__________________________')
for number in range(1,11):
    for multi in range(1,11):
        print(f"{number} * {multi} = {number*multi}", end = '\t')
    print('')





