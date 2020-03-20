"""
This file contains multiple dictionaries of constants to be used by the program. This ensures that
values only have to be changed in one location, as opposed to many, and the code is still easily
readable.
"""

# ~~~ WEAPONS ~~~
# {weapon name: (max damage, stat bonus)}
WEAPONS = {"axe": (8, "str"), "dagger": (4, "dex"), "hammer": (6, "str"), "longbow": (10, "dex"),
           "sword": (8, "dex")}


# ~~~ POTIONS ~~~
# {potion type: max heal}
POTIONS = {"minor": 6, "major": 12}
