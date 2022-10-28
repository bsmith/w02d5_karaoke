class Room:
    def __init__(self, name, guest_limit):
        self.name = name
        self.guest_limit = guest_limit
        self.playlist = []
        self.guests = set()