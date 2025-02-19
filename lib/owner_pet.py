class Pet:
    
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)

    def get_pet_type(self):
        return self._pet_type
    
    def set_pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception("Not a valid pet type.")
        else:
            self._pet_type = pet_type

    pet_type = property(get_pet_type, set_pet_type)

    
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return[pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("invalid pet type")
        else:
            self.owner = self

    