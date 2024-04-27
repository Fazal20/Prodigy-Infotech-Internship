def password_strength(password):
  """Evaluates the strength of a password.

  Args:
      password: The password to be assessed.

  Returns:
      A tuple containing:
          - Strength score (integer)
          - Feedback message (string)
  """
  score = 0
  feedback = ""

  # Check length
  if len(password) >= 12:
    score += 2
  elif len(password) >= 8:
    score += 1
  else:
    feedback += "Password is too short. "

  # Check character types
  has_upper = any(char.isupper() for char in password)
  has_lower = any(char.islower() for char in password)
  has_digit = any(char.isdigit() for char in password)
  has_symbol = any(char in "!@#$%^&*()" for char in password)

  if has_upper:
    score += 1
  else:
    feedback += "Missing uppercase letters. "
  if has_lower:
    score += 1
  else:
    feedback += "Missing lowercase letters. "
  if has_digit:
    score += 1
  else:
    feedback += "Missing digits. "
  if has_symbol:
    score += 1
  else:
    feedback += "Missing special characters. "

  # Strength rating based on score
  if score >= 5:
    strength = "Very Strong"
  elif score >= 4:
    strength = "Strong"
  elif score >= 3:
    strength = "Moderate"
  else:
    strength = "Weak"

  return score, f"Password Strength: {strength}\n{feedback}"

if __name__ == '__main__':
  while True:
    password = input("Enter your password: ")
    score, feedback = password_strength(password)
    print(feedback)
    print("-" * 30)