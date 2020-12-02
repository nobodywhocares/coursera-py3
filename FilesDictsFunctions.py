# open file in read mode
file = open("geodata/where.data", "r")
# read the content of file
data = file.read()
# get the length of the data
number_of_characters = len(data)
print('Number of characters in text file :', number_of_characters)

num_words = len(open("geodata/where.data", "r").read().split())
print(num_words)

num_lines = len(open("school_prompt.txt", "r").read().split("\n")) - 1
print(num_lines)

beginning_chars = open("school_prompt.txt", "r").read()[0:30]
print(beginning_chars)

# remove empty line at end of file w/ [:-1]
three = []
for line in open("school_prompt.txt", "r").read().split("\n")[:-1]:
    print(line.split())
    three.append(line.split()[0])

p_words = []
for word in open("school_prompt.txt", "r").read().split():
    if "p" in word:
        p_words.append(word)
print(p_words)

medal_count = {
    'United States': 70,
    'Great Britain': 38,
    'China': 45,
    'Russia': 30,
    'Germany': 17
}
print(medal_count)

swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4}
swimmers['Phelps'] = 23

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods['hockey'] = 3

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds['Spain'] += 2

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = list(golds.keys())
print(countries)

medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45, 'Russia': 30, 'Germany': 17, 'Italy': 22,
               'France': 22, 'Japan': 26, 'Australia': 22, 'South Korea': 14, 'Hungary': 12, 'Netherlands': 10,
               'Spain': 5, 'New Zealand': 8, 'Canada': 13, 'Kazakhstan': 8, 'Colombia': 4, 'Switzerland': 5,
               'Belgium': 4, 'Thailand': 4, 'Croatia': 3, 'Iran': 3, 'Jamaica': 3, 'South Africa': 7, 'Sweden': 6,
               'Denmark': 7, 'North Korea': 6, 'Kenya': 4, 'Brazil': 7, 'Belarus': 4, 'Cuba': 5, 'Poland': 4,
               'Romania': 4, 'Slovenia': 3, 'Argentina': 2, 'Bahrain': 2, 'Slovakia': 2, 'Vietnam': 2,
               'Czech Republic': 6, 'Uzbekistan': 5}
belarus = medal_count['Belarus']

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111,
               "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87,
               "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22,
               "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209,
               "Uganda": 7, "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds['Chile']

US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3,
             "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2,
             "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals['Fencing']

Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3, 'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}
credits = sum(Junior.values())

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for c in str1:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
print(freq)

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
for word in str1.split():
    if word in freq_words:
        freq_words[word] += 1
    else:
        freq_words[word] = 1

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = {}
for word in sent.split():
    if word in wrd_d:
        wrd_d[word] += 1
    else:
        wrd_d[word] = 1

sally = "sally sells sea shells by the sea shore"
characters = {}
for c in sally:
    if c in characters:
        characters[c] += 1
    else:
        characters[c] = 1
print(characters)
ckeys = list(characters.keys())
cvals = list(characters.values())
best_char = ckeys[cvals.index(max(cvals))]
print(best_char)
# Preferred but Coursera UofM claimed "key" was invalid param
best_char = max(characters, key=characters.get)
print(best_char)

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for c in sally:
    if c in characters:
        characters[c] += 1
    else:
        characters[c] = 1
# best_char = max(characters, key=characters.get)
ckeys = list(characters.keys())
cvals = list(characters.values())
worst_char = ckeys[cvals.index(min(cvals))]

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
letter_counts = {}
for c in string1:
    c = c.lower()
    if c in letter_counts:
        letter_counts[c] += 1
    else:
        letter_counts[c] = 1
print(letter_counts)

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = {}
for c in p:
    c = c.lower()
    if c in low_d:
        low_d[c] += 1
    else:
        low_d[c] = 1


def accum(int_list):
    return sum(int_list)


def length(l):
    return "Longer than 5" if len(l) >= 5 else "Less than 5"


def divide(n):
    return n / 2


def sum(n):
    return divide(n) + 6


# Tuple enclosed by parens, List by square brackets, and dict by curly braces
olympics = ("Beijing", "London", "Rio", "Tokyo")

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'),
              ('Tokyo', 'Japan', 2020, 'Future')]
country = [tuple[1] for tuple in tuples_lst]

# Variable assignment from tuple
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp


def create_info_tuple(name, gender, age, bday_month, hometown):
    return (name, gender, age, bday_month, hometown)


gold = {'USA': 31, 'Great Britain': 19, 'China': 19, 'Germany': 13, 'Russia': 12, 'Japan': 10, 'France': 8, 'Italy': 8}
num_medals = [item[1] for item in gold.items()]
print(num_medals)


def sublist(l):
    sub_list = []
    for i in l:
        if 5 != i:
            sub_list.append(i)
        else:
            break
    return sub_list


def check_nums(l):
    sub_list = []
    idx = 0
    while idx < len(l) and 7 != l[idx]:
        sub_list.append(l[idx])
        idx += 1
    return sub_list


def sublist(l):
    sub_list = []
    idx = 0
    while idx < len(l) and "STOP" != l[idx]:
        sub_list.append(l[idx])
        idx += 1
    return sub_list


sum1 = 0
lst = [65, 78, 21, 33]
for x in lst:
    sum1 = sum1 + x
sum2 = 0
idx = 0
while idx < len(lst):
    sum2 += lst[idx]
    idx += 1


def beginning(l):
    sub_list = []
    idx = 0
    while idx < len(l) and "bye" != l[idx] and 10 > len(sub_list):
        sub_list.append(l[idx])
        idx += 1
    print(sub_list)
    return sub_list


def mult(first, second=6):
    if int == type(second):
        return int(first) * int(second)
    else:
        return str(second) * int(first)


def greeting(name, excl="!", greeting="Hello "):
    return greeting + name + excl


print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))


def test(i, switch=True, dict1={2: 3, 4: 5, 6: 5}):
    if switch and isinstance(i, int) and i in dict1.keys():
        return dict1[i]
    return False

def checkingIfIn(str, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
        if direction:
            if str in d.keys():
                return True
        else:
            if str not in d.keys():
                return True
        return False

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('baseball')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('baseball', False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('wtf', True, {'wtf':8})

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse=True)

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(list(medals.keys()))

# Given the same dictionary, medals, now sort by the medal count. Save the three countries
# with the highest medal count to the list, top_three.
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
sorted_tuples = sorted(medals.items(), key=lambda item: item[1], reverse=True)
print(sorted_tuples)
top_three = [entry[0] for entry in sorted_tuples][0:3]
print(top_three)

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
sorted_tuples = sorted(groceries.items(), key=lambda item: item[1], reverse=True)
print(sorted_tuples)
most_needed = [entry[0] for entry in sorted_tuples]
print(most_needed)

