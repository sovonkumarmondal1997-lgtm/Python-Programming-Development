
# INPUT
expense_1 = float(input("Enter first expense: "))
expense_2 = float(input("Enter second expense: "))
expense_3 = float(input("Enter third expense: "))
expense_4 = float(input("Enter fourth expense: "))

# PROCESS
total = expense_1 + expense_2 + expense_3 + expense_4

average = total / 4

# OUTPUT
print("Total spent:", total)
print("Average expense:", average)

if total > 100:
    print("Warning: total spending is high this period.")
