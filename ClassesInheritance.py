import math

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

  def name(self):
    return self.firstname + " " + self.lastname

class Student(Person):
    pass # inherit all props from parent


class StudentGraduate(Student):
  def __init__(self, fname, lname, admn_year, grad_year):
    """
    :type admn_year: int
    :type grad_year: int
    """
    super().__init__(fname, lname)
    self.admission_year = admn_year
    self.graduation_year = grad_year

  def years_attended(self):
    return self.graduation_year - self.admission_year


class Rectangle:
    def __init__(self, len1, len2):
        self.short_side_length = len1
        self.long_side_length = len2

    def area(self):
        return self.short_side_length * self.long_side_length

    def perimiter(self):
        return 2 * (self.short_side_length + self.long_side_length)

class Circle:
    def __init__(self, rad):
        self.radius = rad

    def area(self):
        return math.pi * (self.radius ** 2)


class Vehicle:

    def __init__(self, max, unit):
        self.speed_max = max
        self.speed_units = unit

    def __str__(self):
        return type(self).__name__+" with the maximum speed of "+str(self.speed_max)+" "+self.speed_units

# 2.7 Car(Vehicle, object)
class Car(Vehicle):
    pass

# 2.7 Boat(Vehicle, object)
class Boat(Vehicle):

    def __init__(self, max):
        # 2.7 super(Boat, self)
        super().__init__(max, "knots")



me_undergraduate = Student("Noah N.", "O'Consequence")
me_graduate = StudentGraduate("Noah N.", "O'Consequence", 1993, 1999)
print("Undergrad: ", me_undergraduate.name())
print("Grad: ", me_graduate.name(), ", years attended: ", me_graduate.years_attended())

print("Rect Area: ", Rectangle(12.4, 28.7).area())
print("Circle Area: ", Circle(1234.56789).area())
print("Car: ", Car(151, "km/h"))
print("Boat: ", Boat(77))
print("dir(Boat): ", dir(Boat))


class Bike:

    def __init__(self, color, price):
        self.color = color
        self.price = price

testOne = Bike('blue', 89.99)
testTwo = Bike('purple', 25.0)


class AppleBasket:

    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        return f'A basket of {self.apple_quantity} {self.apple_color} apples.'

    def to_alt_str(self):
        return 'A basket of {} {} apples.'.format(
            self.apple_quantity, self.apple_color)


print(AppleBasket('red', 4))
print(AppleBasket('blue', 50))
print(AppleBasket('green', 57.5).to_alt_str())

class BankAccount:

    def __init__(self, name, amt):
        self.name = name
        self.amt = amt

    def __str__(self):
        return f'Your account, {self.name}, has {self.amt} dollars.'

    def to_alt_str(self):
        return 'Your account, {}, has {} dollars.'.format(
            self.name, self.amt)

t1 = BankAccount('Bob', 100)
print(t1)
print(t1.to_alt_str())


class Pokemon(object):
    attack = 12
    defense = 10
    health = 15
    p_type = "Normal"

    def __init__(self, name, level=5):
        self.name = name
        self.level = level

    def train(self):
        self.update()
        self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def attack_up(self):
        self.attack = self.attack + self.attack_boost
        return self.attack

    def defense_up(self):
        self.defense = self.defense + self.defense_boost
        return self.defense

    def health_up(self):
        self.health = self.health + self.health_boost
        return self.health

    def update(self):
        self.health_boost = 5
        self.attack_boost = 3
        self.defense_boost = 2
        self.evolve = 10

    def getAttackBoost(self):
        return self.attack_boost

    def __str__(self):
        self.update()
        return "Pokemon name: {}, Type: {}, Level: {}".format(self.name, self.p_type, self.level)


