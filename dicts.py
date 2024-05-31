
def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    list = []
    empty_dict = dict()
    
    for i in items:
        list.append(i)
    
    for a in list:
        if a in empty_dict:
            empty_dict[a] += 1
        else:
            empty_dict[a] = 1
    return empty_dict 


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    list = []
    
    for i in items:
        list.append(i)
    
    for a in list:
        if a in inventory:
            inventory[a] += 1
        else:
            inventory[a] = 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    list = []
    
    for i in items:
        list.append(i)
    
    for a in list:
        if a in inventory:
            inventory[a] -= 1
        if inventory[a] <= 0:
            inventory[a] = 0
    return inventory
    


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    list = []
    
    for i in inventory:
        list.append(i)
    
    for a in list:
        if a in item:
            del inventory[a]
    return inventory


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list = []
    list1= []

    for key, value in inventory.items():
        if value == 0:
            list.append(key)
    for i in list:
        del inventory[i]
        
    for key, value in inventory.items():
        list1.append((key, value))
        
    
    return list1

