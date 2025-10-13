import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Length check
    if len(password) >= 8:
        strength += 1

    # Contains lowercase letters
    if re.search("[a-z]", password):
        strength += 1

    # Contains uppercase letters
    if re.search("[A-Z]", password):
        strength += 1

    # Contains digits
    if re.search("[0-9]", password):
        strength += 1

    # Contains special characters
    if re.search("[@#$%^&+=!]", password):
        strength += 1

    # Remarks based on strength score
    if strength == 5:
        remarks = "💪 Strong password!"
    elif 3 <= strength < 5:
        remarks = "🙂 Moderate password. You can make it stronger."
    else:
        remarks = "⚠️ Weak password. Try adding more variety."

    print(f"\nPassword Strength: {strength}/5")
    print(remarks)

# Main Function
def main():
    print("🔒 Welcome to the Password Strength Checker!\n")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
