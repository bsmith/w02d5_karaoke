from src import KaraokeBar, Room, Guest, Song

def setup_karaoke_bar():
    room = Room(name="Blue", guest_limit=3)
    room.add_song_to_playlist(
        Song("With a Little Help from My Friends", "The Beatles"))
    room.add_song_to_playlist(
        Song("Lucy in the Sky with Diamonds", "The Beatles"))
    return KaraokeBar(rooms=[room], entrance_fee=25)

karaoke_bar = setup_karaoke_bar()

guests = [
    Guest(name="Grace Hopper", wallet=50.0),
    Guest(name="Barbara Liskov", wallet=50.0),
]

room = karaoke_bar.find_empty_room(len(guests))
karaoke_bar.check_in_guests(room, guests)

print(f"Playlist in the {room.name} room:")
for idx, song in enumerate(room.playlist):
    print(f"  {idx+1}.  '{song.title}' by {song.artist}")

print(f"\nSinging tonight are:")
for guest in sorted(room.guests, key=lambda g:g.name):
    print(f"  {guest.name}")

for room in karaoke_bar.rooms:
    karaoke_bar.check_out_guests(room)

print(f"\nTonight's takings were £{karaoke_bar.takings:.2f}")