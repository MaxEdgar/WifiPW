import random
import string
import pyperclip

def generate_random_code(length=8):
    characters = string.ascii_letters + string.digits  # Letters (both lowercase and uppercase) + digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

# Generate 10 random codes and copy to clipboard
codes = [generate_random_code() for _ in range(50000)]
codes_string = '\n'.join(codes)  # Join the codes with newline for better readability

# Copy the generated codes to the clipboard
pyperclip.copy(codes_string)

print("Generated codes copied to clipboard:")
print(codes_string)
