inv= {'gold':20,'rope':5}
dragon_list = ['gold','gr','gold','gold','ruby']
def add_to_inventory(inventory , addlist):
    for i in addlist:
        for k,v in inventory.items():
            if i :
                inventory[k]+=1
            else:
                inventory[i]=1
    return inventory
def display_inventory(inventory):
    print("Inventory:")
    item_totle = 0
    for k,v in inventory.items():
        print(str(v)+'\t'+k)
        item_totle +=v
    print('Total number of items:'+str(item_totle))
add_to_inventory(inv,dragon_list)
display_inventory(inv)
print(inv)