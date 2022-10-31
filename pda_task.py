from src import Guest, Song

playlist = [
    Song("With a Little Help from My Friends", "The Beatles"),
    Song("Lucy in the Sky with Diamonds", "The Beatles"),
]

guests = {
    Guest(name="Grace Hopper", wallet=50.0): playlist[0],
    Guest(name="Barbara Liskov", wallet=50.0): playlist[1],
}

def display_playlist(playlist):
    for idx, song in enumerate(playlist):
        print(f"  {idx+1}.  '{song.title}' by {song.artist}")

def display_guests(guests):
    for guest in guests.keys():
        print(f"  guest: {guest.name}")
        print(f"  favourite song: {guests[guest].title}")

print(f"Playlist:")
display_playlist(playlist)

print(f"\nGuests:")
display_guests(guests)