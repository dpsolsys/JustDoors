stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}


def display_inventory(inventory):
    print 'Inventory:'
    item_total = 0
    for k, v in inventory.items():
        print str(v) + ' ' + k
        item_total += v
    print "Total number of items: %s" % str(item_total)

display_inventory(stuff)


clothes = {'Charlie': {'shirts': 10, 'jeans': 2, 'socks': 30},
           'Kelly': {'dress': 5, 'shorts': 5, 'shoes': 10, 'socks': 20}}


def display_clothes(inventory, item):
    print 'Clothes:'
    for k, v in inventory.items():
        print k + ' ' + item + '' + str(v.get(item, 0))


display_clothes(clothes, 'socks')

