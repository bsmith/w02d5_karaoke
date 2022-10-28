class Room:
    def __init__(self, name, guest_limit):
        self.name = name
        self.guest_limit = guest_limit
        self.playlist = []
        self.guests = set()
    
    def add_song_to_playlist(self, song):
        self.playlist.append(song)

    def clear_playlist(self):
        self.playlist.clear()