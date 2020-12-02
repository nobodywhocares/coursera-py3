let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:]
print(last)


by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = " ".join([by, az, io, qy])
print(message)
message = by + " " + az + io + ", " + qy
print(message)

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

l = ['w', '7', 0, 9]
m = l[1:2]
print(type(m))

l = ['w', '7', 0, 9]
m = l[1]
print(type(m))

b = "My, what a lovely day"
x = b.split(',')
print(type(x))

b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
print(type(a))

my_str = "MICHIGAN"
for c in my_str:
    print(c)

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for elem in several_things:
    print(elem)
for elem in several_things:
    print(type(elem))

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
# Write your code here.
for str in str_list:
    print(len(str))

# DO NOT USE len() ... i.e. use accumulation pattern
original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for c in original_str:
    num_chars += 1
print(num_chars)

addition_str = "2+5+10+20"
sum_val = 0
for n in addition_str.split("+"):
    sum_val += int(n)
print(sum_val)

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_l = week_temps_f.split(",")
tot_temp = 0
for t in week_temps_l:
    tot_temp += float(t)
avg_temp = tot_temp / len(week_temps_l)
print(avg_temp)

# list containing 0 to 67
nums = range(68)

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []
for word in original_str.split(" "):
    num_words_list.append(len(word))
print(num_words_list)

lett = ''.ljust(7, 'b')
print(lett)

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
for rainfall in rainfall_mi.split(", "):
    if 3.0 < float(rainfall):
        num_rainy_months += 1
print(num_rainy_months)


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
# Write your code here.
same_letter_count = 0
for word in sentence.split(" "):
    if 1 == len(word) or word[0] == word[len(word)-1]:
        same_letter_count += 1
print(same_letter_count)

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0
for item in items:
    if "w" in item:
        acc_num += 1
print(acc_num)

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
num_a_or_e = 0
for word in sentence.split(" "):
    if "a" in word or "e" in word:
        num_a_or_e += 1
print(num_a_or_e)

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
num_vowels = 0
# Write your code here.
for ch in s:
    for vowel in vowels:
        if ch == vowel:
            num_vowels += 1
print(num_vowels)

# Both aliases b and z are used to manipulate the same list causing confusion
b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print(z)

# Strings are immutable so aliasing here will not cause issues
sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

lst = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto']
lst.remove('pluto')
first_three = lst[:3]

# Yes, the behavior of obj = obj + object_two is different than obj += object_two when obj is a list.
# The first version makes a new object entirely and reassigns to obj. The second version changes
# the original object so that the contents of object_two are added to the end of the first.
x = ["dogs", "cats", "birds", "reptiles"]
y = x
x += ['fish', 'horses']
y = y + ['sheep']
print(x)
print(y)

# Yes, when we make our own diagrams we want to keep the old information because sometimes
# other variables depend on them. It can get cluttered though if there is a lot of information.
sent = "The mall has excellent sales right now."
wrds = sent.split()
wrds[1] = 'store'
new_sent = " ".join(wrds)
print(sent)
print(wrds)
print(new_sent)


sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
sports.insert(2, "horseback riding")
print(sports)

trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'London', 'Melbourne']
trav_dest.remove('London')
print(trav_dest)
trav_dest = ['Beirut', 'Milan', 'Pittsburgh', 'Buenos Aires', 'Nairobi', 'Kathmandu', 'Osaka', 'Melbourne']
trav_dest.append('Guadalajara')
print(trav_dest)
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
winners.sort()
print(winners)
winners = ['Kazuo Ishiguro', 'Rainer Weiss', 'Youyou Tu', 'Malala Yousafzai', 'Alice Munro', 'Alvin E. Roth']
z_winners = sorted(winners, reverse=True)
print(z_winners)
winners.sort(reverse=True)
print(winners)

# create list from string
str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = [char for char in str1]
print(chars)
chars2 = list(str1) # shorthand for above
print(chars2)

# Count number of strings in list
lst = ['plan', 'answer', 5, 9.29, 'order, items', [4]]
s = 0
for item in lst:
    if type(item) == type("string"):
        s = s + 1


# seqmut-1-15: Which of these are good names for an accumulator variable? Select as many as apply.
# A. sum (reserved word)
# B. x
# X C. total
# X D. accum
# E. none of the above

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")
print("Value of 'a': ", a)

ael = "python!"
app = list(ael)
print(app)
ael = "python!"
app = []
for c in ael:
    app.append(c)
print(app)

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = [wrd+"ed" for wrd in wrds]
print(past_wrds)

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
for score in scores.split():
    if 90 == int(score) or 90 < int(score):
        a_scores += 1
print(a_scores) # 10

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ''
for word in org.split():
    if word not in stopwords:
        acro += word[0].capitalize()
print(acro)

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ''
sent_split = sent.split()
for word in sent_split:
    if word not in stopwords:
        acro += word[0].capitalize()+word[1].capitalize()
        if word != sent_split[-1]:
            acro += ". "
print(acro)

# A palindrome is a phrase that, if reversed, would read the exact same. Write code that checks if p_phrase
# is a palindrome by reversing it and then checking if the reversed version is equal to the original.
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.
p_phrase = "was it a car or a cat I saw"
r_phrase = p_phrase[::-1]
print(r_phrase)

# Provided is a list of data about a store’s inventory where each item in the list represents the name
# of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting,
# using the .format method (not string concatenation). For example, the first print statment should read
# The store has 12 shoes, each for 29.99 USD.
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
fmt = "The store has {} {}, each for {} USD"
for item in inventory:
    item_list = item.split(", ")
    print(fmt.format(item_list[1], item_list[0], item_list[2]))
