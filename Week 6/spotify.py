
songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "Numb",
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
]


def add_song():
    title = input("Enter song title: ")
    artist = input("Enter Artist: ")
    duration_m = int(input("Enter duration (minutes): "))
    duration_s = int(input("Enter duration (seconds): "))

    duration = duration_m * 60 + duration_s

    new_song = {
        "title": title,
        "artist": artist,
        "duration": duration,
        "plays": 0
    }

    songs.append(new_song)
    print("Song added successfully!")


def record_listen():
    song_title = input("Enter song title: ")
    found = False

    for song in songs:
        if song["title"].lower() == song_title.lower():
            song["plays"] += 1
            found = True
            print("Listen recorded!")
            break

    if found == False:
        print("Song not found!")


def generate_wrapped():
    total_songs = len(songs)
    total_plays = 0
    total_time = 0
    most_played = None

    for song in songs:
        total_plays += song["plays"]
        total_time += song["duration"] * song["plays"]

        if most_played is None or song["plays"] > most_played["plays"]:
            most_played = song

    total_minutes = total_time // 60

    print("\n========== YOUR SPOTIFY WRAPPED ==========")
    print("Total Songs:", total_songs)
    print("Total Plays:", total_plays)
    print("Total Listening Time:", total_minutes, "minutes")

    if total_songs == 0:
        print("No songs in your library!")
    elif total_plays == 0:
        print("No songs have been played yet!")
    else:
        print("Your Most Played Song:")
        print(most_played["title"], "-", most_played["artist"],
            "(", most_played["plays"], "plays)")

    print("==========================================")
