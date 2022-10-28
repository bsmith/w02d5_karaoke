class KaraokeBar:
    def __init__(self, rooms, entrance_fee):
        self.rooms = [*rooms]
        self.entrance_fee = entrance_fee
        self.takings = 0

    def find_empty_room(self, num_guests):
        for room in self.rooms:
            if room.has_space(num_guests):
                return room
        return None