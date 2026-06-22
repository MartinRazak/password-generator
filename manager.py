import random
import string


def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()"

    password = [random.choice(lowercase), random.choice(uppercase), random.choice(digits), random.choice(symbols)]

    all_chars = lowercase + uppercase + digits + symbols

    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)

    return "".join(password)

def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char in "!@#$%^&*?" for char in password):
        score += 1

    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"