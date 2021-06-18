
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.


from os import write
import csv

def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    if inventory:
        for key in inventory:
            print(str(key) + ":" + str(inventory[key]))


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    for item in added_items:
        if item in inventory:
            inventory[item] = inventory[item] + 1
        else:
            inventory[item] = 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
        elif inventory[item] < 1:
            del inventory[item]
    return inventory


def print_table(inventory, order=''):  
    order = {"Item Name" : 'Count'}
    inventory = { 
        "Lorem Ipsum": "11",
        "Dolores Semet": "5"
    }
    print('------------------------')
    for key, value in order.items():
        print(key.rjust(15), '|', value)
        print('------------------------')
    for key, value in inventory.items():
        print(key.rjust(15), '|', value.rjust(5))
    print('------------------------')

def import_inventory(inventory, filename= 'test_inventory.csv'):
    """Import new inventory items from a CSV file."""
    items_to_add = []
    try:
        with open(filename, 'r', encoding='utf-8') as new_items:
            for line in new_items:
                line = line.replace(', ',',')
                line = line.split('\n')[0]
                items_to_add = items_to_add + line.split(',')
    except FileNotFoundError:
        print(f"File'{filename}' not found!")
        return
    add_to_inventory(inventory, items_to_add)
    return inventory


def export_inventory(inventory, filename='test_inventory.csv'):
    """Export the inventory into a CSV file."""
    if inventory:
        write_it = ""
        for key, value in inventory.items():
            write_it += ("," + key) * value
        try:
            with open(filename, 'w', encoding="utf-8") as save_inventory:
                save_inventory.write(write_it[1:])
        except PermissionError:
            print(f"You don't have permission creating file '{filename} '!")
            return

if __name__ == "__main__":
    inventory = {"white": 1, "green": 2, "blue": 11, "black": 18,}
    add_to_inventory(
         inventory,
         ["sound", "color", "purple", "something", "open", "try", "else"]
    )
    remove_from_inventory(inventory,"")
    print_table(inventory, "")
    import_inventory(inventory, "test_inventory.csv")
    print_table(inventory, "count,desc")
    export_inventory(inventory)