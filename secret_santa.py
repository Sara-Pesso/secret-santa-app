# Secret Santa!


from math import *
import random

exclusions = {'Gene':['Kristen', 'Liam', 'Phineas', 'Tristan'],
'Tristan':['Tessa','Kristen','Carolyn'],
'Perrin':['Beth','Phineas','Gene'],
'Cullen':['Sara','Carolyn','Phineas'],
'Liam':['Carolyn','Perrin'],
'Owen':['Juliana','Tessa','Kristen'],
'Phineas':['Juliana','Theodora'],
'Theodora':['Owen','Juliana'],
'Josiah':['Cullen','Owen'],
'Kristen': ['Gene','Sara'], 
'Tessa': ['Tristan','Gene'], 
'Beth': ['Perrin','Tristan','Cullen'], 
'Sara': ['Cullen','Theodora','Liam'], 
'Carolyn': ['Liam','Beth'], 
'Juliana': ['Owen','Josiah']}


def secret_santa_generator(exclusions):
    names = [key for key, _ in exclusions.items()]
    n = len(names)

    while True:
        random_order = random.sample(range(0,n), n)
        pairings = {names[i]: names[random_order[i]] for i in range(0, n)}
        exclusions_check = True
        for giver, receiver in pairings.items():
            if giver == receiver or receiver in exclusions.get(giver):
                exclusions_check = False
                break

        if exclusions_check:
            pairings_str = []
            for key, value in pairings.items():
                pairings_str.append(f"{key} DREW {value}")
            return pairings_str

# santas_list = secret_santa_generator(exclusions)
# for val in santas_list:
#     print(val)