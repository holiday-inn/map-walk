# navigation
# directions locations

# input prompt
# distinguish between moving, pick things up

# >based on what they type in, what needs to be done
import random

rarities = ['Common','Uncommon','Rare','Epic','Legendary']
values = [20,40,60,80,99]

rarity = random.choices(rarities,weights=(45,35,14,4,2))
print(rarity)

value = values[rarities.index(rarity)]

print(value)
choice = input(f"Would you like to pickup the {rarity} gun?")

def choice():

    while True:
        if choice == "Yes":
            return {rarity,value}
        
        elif choice == "No":
            return None
        
        else:
            print("That is not a valid input")
        
        break