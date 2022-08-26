############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        """Initialize a melon."""

        self.pairings = []



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        for pair in pairing:
            self.pairings.append(pair)
        # self.pairings = self.pairings
        #print(self.pairings)



    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

    def __repr__(self):
        return f'Melon name is {self.name} & Melon code is {self.code} '


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk_melon = MelonType("musk",  1998, "green", True, True, "Muskmelon")
    musk_melon.add_pairing(["mint"])
    all_melon_types.append(musk_melon)

    casaba_melon = MelonType("cas", 2003, "orange", False, False, "Casaba",)

    casaba_melon.add_pairing(["strawberries"])
    all_melon_types.append(casaba_melon)


    crenshaw_melon = MelonType("cren",  1996, "green", True, False, "Crenshaw")
    musk_melon.add_pairing(["prosciutto"])
    all_melon_types.append(crenshaw_melon)

    yellow_watermelon = MelonType("yw",  2013, "yellow", True, True, "Yello Watermelon")
    yellow_watermelon.add_pairing(["ice cream"])
    all_melon_types.append(yellow_watermelon)

    return all_melon_types


melon_types = make_melon_types()
print(melon_types)

def print_pairing_info(melon_types):
    for melon in melon_types:
        print(melon.pairings)
    """Prints information about each melon type's pairings."""




def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest


############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest
