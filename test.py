import random

rarities = ['common','uncommon','rare','epic','legendary']
weapons = ['pistol','shotgun','assault rifle','Sub-machine gun','Sniper','grenade launcher']

rarity = random.choices(rarities,weights=[35,25,10,5,1])
weapon = random.choices(weapons)

print(rarity,weapon)