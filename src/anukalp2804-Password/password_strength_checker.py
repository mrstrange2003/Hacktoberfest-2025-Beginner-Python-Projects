import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # --- Length-based scoring ---
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password is too short (min 8 characters).")

    # --- Character type checks ---
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add numbers (0-9).")

    if re.search(r"[@#$%^&*()_+=!?.]", password):
        strength += 1
    else:
        feedback.append("Add special characters (@, #, $, etc.).")

    # --- Detect repetitive characters ---
    if re.search(r"(.)\1{2,}", password):
        feedback.append("Avoid using the same character repeatedly.")

    # --- Detect sequential patterns ---
    if re.search(r"(123|234|345|456|567|678|789|abc|abcd|qwerty|password)", password.lower()):
        feedback.append("Avoid common or sequential patterns (like 12345, abc, qwerty).")
        strength -= 1  # Penalize common patterns

    # --- Score-based remarks ---
    if strength >= 6:
        remarks = "💪 Very strong password!"
    elif 4 <= strength < 6:
        remarks = "🙂 Good password, but can be stronger."
    elif 2 <= strength < 4:
        remarks = "😐 Weak password. Try mixing more characters."
    else:
        remarks = "⚠️ Very weak password!"

    # --- Display results ---
    print(f"\nPassword Strength Score: {max(strength, 0)}/6")
    print("Remarks:", remarks)

    if feedback:
        print("\nSuggestions for improvement:")
        for f in feedback:
            print("-", f)

# --- Main Program ---
def main():
    print("🔒 Welcome to the Advanced Password Strength Checker!\n")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
