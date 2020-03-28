#MultiLevel inheritance

class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "TonedWood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This guitar consists of {} strings and it is made of {} and it can play {} keys".format(self.numberOfStrings,self.typeOfWood,self.numberOfMajorKeys))

guitar = Guitar()