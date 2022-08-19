from random import random


import random

capitals = {'United States' : 'Washington, D.C','Russia': 'Moscow','England': 'London','China': ' Beijing','Vietnam': 'Hanoi','Italy': 'Rome','Japan': 'Tokyo','Canada': 'Ottawa','Germany': 'Berlin','France': 'Paris', 'Finland': 'Helsinki', 'Sweden': 'Stockholm', 'Denmark': 'Copenhagen'}
score = 0
print("You have 5 questions to answer!")
for i in range(5):
    country = random.choice(list(capitals.keys()))
    answer = input(f"What is the capital of {country}? \nYour answer: ")
    if answer.lower() == capitals[country].lower():
        print(f"Correct! The capital of {country} is {capitals[country]}!") 
        score = score + 1
    else:
        print(f"Incorrect! The capital of {country} is {capitals[country]}!")
print(f"Your score: {score}")