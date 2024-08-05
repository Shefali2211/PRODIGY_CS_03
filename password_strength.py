import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Assess strength based on criteria
    if length_criteria and uppercase_criteria and lowercase_criteria and number_criteria and special_char_criteria:
        strength = "Very Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria) and number_criteria:
        strength = "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria):
        strength = "Moderate"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    return {
        "strength": strength,
        "feedback": feedback
    }

# Example usage
password = input("Enter your password: ")
result = assess_password_strength(password)
print(f"Password Strength: {result['strength']}")
if result['feedback']:
    print("Feedback:")
    for line in result['feedback']:
        print(f"- {line}")
else:
    print("Your password meets all strength criteria.")
