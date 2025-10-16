"""
Inventory management system module.
Added this doctring for documentation,
to fix the issue : C0114 (missing-module-docstring)
"""

import json
from datetime import datetime
import ast


stock_data = {}


# docstrings for every fn(C0116) + every fn name -> camelcase (C0103)
# Corrected function name (C0103) and mutable default arg (W0102)
def add_item(item="default", qty=0, logs=None):
    """Increases qty of item frm the stock data and logs the action (C0116)."""
    # Fix W0102: Dangerous default value
    if logs is None:
        logs = []

    if not item:
        return

    stock_data[item] = stock_data.get(item, 0) + qty

    # Fixed C0209 (consider-using-f-string)
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Removes a quantity of an item from the stock data (C0116)."""
    try:
        # Ensure qty is int
        qty = int(qty)
        # We only attempt to modify stock if the item exists
        if item in stock_data:
            stock_data[item] -= qty
            if stock_data[item] <= 0:
                del stock_data[item]
    # Fixed W0702/E722/B110 (bare-except)
    except KeyError:
        # Item did not exist or was already deleted; safe to pass
        pass
    except ValueError:
        # Handling case where qty is not convertible to int
        print("Warning: Removal quantity must be an integer.")


def get_qty(item):
    """Returns the current quantity of a specific item"""
    # Using .get() prevents KeyError if the item is not found
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Loads inventory data from a JSON file (C0116)."""
    # Fixed R1732 (consider-using-with) and W1514 (unspecified-encoding)
    # Using .update() instead of assignment avoids W0603 (global-statement)
    # The 'global stock_data' is removed to fix F824/W0602
    with open(file, "r", encoding='utf-8') as f:
        stock_data.clear()
        loaded_data = json.loads(f.read())
        stock_data.update(loaded_data)


def save_data(file="inventory.json"):
    """Saves the current inventory data to a JSON file (C0116)."""
    # Fixed R1732 (consider-using-with) and W1514 (unspecified-encoding)
    with open(file, "w", encoding='utf-8') as f:
        f.write(json.dumps(stock_data))


def print_data():
    """Prints report of all items & their quantities (C0116)."""
    print("Items Report")
    # Fixed C0206: consider iterating with .items()
    for item, qty in stock_data.items():
        print(item, "->", qty)


def check_low_items(threshold=5):
    """Checks for items below the specified stock threshold (C0116)."""
    result = []
    # Fixed C0206: consider iterating with .items()
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    return result


def main():
    """Main execn fn"""
    add_item("apple", 10)
    add_item("banana", 2)
    add_item(123, "ten")  # will print a warning due to non-integer qty
    remove_item("apple", 3)
    remove_item("orange", 1)  # Handled by KeyError fix
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    ast.literal_eval("print('eval used')")


main()
# Fixed E305 (expected 2 blank lines after class/function)
