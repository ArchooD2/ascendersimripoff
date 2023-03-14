import random
import decimal
import os
def clr():
    os.system("cls")
def find_decimals(value):
    return (abs(decimal.Decimal(str(value)).as_tuple().exponent))
raritiesbase = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
rarities = []
current = 0
for i in raritiesbase:
    rarities.append(i + "-")
    rarities.append(i)
    rarities.append(i + "+")
    rarities.append(i + "++")
print(rarities[current])
chance = .9**current
while True:
    print("\x1B[H")
    key = round(random.uniform(1, chance), find_decimals(chance))
    print(key)
    if key == chance:
        clr()
        current+=1
        chance = .5**current
        print("\r" + rarities[current])
        print(key)
        print(chance)