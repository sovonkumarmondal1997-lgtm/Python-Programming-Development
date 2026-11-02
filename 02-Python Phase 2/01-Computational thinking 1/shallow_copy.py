"""
Shallow Copy:
A shallow copy creates a new outer list, 
but the inner lists are shared between the original and copied lists.
"""

original_cart = [
    ["Milk", "Bread"],
    ["Eggs", "Butter"]
]

backup_cart = original_cart.copy()

# Modify the first nested list
backup_cart[0].append("Cheese")

print("Original:", original_cart)
print("Backup:", backup_cart)