class Grass_Pokemon(Pokemon):
    attack = 15
    defense = 14
    health = 12
    p_type = "Grass"

    def __init__(self, name):
        super().__init__(name)

    def train(self):
        self.update()
        # self.attack_up()
        self.defense_up()
        self.health_up()
        self.level = self.level + 1
        if 10 <= self.level:
            self.attack_up()
        if self.level % self.evolve == 0:
            return self.level, "Evolved!"
        else:
            return self.level

    def update(self):
        self.health_boost = 6
        self.attack_boost = 2
        self.defense_boost = 3
        self.evolve = 12

    def moves(self):
        self.p_moves = ["razor leaf", "synthesis", "petal dance"]

    def action(self):
        return "{} knows a lot of different moves!".format(self.name)

    def opponent(self):
        if ('Grass' == self.p_type):
            return ('Fire', 'Water')
        if ('Ghost' == self.p_type):
            return ('Dark', 'Psychic')
        if ('Fire' == self.p_type):
            return ('Water', 'Grass')
        if ('Flying' == self.p_type):
            return ('Electric', 'Fighting')

class Ghost_Pokemon(Pokemon):
    p_type = "Ghost"

    def update(self):
        self.health_boost = 3
        self.attack_boost = 4
        self.defense_boost = 3

class Fire_Pokemon(Pokemon):
    p_type = "Fire"

class Flying_Pokemon(Pokemon):
    p_type = "Flying"


p1 = Grass_Pokemon('Belle')
print(p1.action())

p2 = Grass_Pokemon('Bulby')
p3 = Grass_Pokemon('Pika')
print(p2, ", Attack: ", p2.attack)
print(p3, ", Attack: ", p3.attack)
for i in range(10-p3.level):
    p3.train()
print(p2, ", Attack: ", p2.attack)
print(p3, ", Attack: ", p3.attack)

def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM

# rudimentary alternative using test module
# import test
# test.testEqual(mySum([]), 0)


# EXCEPTIONS
gold = {"US":46, "Fiji":1, "Great Britain":27, "Cuba":5, "Thailand":2, "China":26, "France":10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

for x in country:
    try:
        country_gold.append(gold[x])
    except Exception:
        country_gold.append("Did not get gold")

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49},
      {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7},
      {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89},
      {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except Exception:
        print('failed to find puppies')

print("Total number of puppies:", total)


numb = [6, 0, 36, 8, 2, 36, 0, 12, 60, 0, 45, 0, 3, 23]

remainder = []
for num in numb:
    try:
        remainder.append(36 % num)
    except Exception:
        remainder.append('Error')

lst = [2,4,10,42,12,0,4,7,21,4,83,8,5,6,8,234,5,6,523,42,34,0,234,1,435,465,56,7,3,43,23]

lst_three = []

for num in lst:
    try:
        if 3 % num == 0:
            lst_three.append(num)
    except Exception:
        print('remainder error')


full_lst = ["ab", 'cde', 'fgh', 'i', 'jkml', 'nop', 'qr', 's', 'tv', 'wxy', 'z']

attempt = []

for elem in full_lst:
    try:
        attempt.append(elem[1])
    except Exception:
        attempt.append('Error')

conts = [['Spain', 'France', 'Greece', 'Portugal', 'Romania', 'Germany'], ['USA', 'Mexico', 'Canada'], ['Japan', 'China', 'Korea', 'Vietnam', 'Cambodia'], ['Argentina', 'Chile', 'Brazil', 'Ecuador', 'Uruguay', 'Venezuela'], ['Australia'], ['Zimbabwe', 'Morocco', 'Kenya', 'Ethiopa', 'South Africa'], ['Antarctica']]

third_countries = []

for c in conts:
    try:
        third_countries.append(c[2])
    except Exception:
        third_countries.append('Continent does not have 3 countries')

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        print(ppl_play[x])
    except Exception:
        ppl_play[x] = 1

di = [{"Puppies": 17, 'Kittens': 9, "Birds": 23, 'Fish': 90, "Hamsters": 49}, {"Puppies": 23, "Birds": 29, "Fish": 20, "Mice": 20, "Snakes": 7}, {"Fish": 203, "Hamsters": 93, "Snakes": 25, "Kittens": 89}, {"Birds": 20, "Puppies": 90, "Snakes": 21, "Fish": 10, "Kittens": 67}]
total = 0
for diction in di:
    try:
        total = total + diction['Puppies']
    except Exception:
        diction['Puppies'] = 0

print("Total number of puppies:", total)


