import random
import string

num1 = random.randint(1, 70923)
num2 = random.randint(1, 99332)

print(random.random())
print(random.randint(1, 35))
print(random.choice([num1, num2]))
print(random.choices([num1, num2], k=3))


def password_generator():
    return "".join(random.choices(str(num1) + string.ascii_lowercase + string.digits, k=13))


print(password_generator())
