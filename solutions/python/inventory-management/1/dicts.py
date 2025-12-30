"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    counts = {}
    
    for item in items:
        
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """

    counts = {}
    
    for item in items:
        
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
            
    for key, value in counts.items():
        
        if key in inventory:
            inventory[key] += value
        else:
            inventory[key] = value

    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    counts = {}
    
    for item in items:
        
        if item in counts:
            counts[item] += 1
            
        else: 
            counts[item] = 1
    for key, value in counts.items():
        if key in inventory:
            inventory[key] -= value
            if inventory[key] < 0:
                inventory[key] = 0
    return inventory
            
        
        

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """

def list_inventory(inventory):
    """Create a list containing only available (item_name, item_count > 0) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    list_items = []

    for key in inventory:
        
        if inventory[key] > 0:
            
            item = (key, inventory[key])

            list_items.append(item)
        
    return list_items
