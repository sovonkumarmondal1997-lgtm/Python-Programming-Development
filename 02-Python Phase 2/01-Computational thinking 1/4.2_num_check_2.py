def is_password_long_enough(password):
    return len(password) >= 8

def count_signs(numbers):
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
    return positive_count, negative_count, zero_count

passwords_to_check = ["hunter2", "correcthorsebatterystaple", "abc"]
for password in passwords_to_check:
    if is_password_long_enough(password):
        print(password, "-> OK")
    else:
        print(password, "-> too short")

positives, negatives, zeros = count_signs([4, -2, 0, 7, -9, 0, 1])
print("Positive:", positives, "Negative:", negatives, "Zero:", zeros)
