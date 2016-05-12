inventory = { 'gold' : 500,
              'pouch' : ['flint', 'twine', 'gemstone'],
              'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
              }
inventory['key'] = ['seashell', 'strange berry', 'lint']
print(inventory)
print(sorted(inventory))
for key in inventory.items():
    if key[0] == 'backpack':
        key[1].sort()
        key[1].remove('dagger')
        print(inventory)
    if key [0] == 'gold':
        inventory[key[0]] = key[1] + 50
        print(inventory)
        
    

##inventory.remove['backpack'] = 'dagger'
##print(inventory)
