__author__ = 'yura'

class Tank:
    def __init__(self,name,maxSpeed,powerOfMarch,caliber):
        self.name = name
        self.maxSpeed = maxSpeed
        self.powerOfMarch = powerOfMarch
        self.caliber = caliber

class Planes:
    def __init__(self,name,maxSpeed,flightAltitude,attackRadius):
        self.name = name
        self.maxSpeed = maxSpeed
        self.flightAltitude = flightAltitude
        self.attackRadius = attackRadius

listOfTanks = []
listOfPlanes = []
listOfPVO = []
listOfShips = []

listOfResults = []

wishTankMaxSpeed = 1
wishTankPowerOfMarch = 1
wishTankCaliber = 1

def purposefulSearchMethod(money):
    flag = False
    for tank in listOfTanks:
        if (tank.maxSpeed < wishTankMaxSpeed) or (tank.powerOfMarch < wishTankPowerOfMarch) or (tank.caliber < wishTankCaliber):
            flag = True
