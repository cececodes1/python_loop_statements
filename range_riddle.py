# Task 1: Write a program that prints off different moods for each day of the week.
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm".
# Using the range() function, loop through every day of the week and for each day,
# randomly select a mood from the list and print it. Ensure that your program includes 
#the use of the random module to select the mood.

import random
# Define moods
moods = ["Happy", "Sad", "Energetic", "Calm"]
# Define days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
# Loop through each day of the week
for day in range(7):
    # Select a random mood from the list
    mood = random.choice(moods)
    # Print the day and mood
    print(f"On {days[day]}, you were feeling {mood}.")



