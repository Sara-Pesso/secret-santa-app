# Secret Santa!

from math import *
import random
import csv

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

with open("exclusions.csv", mode="r",newline="",encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader) # skip the header row
    for row in reader:
        giver = row[0]
        other_excluded = row[1]

        if giver not in exclusions:
            exclusions = exclusions.update({giver:[]})

        # String scrubbing
        other_excluded = other_excluded.replace(" ","") #remove spaces
        other_excluded = other_excluded.split(",")

        #Append new exclusions to exclusion dictionary
        for ex in other_excluded:
            if ex not in exclusions[giver]:
                exclusions[giver].append(ex)

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