import decimal
import os
import random
def find_decimals(value):
    return abs(decimal.Decimal(str(value)).as_tuple().exponent)
raritiesprenum = []
raritiesbase = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
for i in raritiesbase:
    raritiesprenum.extend([f"{i}-", f"{i}", f"{i}+", f"{i}++"])
rarities = [i for i in raritiesprenum]
for i in range(2, 8):
    rarities += [f"{rarity}({i})" for rarity in raritiesprenum]
print(rarities)
input()
def clr():
    os.system("cls")

chance = 1
current = 0
decay = 0.5
luck = 1

while True:
    print("\x1B[H")
    key = round(random.uniform(0, 1), find_decimals(chance))
    print(key)
    if key <= chance:
        clr()
        current+=1
        print("\r" + rarities[current])
        chance *= decay
        x = find_decimals(chance)
        print(key)
        print(f"{chance}")
