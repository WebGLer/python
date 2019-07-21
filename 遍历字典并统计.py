stuff = {'rope':1,
         'torch':6,
         'gold coin': 42,
         'dagger': 1,
         'arroe': 12,
         }
def display_inventory(inventory):
    print("Inventory:")
    item_totle = 0
    for k,v in stuff.items():
        print(str(v)+'\t'+k)
        item_totle +=v
    print('Total number of items:'+str(item_totle))
display_inventory(stuff)