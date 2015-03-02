__author__ = 'yura'

class Tank:
    def __init__(self,name,maxSpeed,powerOfMarch,caliber):
        self.name = name
        self.maxSpeed = maxSpeed
        self.powerOfMarch = powerOfMarch
        self.caliber = caliber

class Plane:
    def __init__(self,name,maxSpeed,flightAltitude,attackRadius,calibre):
        self.name = name
        self.maxSpeed = maxSpeed
        self.flightAltitude = flightAltitude
        self.attackRadius = attackRadius
        self.calibre = calibre

class Ship:
    def __init__(self,name,maxSpeed,carrying,planesOnBoard,soldiers):
        self.name = name
        self.maxSpeed = maxSpeed
        self.carrying = carrying
        self.planesOnBoard = planesOnBoard
        self.soldiers = soldiers

class PVO:
    def __init__(self,name,attackRadius,warheadSpeed,attackHeight):
        self.name = name
        self.attackRadius = attackRadius
        self.warheadSpeed = warheadSpeed
        self.attackHeight = attackHeight


##########################################################Forming lists of TANKS,PLANES,SHIPS,PVO,WARCARS
listOfTanks = []
listOfPlanes = []
listOfPVO = []
listOfShips = []

listOfTanks.append(Tank('CHALLENGER',56,400,120))
listOfTanks.append(Tank('BULAT',60,600,125))
listOfTanks.append(Tank('ABRAMS',67,465,120))
listOfTanks.append(Tank('LEOPARD',65,600,105))

listOfPlanes.append(Plane('TYPHOON',2450,19812,1390,27))
listOfPlanes.append(Plane('RAFALE',1900,15240,1110,30))
listOfPlanes.append(Plane('GRIPEN',2200,15240,800,27))
listOfPlanes.append(Plane('F-18',1915,15240,1065,20))
listOfPlanes.append(Plane('SU-35',2500,18000,900,30))

listOfShips.append(Ship('UOSP',24,41.182,46,1900))
listOfShips.append(Ship('TARAVA',24,40608,43,1900))
listOfShips.append(Ship('KARLOS-1',21,27.079,30,1200))
listOfShips.append(Ship('OUSHEN',18,22500,18,800))
listOfShips.append(Ship('MISTRAL',19,21300,16,900))
listOfShips.append(Ship('TOHTO',22,18800,15,700))
listOfShips.append(Ship('HUGO',30,18000,11,500))

listOfPVO.append(PVO('IGLA',34,1500,12))
listOfPVO.append(PVO('PANCIR',20,1450,15))
listOfPVO.append(PVO('IGLA-C',6,1440,3.5))
listOfPVO.append(PVO('EGIDA',500,30000,250))
listOfPVO.append(PVO('TOPOL-M',11,1000,11))



#############################################################################WISHES
wishTankMaxSpeed = 1
wishTankPowerOfMarch = 1
wishTankCaliber = 1

wishPlaneMaxSpeed = 1
wishPlaneFlightAltitude = 1
wishPlaneAttackRadius = 1
wishPlaneCalibre = 1

wishShipMaxSpeed = 1
wishShipCarrying = 1
wishShipPlanesOnBoard = 1
wishShipSoldiers = 1

wishPVOAttackRadius = 1
wishPVOWarheadSpeed = 1
wishPVOAttackHeight = 1
#############################################################################


def purposefulSearchMethod(money):

    dictOfResults = {'Tank':'' , 'Plane':'' , 'Ship':'' , 'PVO':''}

    for tank in listOfTanks:
        if (tank.maxSpeed < wishTankMaxSpeed) or (tank.powerOfMarch < wishTankPowerOfMarch) or (tank.caliber < wishTankCaliber):
            listOfTanks.pop(0)
        else:
            dictOfResults['Tank'] = listOfTanks[0].name
            break

    for plane in listOfPlanes:
        if (plane.maxSpeed < wishPlaneMaxSpeed) or (plane.flightAltitude < wishPlaneFlightAltitude) or (plane.attackRadius < wishPlaneAttackRadius) or (plane.calibre < wishPlaneCalibre):
            listOfPlanes.pop(0)
        else:
            dictOfResults['Plane'] = listOfPlanes[0].name
            break

    for ship in listOfShips:
        if (ship.maxSpeed < wishShipMaxSpeed) or (ship.carrying < wishShipCarrying) or (ship.planesOnBoard < wishShipPlanesOnBoard) or (ship.soldiers < wishShipSoldiers):
            listOfShips.pop(0)
        else:
            dictOfResults['Ship'] = listOfShips[0].name
            break

    for PVO in listOfPVO:
        if (PVO.attackRadius < wishPVOAttackRadius) or (PVO.warheadSpeed < wishPVOWarheadSpeed) or (PVO.attackHeight < wishPVOAttackHeight):
            listOfTanks.pop(0)
        else:
            dictOfResults['PVO'] = listOfPVO[0].name
            break

    return dictOfResults



















