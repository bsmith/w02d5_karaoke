from . import Room, Guest

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

    def increase_takings(self, amount):
        self.takings += amount

    def check_in_guests(self, room: Room, guests: list[Guest]):
        # check they fit into the room
        if not room.has_space(len(guests)):
            return

        # relieve guests of money into our coffers
        for guest in guests:
            fee = self.entrance_fee
            if guest.can_afford_fee(fee):
                guest.pay_fee(fee)
                self.increase_takings(fee)

        # add guests to room
        for guest in guests:
            room.add_guest(guest)

    def check_out_guests(self, room: Room):
        room.clear_guests()
        # if the guests enjoyed themselves, maybe they'd like to leave a tip,
        # if they have money left!