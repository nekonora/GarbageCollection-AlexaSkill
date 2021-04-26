# DataModels

from enum import Enum

class GarbageType(Enum):
    paper = 0
    plastic = 1
    foliage = 2
    notReciclable = 3
    organic = 4
    business_paper = 5

    def description(self):
        if self.value == 0:
            return "Carta"
        elif self.value == 1:
            return "Plastica"
        elif self.value == 2:
            return "Verde"
        elif self.value == 3:
            return "Non riciclabile"
        elif self.value == 4:
            return "Umido"
        elif self.value == 5:
            return "Carta Attivitá"