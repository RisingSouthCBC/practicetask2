# ============================================================
# Practice Test — Question 2                        (9 marks)
# ============================================================
# A swimming app tracks a swimmer's training session. The
# swimmer enters the number of laps completed and the pool
# length. The app calculates the total distance swum and
# checks whether they have met their training target.
# ============================================================

TARGET = 1000   # metres


# ------------------------------------------------------------
# Part (a) — 3 marks
# ------------------------------------------------------------
# Write a function called lap_distance.
#
# The function must:
#   - receive laps (integer) and pool_length (integer) as
#     parameters
#   - calculate and return the total distance swum in metres
#     (laps multiplied by pool_length)
#
# Examples:
#   lap_distance(20, 50)  returns 1000   # 20 laps in a 50m pool
#   lap_distance(10, 25)  returns  250   # 10 laps in a 25m pool
# ------------------------------------------------------------

# Write your lap_distance function here:


# ------------------------------------------------------------
# Part (b) — 3 marks
# ------------------------------------------------------------
# Write a function called target_met.
#
# The function must:
#   - receive distance (integer) and target (integer) as
#     parameters
#   - return True if distance is greater than or equal to target
#   - return False otherwise
#
# Examples:
#   target_met(1000, 1000)  returns True    # exactly met
#   target_met(750,  1000)  returns False   # not yet met
#   target_met(1200, 1000)  returns True    # exceeded
# ------------------------------------------------------------

# Write your target_met function here:


# ------------------------------------------------------------
# Part (c) — 3 marks
# ------------------------------------------------------------
# Write a main() function.
#
# The function must:
#   - ask the user to enter the number of laps — validate that
#     it is greater than 0, keep asking until valid
#   - ask the user to enter the pool length — validate that it
#     is either 25 or 50, keep asking until valid
#   - call lap_distance and print the total distance
#   - call target_met and print whether the TARGET was met
#   - use good programming practice — meaningful variable
#     names, comments, and use of the TARGET constant
#
# Example output:
#   Enter number of laps: 0
#   Laps must be greater than 0. Please try again.
#   Enter number of laps: 20
#   Enter pool length (25 or 50): 30
#   Pool length must be 25 or 50. Please try again.
#   Enter pool length (25 or 50): 50
#   Total distance: 1000 metres
#   Well done! You met your target of 1000 metres.
# ------------------------------------------------------------

# Write your main() function here:


# Call main() to run your program:
