# Step 1: Define shopping basket
shopping_basket = [1000, 1500, 500, 2000]

# Step 2: Define spending budget
budget = 4000

# Step 3: Initialize total cost
total_cost = 0

# Step 4: Calculate total basket cost
for price in shopping_basket:
    total_cost = total_cost + price

# Step 5: Compare total cost with budget
if total_cost > budget:
    print("Budget Exceeded")
else:
    print("Within Budget")

# Step 6: Display total cost
print("Total Basket Cost:", total_cost)
