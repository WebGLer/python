# stuff = {'rope':1,
#          'torch':6,
#          'gold coin': 42,
#          'dagger': 1,
#          'arroe': 12,
#          }
# def display_inventory(inventory):
#     print("Inventory:")
#     item_totle = 0
#     for k,v in stuff.items():
#         print(str(v)+'\t'+k)
#         item_totle +=v
#     print('Total number of items:'+str(item_totle))
# display_inventory(stuff)

inv= {'gold':20,'rope':5}
dragon_list = ['gold','dragger','gold','gold','ruby']
def add_to_inventory(inventory , addlist):

    for i in addlist:
        for key in list(inventory.keys()):
            if i in inventory:
                #print(inventory[key])
                inventory[key]+=1
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


    # for i in addlist:
    #
    #     for key,value in inventory.items():
    #         if i == key:
    #             inventory[i]+=1
    #         inventory[]
    # print("count = "+str(count+value))
add_to_inventory(inv,dragon_list)
display_inventory(inv)