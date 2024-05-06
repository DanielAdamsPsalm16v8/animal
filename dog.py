from animal import Animal

class Dog(Animal):
    # attributes
    _onLeash = None

    # constructors
    def __init__(self, speed, x, onLeash):
        super().__init__(speed, x, legs=4, noise="woof", canClimb = False)
        self.setOnLeash(onLeash)
    # accessors
    def getOnLeash(self):
        return self._onLeash
    # mutators
    def setOnLeash(self, newOnLeash):
        self._onLeash = newOnLeash
    # methods
    def fetch(self,pos):
        if self.getOnLeash():
            print("Can't fetch")
        else:
            distance = abs(self.getX() - pos)
            if distance < 10 * self.getSpeed():
                self.setX(pos)
                print("Fetch")
            else:
                print("Won't fetch")
    # create a dog object
    def reproduce(self):
        dalmation = Dog(10,0,True)
        return dalmation





