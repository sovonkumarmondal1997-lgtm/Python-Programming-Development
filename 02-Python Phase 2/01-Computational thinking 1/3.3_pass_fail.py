
# INPUT
score_1 = float(input("Enter first test score: "))
score_2 = float(input("Enter second test score: "))
score_3 = float(input("Enter third test score: "))

# PROCESS
total = score_1 + score_2 + score_3

average = total / 3

# OUTPUT
print("Average score:", average)

if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
