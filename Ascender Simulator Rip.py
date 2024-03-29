import decimal
import os
import random
import math
from time import sleep as wait
def find_decimals(value):
    return abs(decimal.Decimal(str(value)).as_tuple().exponent)
CharmRars = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
raritiesprenum = []
raritiesbase = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Ultimate", "Super", "Alpha", "Extreme", "Ultra", "Omega", "Mega", "Hyper","Godly", "Unique", "Majestic","Toxin","Divine", "Exotic", "Eternal", "Devastational", "Planetary", "Unidentifiable", "Holy", "Vintage", "Supreme", "Omni"]
for i in raritiesbase:
    raritiesprenum.extend([f"{i}-", f"{i}", f"{i}+", f"{i}++"])
rarities = [i for i in raritiesprenum]
print(f"made list of {len(rarities)} items")
input("Press Enter to Continue\n")
for i in range(2, 8):
    rarities += [f"{rarity}({i})" for rarity in raritiesprenum]
def clr():
    os.system("cls")
print(f"made list of {len(rarities)} items")
input("Press enter to continue\n")
chance = 1
current = 0
decay = 0.45
gems = 0
luck = 1
lucklambda = 1/luck
auto = False
gemcheck = True
while True:
    if auto == True:
        pass
    else:
        input()
        pass
    gems += round(1.1**current, 0)
    if gemcheck == True:
        if gems >= 100:
            gems -= 100
            print("\n\n\nBought Auto for you ;)")
            auto = True
            gemcheck = False
    print("\x1B[H")
    key = round(random.uniform(0, 1), find_decimals(chance))
    print(f"Auto = {auto}   ")
    wait(0.001)
    print(f"Gems:{gems}                                   ")
    print(key)
    if key <= chance/lucklambda:
        clr()
        current+=1
        print("\r" + rarities[current])
        chance *= decay
        x = find_decimals(chance)
        print(f"Gems:{gems}")
        print(f"Auto = {auto}")
        print(key)
        print(chance)
