# Step 1: Define shopping basket
shopping_basket = [250, 450, 300, 500, 200]

# Step 2: Define the spending budget
budget = 1500

# Step 3 : Initialize the total cost
total_cost = 0

# Step 4: Calculate the busket cost
for price in shopping_basket:
    total_cost = total_cost + price

# Step 5: Compare total cost with budget
if total_cost > budget:
    print("Budget Exceeded")
else:
    print("Remaining Budget:", budget - total_cost)

# Step 6: Display total cost
print("Total Basket Cost:", total_cost)