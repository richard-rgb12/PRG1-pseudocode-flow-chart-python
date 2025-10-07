videos = int(input("Enter the number of videos watched: "))
average_length = float(input("Enter the average length of the videos in minutes: "))

total_time = videos * average_length
total_days = total_time / 60 / 24

print(f"The total time taken to watch all the videos is: {total_time:.0f} minutes")
print(f"The equivalent number of days is: {total_days:.1f} days")