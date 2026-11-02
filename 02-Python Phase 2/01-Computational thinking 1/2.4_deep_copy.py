"""
Deep Copy:
A deep copy creates a completely independent copy, including the nested lists.
Python provides deepcopy() through its built-in copy module.
"""

import copy

original_cart = [
    ["Milk", "Bread"],
    ["Eggs", "Butter"]
]

backup_cart = copy.deepcopy(original_cart)

# Modify the first nested list
backup_cart[0].append("Cheese")

print("Original:", original_cart)
print("Backup:", backup_cart)