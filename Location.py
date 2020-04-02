

class Location(object):

    def __init__(self, name, description, items, north="", east="", south="", west="", up="",
                 down=""):
        """
        Creates an instance of a location in the game world.
        :param name: [str] the name of the location.
        :param description: [str] the description of the location.
        :param north: [str] the name of the location to the north.
        :param east: [str] the name of the location to the east.
        :param south: [str] the name of the location to the south.
        :param west: [str] the name of the location to the west.
        :param up: [str] the name of the location upwards.
        :param down: [str] the name of the location downwards.
        """
        self.name = name
        # A dictionary to store all of the locations instead of creating variables for each
        # direction.
        self.locations_dict = {}
        # The description of the location to be displayed when the location is visited.
        self.description = description
        # False if the player has not visited the area, True otherwise.
        self.visited = False
        # Any special items present in this location will be in a list here
        self.items = items

        # Initialize the locations dictionary.
        if north:
            self.locations_dict["north"] = north
        if east:
            self.locations_dict["east"] = east
        if south:
            self.locations_dict["south"] = south
        if west:
            self.locations_dict["west"] = west
        if up:
            self.locations_dict["up"] = up
        if down:
            self.locations_dict["down"] = down

    def get_location(self, direction):
        """
        Returns the location at the given direction.
        :param direction: [str] the direction of the next location.
        :return: [str] the name of the desired location.
        """
        if direction not in self.locations_dict:
            return ""
        return self.locations_dict[direction]

    def look(self):
        """
        Creates the display for the player when they visit this location.
        :return: [str] the display of the location.
        """
        self.visited = True

        return self.description

