__author__ = 'yura'


class Tank:
    def __init__(self, name, maxSpeed, powerOfMarch, caliber, cost):
        self.name = name
        self.maxSpeed = maxSpeed
        self.powerOfMarch = powerOfMarch
        self.caliber = caliber
        self.cost = cost
        self.flag = True


class Plane:
    def __init__(self, name, maxSpeed, flightAltitude, attackRadius, calibre, cost):
        self.name = name
        self.maxSpeed = maxSpeed
        self.flightAltitude = flightAltitude
        self.attackRadius = attackRadius
        self.calibre = calibre
        self.cost = cost
        self.flag = True


class Ship:
    def __init__(self, name, maxSpeed, carrying, planesOnBoard, soldiers, cost):
        self.name = name
        self.maxSpeed = maxSpeed
        self.carrying = carrying
        self.planesOnBoard = planesOnBoard
        self.soldiers = soldiers
        self.cost = cost
        self.flag = True


class PVO:
    def __init__(self, name, attackRadius, warheadSpeed, attackHeight, cost):
        self.name = name
        self.attackRadius = attackRadius
        self.warheadSpeed = warheadSpeed
        self.attackHeight = attackHeight
        self.cost = cost
        self.flag = True


class BMP:
    def __init__(self, name, maxSpeed, soldiers, armor, cost):
        self.name = name
        self.maxSpeed = maxSpeed
        self.soldiers = soldiers
        self.armor = armor
        self.cost = cost
        self.flag = True

# #########################################################Forming lists of TANKS,PLANES,SHIPS,PVO,BMP
listOfTanks = []
listOfPlanes = []
listOfPVO = []
listOfShips = []
listOfBMP = []

listOfTanks.append(Tank('CHALLENGER', 56, 400, 120, 6000000))
listOfTanks.append(Tank('BULAT', 60, 600, 125, 287500))
listOfTanks.append(Tank('ABRAMS', 67, 465, 120, 6500000))
listOfTanks.append(Tank('LEOPARD', 65, 600, 105, 5000000))

listOfPlanes.append(Plane('TYPHOON', 2450, 19812, 1390, 27, 114000000))
listOfPlanes.append(Plane('RAFALE', 1900, 15240, 1110, 30, 124000000))
listOfPlanes.append(Plane('GRIPEN', 2200, 15240, 800, 27, 60000000))
listOfPlanes.append(Plane('F-18', 1915, 15240, 1065, 20, 60900000))
listOfPlanes.append(Plane('SU-35', 2500, 18000, 900, 30, 38000000))

listOfShips.append(Ship('UOSP', 24, 41.182, 46, 1900, 720000000))
listOfShips.append(Ship('TARAVA', 24, 40608, 43, 1900, 700000000))
listOfShips.append(Ship('KARLOS-1', 21, 27.079, 30, 1200, 400000000))
listOfShips.append(Ship('OUSHEN', 18, 22500, 18, 800, 650000000))
listOfShips.append(Ship('MISTRAL', 19, 21300, 16, 900, 600000000))
listOfShips.append(Ship('TOHTO', 22, 18800, 15, 700, 500000000))
listOfShips.append(Ship('HUGO', 30, 18000, 11, 500, 490000000))

listOfPVO.append(PVO('IGLA', 34, 1500, 12, 1000000))
listOfPVO.append(PVO('PANCIR', 20, 1450, 15, 14670000))
listOfPVO.append(PVO('IGLA-C', 6, 1440, 3.5, 900000))
listOfPVO.append(PVO('EGIDA', 500, 30000, 250, 115000000))
listOfPVO.append(PVO('TOPOL-M', 11, 1000, 11, 25000000))

listOfBMP.append(BMP('Warrior', 75, 7, 155, 2100000))
listOfBMP.append(BMP('Bradley', 65, 6, 70, 3160000))
listOfBMP.append(BMP('M113', 64, 11, 70, 1050000))
listOfBMP.append(BMP('BMP-1', 65, 8, 30, 40000))



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


