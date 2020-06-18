
phrases = ["everything is fine", "have a seat", "holy cow"]
def toUpperCase(list_to_uppercase):
    return [item.upper() for item in list_to_uppercase]


print(toUpperCase(phrases))

# def toUpperCase(list_to_uppercase):
#     newlist = []
#     for item in list_to_uppercase:
#         newlist.append(item.upper())
#     return newlist

#[thing_in_new for thing_in_old in list_of_stuff // if thing_in_old_meets_condition]


def remove_from_list(list_to_remove, object_to_remove):
    return [item for item in list_to_remove if item != object_to_remove]

print(remove_from_list(['Dallas', 'Kelly', 'Courtney', 'Hayden', 'Chase'], 'Hayden'))
# should return  ['Dallas', 'Kelly', 'Courtney', 'Chase']
#________________________________________________________________________

ingredients = ['onions',
               'habanero hot sauce',
               'tomatoes',
               'tortillas',
               'corn',
               'black beans',
               'avocados',
               'cheese',]
foods_my_kids_hate = ['habanero hot sauce', 'avocados']

def remove_many(list_of_stuff, list_of_things_to_remove):
    return [item for item in list_of_stuff if item not in list_of_things_to_remove]

print(remove_many(ingredients, foods_my_kids_hate))
# should return ['onions', 'tomatoes', 'tortillas', 'corn', 'black beans', 'cheese']

#________________________________________________________________________________________

list_of_frequency = [
     ('her', 33),
     ('all', 12),
     ('which', 12),
     ('she', 7),
     ('their', 7),
]

def print_freq_results(list_of_frequency):
    for item in list_of_frequency:
        print(item[0].rjust(6) + " | " + str(item[1]).ljust(3) + " " + item[1] * "*")


print_freq_results(list_of_frequency)