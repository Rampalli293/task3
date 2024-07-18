import random
import string

def generate_password(length=12):
    # Define character sets to use in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    # Ensure the password has at least one character from each set
    all_chars = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string
    return ''.join(password)

# Example usage:
if _name_ == "_main_":
    print(generate_password())
    print(generate_password(16))
    print(generate_password(20))
