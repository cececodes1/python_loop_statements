# Task 2:  Simulate a mood tracker that records your mood at three different 
# times of the day (morning, afternoon, evening) for each day of the week. 
#Use nested loops to implement this: the outer loop should iterate over the days,
# and the inner loop should iterate over the times of the day. For each time, 
#randomly select a mood from a predefined list and print it.
# Use the random module again to randomly select the mood.

# Define days
days = ["Monday","Tuesday","Wednesday","Thurday","Friday","Saturday","Sunday"]
# Define times
times = ["Morning", "Afternoon", "Evening"]
# Define moods
moods = ["Happy", "Sad", "Angry", "Excited", "Relaxed"]

import random

for day in days:
    for time in times:
        mood = random.choice(moods)
        print(f"On {day} {time}, you were feeling {mood}")    

                                                            