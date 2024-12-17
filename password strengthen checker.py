import re

# Function to check the strength of the password
def check_password_strength(password):
    # Initialize strength score
    strength = 0
    
    # Length check at least 8 characters
    if len(password) >= 8:
        strength += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        print("Password should include at least one lowercase letter.")
    
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        print("Password should include at least one uppercase letter.")
    
    # Check for digits
    if re.search(r"\d", password):
        strength += 1
    else:
        print("Password should include at least one number.")
    
    # Check for special characters
    if re.search(r"[!@#$%^&*()_+={}:;',.<>?/|`~\[\]\\-]", password):
        strength += 1
    else:
        print("Password should include at least one special character.")
    
    # Final strength evaluation
    if strength == 5:
        print("Your password is strong!")
    elif strength >= 3:
        print("Your password is moderate.")
    else:
        print("Your password is weak.")

# Get user input for the password
def main():
    password = input("Enter a password to check its strength: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()