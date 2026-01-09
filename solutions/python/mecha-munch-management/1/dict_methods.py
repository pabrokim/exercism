"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    counter = {}
    

    for item in items_to_add:

        if item in counter:

            counter[item]+=1
        else:
            counter[item]=1

    for key, value in counter.items():

        if key in current_cart:
            current_cart[key]+=value
        else:
            current_cart[key]=value

    return current_cart
        


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    notes_dict = dict.fromkeys(notes, 1)
    
    return notes_dict


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: iterable -  with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
       
    for update in recipe_updates:
        
        updated_recipe = {update[0] : update[1]}
        
        ideas.update(updated_recipe)
        
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    cart_sorted = dict(sorted(cart.items()))

    return cart_sorted


def send_to_store(cart, aisle_mapping):
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    
    fulfilment = {}
    
    for item in cart:
        
        quantity = cart[item]

        aisle, refrigerated = aisle_mapping[item]
        
    
        fulfilment[item] = [quantity, aisle, refrigerated]
    
   
    sorted_fuilfilment = dict(sorted(fulfilment.items(), reverse=True))

    return sorted_fuilfilment

    

def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment_cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    updated_inventory = {}
    
    for item in store_inventory:
        updated_inventory[item] = store_inventory[item]

    for item in fulfillment_cart:

        item_quantity = fulfillment_cart[item][0]

        store_quantity, aisle, refrigerated = store_inventory[item]

        remaider_quantity = store_quantity - item_quantity

       
        if remaider_quantity <= 0:

            updated_inventory[item] = ['Out of Stock', aisle, refrigerated]

        else:
            updated_inventory[item] = [remaider_quantity, aisle, refrigerated] 
            
    return updated_inventory
