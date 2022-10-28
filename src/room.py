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

    def is_empty(self):
        return len(self.guests) == 0

    def add_guest(self, guest):
        if guest.paid_fee:
            self.guests.add(guest)

    def clear_guests(self):
        self.guests.clear()

    def has_space(self, num_guests):
        return (self.guest_limit - len(self.guests)) >= num_guests