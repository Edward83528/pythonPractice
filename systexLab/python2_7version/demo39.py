import math
import random

print math.pi, math.sin(0), math.sin(math.pi / 2)
for i in range(0, 10):
    print random.randint(0, 20),
print

stores = ['7-11', 'Fami', "OK", "Hi-Life"]
for i in range(0, 10):
    print random.choice(stores)

cards = ['A', 'K', 'Q', 'J', '10', '9']
for i in range(0,10):
    random.shuffle(cards)
    print cards
