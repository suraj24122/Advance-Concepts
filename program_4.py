class animal:
    species = "dog"

    @classmethod
    def get_species(cls):
        return cls.species
    
print(animal.get_species())