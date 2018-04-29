def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]+=1
    return inventory
    pass
# your code goes here
def displayInventory(dic):
    count=0
    for k,v in dic.items():
        print(str(v)+' '+str(k))
        count+=v
    print('Toltal number of items:'+str(count))
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

