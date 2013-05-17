class car(object):
    speed = 0
    maxbreakstr = 0.10
    position = 0
    accel = 0
    maxspeed = 100
    def __init__(self,speed=0, maxbreakstr=0.10, position=0):
        self.speed = speed
        self.maxbreakstr = maxbreakstr
        self.position = position
        pass
    def getSpeed(self):
        return self.speed
    