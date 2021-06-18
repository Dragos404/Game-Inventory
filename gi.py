def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""
    if inventory:
        for key in inventory:
            print(str(key) + ": " + str(inventory[key]))


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    added_items = make_it_a_list(added_items)
    for item in added_items:
        if item not in inventory:
            inventory[item] = 1
        else:
            inventory[item] = inventory[item] + 1
    return inventory


def remove_from_inventory(inventory, removed_items):
    """Remove from the inventory dictionary a list of items from removed_items."""
    removed_items = make_it_a_list(removed_items)
    for item in removed_items:
        if item in inventory:
            inventory[item] = inventory[item] - 1
            if inventory[item] < 1:
                del inventory[item]
    return inventory


def make_it_a_list(single_item_string):
    if type(single_item_string) is not list:
        single_item_string = [single_item_string]
    return single_item_string


def print_table(inventory, order=""):
    """
    Display the contents of the inventory in an ordered, well-organized table
    with each column right-aligned.
    """
    the_longest_key, the_longest_value = number_of_whitespaces(inventory)
    number_of_dashes = the_longest_key + len(" | ") + the_longest_value
    print_table_header(number_of_dashes, the_longest_key, the_longest_value)
    if order.lower() == "count,desc":
        inventory = set_values_in_order(inventory, True)
    elif order.lower() == "count,asc":
        inventory = set_values_in_order(inventory, False)
    for item in inventory:
        print(
            item.rjust(the_longest_key)
            + " | "
            + str(inventory[item]).rjust(the_longest_value)
        )
    print("-" * number_of_dashes)


def print_table_header(number_of_dashes, the_longest_key, the_longest_value):
    print("-" * number_of_dashes)
    print(
        "item name".rjust(the_longest_key)
        + " | "
        + "count".rjust(the_longest_value)
    )
    print("-" * number_of_dashes)


def number_of_whitespaces(inventory):
    the_longest_key = len("item name")
    the_longest_value = len("count")
    for key in inventory:
        if len(key) > the_longest_key:
            the_longest_key = len(key)
        if len(str(inventory[key])) > the_longest_value:
            the_longest_value = len(str(inventory[key]))
    return the_longest_key, the_longest_value


def set_values_in_order(inventory, do_reverse):
    return {
        key: value for key, value
        in sorted(inventory.items(), key=lambda x: x[1], reverse=do_reverse)
    }


def import_inventory(inventory, filename="import_inventory.csv"):
    """Import new inventory items from a CSV file."""
    items_to_add = []
    try:
        with open(filename, "r", encoding="utf-8") as new_items:
            for line in new_items:
                line = line.replace(", ", ",")
                line = line.split("\n")[0]
                items_to_add = items_to_add + line.split(",")
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
        return
    add_to_inventory(inventory, items_to_add)
    return inventory


def export_inventory(inventory, filename="export_inventory.csv"):
    """Export the inventory into a CSV file."""
    if inventory:
        write_it = ""
        for key, value in inventory.items():
            write_it += ("," + key) * value
        try:
            with open(filename, "w", encoding="utf-8") as save_inventory:
                save_inventory.write(write_it[1:])
        except PermissionError:
            print(f"You don't have permission creating file '{filename}'!")
            return


if __name__ == "__main__":
    inventory = {"alb": 1, "negru": 2, "albastru": 11, "galben": 18}
    add_to_inventory(
        inventory,
        ["alb", "negru", "gri", "rosu", "curcubeu", "ceva ", "culoare"]
    )
    remove_from_inventory(inventory, "ceva")
    print_table(inventory, "")
    import_inventory(inventory, "items.csv")
    print_table(inventory, "count,desc")
    export_inventory(inventory)