############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller, 
                 ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types(Melon_Type):
    """Returns a list of current melon types."""
    
    all_melon_types = []

    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange',
                     False, False)
    cas.add_pairing('strawberries')
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType('cren', "Crenshaw", 1996, 'green',
                     False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 1998, 'yellow',
                     False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    
    for melon in melon_types:
        
        print(f"{melon.name} pairs with \n {melon.pairings[0]}")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    code_lookup = {}

    for melon in melon_types:
        
        code_lookup[melon.code] = melon.name 
    
    print(code_lookup)
    return code_lookup
############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""
    # Needs __init__ and is_sellable methods
    def __init__(self, code, shape, color_rating, field, farmer):
        self.code = code
        self.shape = shape
        self.color_rating = color_rating
        self.field = field
        self.farmer = farmer

    def is_sellable(self):
        return(self.shape and self.color_rating > 5 and self.field != 3) 
    

def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_list = []

    for melon in melon_types:
        melon = Melon
        melon_list.append(melon)

    return melon_list # work in progress

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

make_melon_type_lookup(make_melon_types(MelonType))



