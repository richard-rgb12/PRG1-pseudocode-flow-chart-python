print("=== Gaming Achievement Checker ===")
    
# Input
player_score = int(input("Enter your player score: "))
time_played_hours = int(input("Enter hours played: "))
enemies_defeated = int(input("Enter enemies defeated: "))

if player_score < 0:
    while player_score < 0:
        print('There can not be negative player score')
        player_score = int(input("Enter your player score: "))
elif time_played_hours < 0:
    while time_played_hours < 0:
        print('There can not be negative time player hours')
        time_played_hours = int(input("Enter hours played: "))
elif enemies_defeated < 0:
    while enemies_defeated < 0:
        print('There can not be negative enemies defeated')
        enemies_defeated = int(input("Enter enemies defeated: "))


# Selection logic
if player_score >= 10000 and time_played_hours >= 50:
    achievement = "Master Player"
elif player_score >= 15000 and time_played_hours >= 100:
    achievement = "Legend"
elif enemies_defeated >= 1000:
    achievement = "Combat Expert"
elif time_played_hours >= 20:
    achievement = "Dedicated Gamer"
elif player_score >= 5000:
    achievement = "Rising Star"
else:
    achievement = "Newcomer"

# Output
print(f"\nCongratulations! You've earned: {achievement}")

if achievement == "Master Player":
    print("You've unlocked the secret bonus level!")