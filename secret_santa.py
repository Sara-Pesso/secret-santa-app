# Secret Santa!


from math import *
import random

exclusions = {'Gene':['Kristen'],
'Tristan':['Tessa'],
'Perrin':['Beth'],
'Cullen':['Sara'],
'Liam':['Carolyn'],
'Owen':['Juliana'],
'Phineas':[],
'Theodora':[],
'Josiah':[],
'Kristen': ['Gene'], 
'Tessa': ['Tristan'], 
'Beth': ['Perrin'], 
'Sara': ['Cullen'], 
'Carolyn': ['Liam'], 
'Juliana': ['Owen']}


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