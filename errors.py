
class SpaceError(Exception):
    def __init__(self, message):
        self._message = "Two characters share the same space on the Board or a\
 character overrides terrain."