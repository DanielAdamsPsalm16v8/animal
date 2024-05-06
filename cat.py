from animal import Animal
class Cat(Animal):
    # attributes
    _whiskerLength = None
    _hasLongHair = None
    _y = None

    # constructors
    def __init__(self, speed, x, whiskerLength, hasLongHair, y):
        super().__init__(speed, x, noise = "meow", canClimb = True, legs=4)
        self.setWhiskerLength(whiskerLength)
        self.setHasLongHair(hasLongHair)
        self.setY(y)
    
    # accessors
    def getWhiskerLength(self):
        return self._whiskerLength
    
    def getHasLongHair(self):
        return self._hasLongHair
    
    def getY(self):
        return self._y
    
    # mutators
    def setWhiskerLength(self, newWhiskerLength):
        self._whiskerLength = newWhiskerLength
    
    def setHasLongHair(self, newHasLongHair):
        self._hasLongHair = newHasLongHair
    
    def setY(self, newY):
        self._y = newY
    
    # methods
    def climb(self):
        if self.getCanClimb():
            self.setY(self.getY() + self.getSpeed())

    def beStroked(self):
        __cuteness = 0
        if self.getHasLongHair():
            __cuteness += 10
        __cuteness -= self.getWhiskerLength()
        if __cuteness > 0:
            __strokeTime = __cuteness
            print(self.getNoise())
        else:
            __strokeTime = 0
        return __strokeTime
    
    # create a cat object
    def reproduce(self):
        ragdoll = Cat(10,0,10,True,0)
        return ragdoll
    
bobby = Cat(10,25,1000,True, 0)
speach = bobby.talk(5)
print(speach)


    

