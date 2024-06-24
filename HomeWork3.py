class Building:

    def __init__(self, numberoffloors, buildingtype):

        self.numberoffloors = numberoffloors
        self.buildingtype = buildingtype

    def __eq__(self, other):
        return self.numberoffloors == other.numberoffloors and self.buildingtype == other.buildingtype


b1 = Building(numberoffloors=10, buildingtype="Таунхаус")
b2 = Building(numberoffloors=10, buildingtype="Офис")

print(b1 == b2)
