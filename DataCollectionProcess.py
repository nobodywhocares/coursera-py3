
# Create a function called last_four that takes in an ID number and returns the last four digits.
# For example, the number 17573005 should return 3005. Then, use this function to sort the list
# of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable,
# sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
def last_four(x):
    return str(x)[-4]
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_ids = sorted(ids, key=last_four)
print(sorted_ids)
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids, key=lambda id: str(id)[-4])
print(sorted_ids)

# sort by second letter of each list entry
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda str: str[1])


lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda str: 'Fruit: '+str, lst_check)

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = filter(lambda str: 'B' == str[0], countries)

# Below, we have provided a list of tuples that contain the names of Game of Thrones characters.
# Using list comprehension, create a list of strings called first_names that contains only
# the first names of everyone in the original list.
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [person[1] for person in people]

# Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [item * 2 for item in lst]
print(lst2)

# List comprhension with modification and condition
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [student[0] for student in students if student[1] >= 70]

# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list
# and assigned to the variable opposites if they are both longer than 3 characters each.
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = list(filter(lambda x: (len(x[0]) > 3 and len(x[1]) > 3), zip(l1, l2)))
print(opposites)
# alternative methods
opposites = list(filter(lambda x: (len(x[0]) > 3 and len(x[1]) > 3), zip(l1, l2)))
print(opposites)
opposites = [(w1,w2) for (w1,w2) in list(zip(l1,l2)) if len(w1) > 3 and len(w2) > 3]
print(opposites)

# Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples
# called pop_info. From this list, create a new list called endangered that contains the names of species
# whose populations are below 2500.
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species, population))
print(pop_info)
endangered = [species[0] for species in pop_info if species[1] < 2500 ]
print(endangered)
