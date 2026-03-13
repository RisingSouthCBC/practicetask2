# ============================================================
# Practice Test — Question 1                        (6 marks)
# ============================================================
# A program converts temperatures between Celsius and
# Fahrenheit and checks whether a temperature indicates a
# fever. A temperature is considered a fever if it is
# 37.5°C or above.
# ============================================================

FEVER_THRESHOLD = 37.5


def to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# ------------------------------------------------------------
# Part (a) — 2 marks
# ------------------------------------------------------------
# The function below contains ONE syntax error and ONE logic
# error. Find and fix both errors.
#
# Syntax error: find the line with a syntax mistake and fix it.
# Logic error:  a temperature of exactly 37.5°C should be
#               considered a fever, but the current condition
#               does not include it.
# ------------------------------------------------------------

def is_fever(celsius):
    if celsius > FEVER_THRESHOLD
        return True
    return False


# ------------------------------------------------------------
# Part (b) — 2 marks
# ------------------------------------------------------------
# Add a function called validate_input below.
#
# The function must:
#   - receive celsius (a number) and scale (string) as parameters
#   - return True only if celsius is greater than -273.15
#     AND scale is either 'C' or 'F'
#   - return False otherwise
#
# Examples:
#   validate_input(36.6, 'C')   returns True
#   validate_input(36.6, 'F')   returns True
#   validate_input(-300, 'C')   returns False   # below absolute zero
#   validate_input(36.6, 'K')   returns False   # invalid scale
# ------------------------------------------------------------

# Write your validate_input function here:


# ------------------------------------------------------------
# Part (c) — 2 marks
# ------------------------------------------------------------
# Write a main() function.
#
# The function must:
#   - ask the user to enter a temperature in Celsius
#   - validate the input using validate_input with scale 'C'
#     — keep asking until valid
#   - call to_fahrenheit and print the converted temperature
#     rounded to 1 decimal place
#   - call is_fever and print whether the temperature is a
#     fever or not
#
# Example output:
#   Enter temperature in Celsius: -300
#   Invalid temperature. Please try again.
#   Enter temperature in Celsius: 38.2
#   38.2°C is 100.8°F
#   Fever detected.
# ------------------------------------------------------------

# Write your main() function here:


# Call main() to run your program:
