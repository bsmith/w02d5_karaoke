from src import Room, Guest, Song

room = Room(name="Blue", guest_limit=3)
song1 = Song("With a Little Help from My Friends", "The Beatles")
song2 = Song("Lucy in the Sky with Diamonds", "The Beatles")
guest1 = Guest(name="Grace Hopper", wallet=50.0)
guest2 = Guest(name="Barbara Liskov", wallet=50.0)

room.add_song_to_playlist(song1)
room.add_song_to_playlist(song2)

guest2.pay_fee(10)

room.add_guest(guest1)
room.add_guest(guest2)

print(f"Playlist in the {room.name} room:")
for idx, song in enumerate(room.playlist):
    print(f"  {idx+1}.  '{song.title}' by {song.artist}")

print(f"\nSinging tonight are:")
for guest in sorted(room.guests):
    print(f"  {guest.name}")