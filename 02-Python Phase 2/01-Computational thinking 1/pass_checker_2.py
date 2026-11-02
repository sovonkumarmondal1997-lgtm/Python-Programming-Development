password_attempts = []

password_attempts.append("qwerty")
password_attempts.append("letmein")

print(password_attempts)

backup_attempts = password_attempts.copy()

backup_attempts.append("hunter2")

print(password_attempts)
print(backup_attempts)

password_attempts = ["reset"]

print(password_attempts)
print(backup_attempts)