def purposefulSearchMethod(dictOfWishes):
    listOfAlternatives = []

    end = False
    while not end:

        dictOfResults = {'Tank': '', 'Plane': '', 'Ship': '', 'PVO': '', 'BMP': '' , 'price': 0}
        sum = 0

        for tank in listOfTanks:
            if tank.flag == True:
                if (tank.maxSpeed < dictOfWishes['wishTankMaxSpeed']) or (
                            tank.powerOfMarch < dictOfWishes['wishTankPowerOfMarch']) or (
                            tank.caliber < dictOfWishes['wishTankCaliber']):
                    tank.flag = False
                else:
                    dictOfResults['Tank'] = tank.name
                    sum += tank.cost
                    tank.flag = False
                    break

        for plane in listOfPlanes:
            if plane.flag == True:
                if (plane.maxSpeed < dictOfWishes['wishPlaneMaxSpeed']) or (
                            plane.flightAltitude < dictOfWishes['wishPlaneFlightAltitude']) or (
                            plane.attackRadius < dictOfWishes['wishPlaneAttackRadius']) or (
                            plane.calibre < dictOfWishes['wishPlaneCalibre']):
                    plane.flag = False
                else:
                    dictOfResults['Plane'] = plane.name
                    sum += plane.cost
                    plane.flag = False
                    break

        for ship in listOfShips:
            if ship.flag == True:
                if (ship.maxSpeed < dictOfWishes['wishShipMaxSpeed']) or (
                            ship.carrying < dictOfWishes['wishShipCarrying']) or (
                            ship.planesOnBoard < dictOfWishes['wishShipPlanesOnBoard']) or (
                            ship.soldiers < dictOfWishes['wishShipSoldiers']):
                    ship.flag = False
                else:
                    dictOfResults['Ship'] = ship.name
                    sum += ship.cost
                    ship.flag = False
                    break

        for PVO in listOfPVO:
            if PVO.flag == True:
                if (PVO.attackRadius < dictOfWishes['wishPVOAttackRadius']) or (
                            PVO.warheadSpeed < dictOfWishes['wishPVOWarheadSpeed']) or (
                            PVO.attackHeight < dictOfWishes['wishPVOAttackHeight']):
                    PVO.flag = False
                else:
                    dictOfResults['PVO'] = PVO.name
                    sum += PVO.cost

                    break

        for BMP in listOfBMP:
            if BMP.flag == True:
                if (BMP.maxSpeed < dictOfWishes['wishBMPMaxSpeed']) or (
                            BMP.soldiers < dictOfWishes['wishBMPSoldiers']) or (BMP.armor < dictOfWishes['wishBMPArmor']):
                    BMP.flag = False
                else:
                    dictOfResults['BMP'] = BMP.name
                    sum += BMP.cost
                    break

        if (len(dictOfResults['Tank']) > 0) and (len(dictOfResults['Plane']) > 0) and (
                    len(dictOfResults['Ship']) > 0) and (len(dictOfResults['PVO']) > 0) and (
                    len(dictOfResults['BMP']) > 0) and (dictOfWishes['budget'] >= sum):
            listOfAlternatives.append(dictOfResults)
            listOfAlternatives['price'] = sum

        if (listOfTanks[0].flag == False) and (listOfTanks[1].flag == False) and (listOfTanks[2].flag == False) and (
                    listOfTanks[3].flag == False):
            end = True
        if (listOfPlanes[0].flag == False) and (listOfPlanes[1].flag == False) and (listOfPlanes[2].flag == False) and (
                    listOfPlanes[3].flag == False) and (listOfPlanes[4].flag == False):
            end = True
        if (listOfShips[0].flag == False) and (listOfShips[1].flag == False) and (listOfShips[2].flag == False) and (
                    listOfShips[3].flag == False) and (listOfShips[4].flag == False) and (listOfShips[5].flag == False) and (
                    listOfShips[6].flag == False):
            end = True
        if (listOfPVO[0].flag == False) and (listOfPVO[1].flag == False) and (listOfPVO[2].flag == False) and (
                    listOfPVO[3].flag == False) and (listOfPVO[4].flag == False):
            end = True
        if (listOfBMP[0].flag == False) and (listOfBMP[1].flag == False) and (listOfBMP[2].flag == False) and (
                    listOfBMP[3].flag == False):
            end = True
    i = 0
    while i < listOfAlternatives.count():
        if listOfAlternatives[i]['price'] > (listOfAlternatives[i+1]['price'] - 1):
            a = listOfAlternatives[i]
            listOfAlternatives[i] = listOfAlternatives[i+1]
            listOfAlternatives[i+1] = a
    i = 0
    while i < listOfAlternatives.count():
        listOfAlternatives['ID'] = i+1
        i+=1

    return listOfAlternatives



















