import random
letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

print("🔐 Welcome to the PyPassword Generator!")

nr_letters = int(input("👉 How many letters would you like in your password? "))
nr_symbols = int(input("👉 How many symbols would you like? "))
nr_numbers = int(input("👉 How many numbers would you like? "))

password_chars = (
    [random.choice(letters) for _ in range(nr_letters)] +
    [random.choice(symbols) for _ in range(nr_symbols)] +
    [random.choice(numbers) for _ in range(nr_numbers)]
)

random.shuffle(password_chars)
password = ''.join(password_chars)
length = len(password)
if length < 6:
    strength = "Weak"
elif length < 10:
    strength = "Moderate"
else:
    strength = "Strong"
print(f"\n✅ Your generated password is: {password}")
print(f"🔒 Password Strength: {strength}")

