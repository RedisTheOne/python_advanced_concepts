class Animal:
    def __init__(self, birthType="Unknown", apperance="Unknown", blooded="Unknown"):
        self.__birthType = birthType
        self.__apperance = apperance
        self.__blooded = blooded

    @property
    def birthType(self):
        return self.__birthType
    
    @birthType.setter
    def birthType(self, birthType):
        self.__birthType = birthType

    @property
    def apperance(self):
        return self.__apperance
    
    @apperance.setter
    def apperance(self, apperance):
        self.__apperance = apperance

    @property
    def blooded(self):
        return self.__blooded
    
    @blooded.setter
    def blooded(self, blooded):
        self.__blooded = blooded

    def __str__(self):
        return "A {} is {} it is {} and {}".format(type(self).__name__, self.birthType, self.apperance, self.blooded)
    
class Mammal(Animal):
    def __init__(self, birthType="Unknown", apperance="Unknown", blooded="Unknown", nurseYoung=True):
       super().__init__(birthType, apperance, blooded)
       self.__nurseYoung = nurseYoung

    @property
    def nurseYoung(self):
        return self.__nurseYoung

    @nurseYoung.setter 
    def nurseYoung(self, nurseYoung):
        self.__nurseYoung = nurseYoung

    def __str__(self):
        return super().__str__() + " and it is {} they nurse their young".format(self.nurseYoung)

class Reptile(Animal):
    def __init__(self, birthType="Unknown", apperance="Unknown", blooded="Unknown"):
        super().__init__(birthType, apperance, blooded)
    
    def sumAll(self, *args):
        sum = 0
        for a in args:
            sum += a
        return sum

def getBirthType(object):
    print("The {} is {}".format(type(object).__name__, object.birthType))

def main():
    reptile = Reptile(birthType="BIG")
    print("Sum: {}".format(reptile.sumAll(1, 2, 3, 4, 5)))
    getBirthType(reptile)

main()