class Animal:
    # attributes
    _speed = None
    _x = None
    _legs = None
    _noise = None
    _canClimb = None

    # constructors
    def __init__(self, speed, x, legs, noise, canClimb):
        self._speed = speed
        self._x = x
        self._legs = legs
        self._noise = noise
        self._canClimb = canClimb 
    

    # accessors

    def getSpeed(self):
        return self._speed
    
    def getX(self):
        return self._x
    
    def getLegs(self):
        return self._legs
    
    def getNoise(self):
        return self._noise
    
    def getCanClimb(self):
        return self._canClimb
    
    # mutators
    
    def setSpeed(self, new_speed):
        self._speed = new_speed

    def setX(self, new_x):
        self._x = new_x

    def setLegs(self, new_legs):
        self._legs = new_legs
    
    def setNoise(self, new_noise):
        self._noise = new_noise

    def setCanClimb(self, new_can_climb):
        self._canClimb = new_can_climb

    # methods
    def move(self, time):
        self._x += time * self._speed

    def talk(self, pos):
        distance = abs(pos - self._x)
        if distance > 100:
            return None
        elif distance > 10:
            return self.getNoise()
        else:
            return self.getNoise().upper() + len(self.getNoise()) * '!'
    
    
    
    # create an animal object
    def createAnimal(self):
        chicken = Animal(1.3, 0, 2,"Sqwark", False)
        return chicken
