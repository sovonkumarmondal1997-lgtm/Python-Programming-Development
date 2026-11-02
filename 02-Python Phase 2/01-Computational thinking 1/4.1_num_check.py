numbers = [4, -2, 0, 7, -9, 0, 1]

positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number > 0:
        positive_count = positive_count + 1
    elif number < 0:
        negative_count = negative_count + 1
    else:
        zero_count = zero_count + 1
        
print("Positive:", positive_count)
print("Negative:", negative_count)
print("Zero:", zero_count)
