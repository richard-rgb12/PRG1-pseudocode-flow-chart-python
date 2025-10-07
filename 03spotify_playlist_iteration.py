print("=== Spotify Playlist Mood Detector ===")
    
# Input
playlist_name = input("Enter your playlist name: ")
playlist_size = int(input("How many songs in your playlist? "))

# Initialise counters
happy_songs = 0
sad_songs = 0
energetic_songs = 0
chill_songs = 0
romantic_songs = 0

# Iteration through playlist
for i in range(playlist_size):
    print(f"\nSong {i+1}:")
    song_mood = input("Enter mood (happy/sad/energetic/chill/romantic): ").lower()
    
    if song_mood == "happy":
        happy_songs += 1
    elif song_mood == "sad":
        sad_songs += 1
    elif song_mood == "energetic":
        energetic_songs += 1
    elif song_mood == "romantic":
        romantic_songs += 1
    else:
        chill_songs += 1

# Calculate totals and percentages
total_songs = happy_songs + sad_songs + energetic_songs + chill_songs+ romantic_songs

# Output results
print(f"\nYour playlist '{playlist_name}' analysis:")
print(f"{happy_songs} happy songs ({(happy_songs/total_songs)*100:.1f}%)")
print(f"{sad_songs} sad songs ({(sad_songs/total_songs)*100:.1f}%)")
print(f"{energetic_songs} energetic songs ({(energetic_songs/total_songs)*100:.1f}%)")
print(f"{chill_songs} chill songs ({(chill_songs/total_songs)*100:.1f}%)")
print(f"{romantic_songs} romantic songs ({(romantic_songs/total_songs)*100:.1f}%)")

if happy_songs > sad_songs > energetic_songs > chill_songs > romantic_songs:
    print("The most common mood in your playlist is happy")
elif sad_songs > energetic_songs > chill_songs > romantic_songs:
    print("The most common mood in your playlist is sad")
elif energetic_songs > chill_songs > romantic_songs:
    print("The most common mood in your playlist is energetic")
elif chill_songs > romantic_songs:
    print("The most common mood in your playlist is chill")
else:
    print("The most common mood in your playlist is romantic")


if happy_songs > sad_songs:
    print("Overall mood: Upbeat! 😊")
else:
    print("Overall mood: Contemplative 🤔")