class car(object):
    speed = 0
    position = 0
    accel = 0
    maxspeed = 100
    mode = "automatic"
    alloweddistance = 20
    nextCar = None
    speedAim = 0
    topAccel = 10
    def __init__(self,speed=0, position=0,maxspeed=100,mode="automatic"):
        self.speed = speed
        self.position = position
        self.maxspeed = maxspeed
        self.setMode(mode)
    
    def setMode(self,mode):
        if mode.lower() != "automatic" and mode.lower() != "override":
            print(mode.lower())
            print("Mode not set properly, assuming automatic mode")
            self.mode = "automatic"
        else:
            self.mode = mode.lower()
    
    def getSpeed(self):
        return self.speed
    
    def getAccel(self):
        return self.accel
    
    def getPosition(self):
        return self.position
    
    def getMaxSpeed(self):
        return self.maxspeed
    
    def getDistanceForward(self, othercar):
        if othercar == None:
            return 999
        else:
            distance = othercar.getPosition() - self.getPosition()
            return distance
    
    def getDistanceBehind(self, othercar):
        distance = self.getPosition() - othercar.getPosition()
        return distance
    
    def setNextCar(self,nextCar):
        self.nextCar = nextCar
    
    def setSpeed(self, speed):
        if speed != 0:
            self.speed = speed
        else:
            self.speed = self.getSpeed() + self.getAccel()
    
    def setAccel(self, accel):
        self.accel = accel
        
    def setSpeedAim(self,SpeedAim):
        self.speedAim = SpeedAim
    
    def doDrive(self):
        self.position = self.getPosition() + self.getSpeed()
        
    def doAccel(self):
        self.speed = self.speed + self.accel

    def act(self):
        if self.mode == "automatic":
            if self.getDistanceForward(self.nextCar) < self.alloweddistance:
                self.setAccel(-2)
            elif self.speed < self.speedAim:
                self.setAccel(2)
                self.doAccel()
                self.doDrive()
            elif self.speed == self.speedAim:
                self.setAccel(0)
                self.doDrive()
            pass
        elif self.mode == "override":
            self.doDrive()
            pass
        pass
        
if __name__ == "__main__":
    pass