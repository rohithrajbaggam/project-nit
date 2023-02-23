from enum import Enum 

class GenderEnumType(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHERS = "OTHERS"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]