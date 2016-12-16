#controls an Inventory of the player for a fantasy game

inventory = {'gold coin': 42, 'arrow(s)': 12, 'rope': 1,
             'torch': 6, 'dagger': 1}
drops = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print()
    print('Total number of items: ' + str(item_total))
    print()

def addToInventory(drops, inventory):
    print('Congratulations on all that loot! Adding to inventory...')
    for s in drops:
        inventory[s] = (inventory.get(s, 0) + 1)
    print('Done! Enjoy the loot.')
    print()

displayInventory(inventory)
addToInventory(drops, inventory)
displayInventory(inventory)
