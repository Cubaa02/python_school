'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

# dictionary.py

# a) Create a nested dictionary
cars = {
    "car1": {
        "brand": "Toyota",
        "model": "Corolla",
        "year": 2010,
        "features": ["Air Conditioning", "Power Steering", "Cruise Control"],
        "owners": ("John Doe", "Jane Smith"),
        "service_dates": {"2020-01-10", "2021-02-15", "2022-03-20"}
    },
    "car2": {
        "brand": "Honda",
        "model": "Civic",
        "year": 2015,
        "features": ["Bluetooth", "Backup Camera", "Heated Seats"],
        "owners": ("Alice Johnson", "Bob Brown"),
        "service_dates": {"2019-05-10", "2020-06-15", "2021-07-20"}
    },
    "car3": {
        "brand": "Ford",
        "model": "Focus",
        "year": 2018,
        "features": ["Navigation System", "Sunroof", "Leather Seats"],
        "owners": ("Charlie Davis", "Dana White"),
        "service_dates": {"2020-08-10", "2021-09-15", "2022-10-20"}
    }
}

# b) Add a new element and remove an existing one
cars["car4"] = {
    "brand": "Chevrolet",
    "model": "Malibu",
    "year": 2020,
    "features": ["Remote Start", "Blind Spot Monitoring", "Apple CarPlay"],
    "owners": ("Eve Black", "Frank Green"),
    "service_dates": {"2021-11-10", "2022-12-15"}
}

# Remove car1
del cars["car1"]

# c) Print the contents of the dictionary in a formatted table
print("Slovník cars")
print("---------------------------------------------")
print("car             brand               year")
print("---------------------------------------------")
for car, details in cars.items():
    print(f"{car:<15} {details['brand']:<20} {details['year']}")
print("---------------------------------------------")
print(f"Počet záznamů: {len(cars)}")