import copy

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
listOfTanksGeneric = []
listOfPlanesGeneric = []
listOfPVOGeneric = []
listOfShipsGeneric = []
listOfBMPGeneric = []

listOfTanksGeneric.append(Tank('CHALLENGER', 56, 400, 120, 6000000))
listOfTanksGeneric.append(Tank('BULAT', 60, 600, 125, 287500))
listOfTanksGeneric.append(Tank('ABRAMS', 67, 465, 120, 6500000))
listOfTanksGeneric.append(Tank('LEOPARD', 65, 600, 105, 5000000))

listOfPlanesGeneric.append(Plane('TYPHOON', 2450, 19812, 1390, 27, 114000000))
listOfPlanesGeneric.append(Plane('RAFALE', 1900, 15240, 1110, 30, 124000000))
listOfPlanesGeneric.append(Plane('GRIPEN', 2200, 15240, 800, 27, 60000000))
listOfPlanesGeneric.append(Plane('F-18', 1915, 15240, 1065, 20, 60900000))
listOfPlanesGeneric.append(Plane('SU-35', 2500, 18000, 900, 30, 38000000))

listOfShipsGeneric.append(Ship('UOSP', 24, 41.182, 46, 1900, 720000000))
listOfShipsGeneric.append(Ship('TARAVA', 24, 40608, 43, 1900, 700000000))
listOfShipsGeneric.append(Ship('KARLOS-1', 21, 27.079, 30, 1200, 400000000))
listOfShipsGeneric.append(Ship('OUSHEN', 18, 22500, 18, 800, 650000000))
listOfShipsGeneric.append(Ship('MISTRAL', 19, 21300, 16, 900, 600000000))
listOfShipsGeneric.append(Ship('TOHTO', 22, 18800, 15, 700, 500000000))
listOfShipsGeneric.append(Ship('HUGO', 30, 18000, 11, 500, 490000000))

listOfPVOGeneric.append(PVO('IGLA', 34, 1500, 12, 1000000))
listOfPVOGeneric.append(PVO('PANCIR', 20, 1450, 15, 14670000))
listOfPVOGeneric.append(PVO('IGLA-C', 6, 1440, 3.5, 900000))
listOfPVOGeneric.append(PVO('EGIDA', 500, 30000, 250, 115000000))
listOfPVOGeneric.append(PVO('TOPOL-M', 11, 1000, 11, 25000000))

listOfBMPGeneric.append(BMP('Bradley', 65, 6, 70, 3160000))
listOfBMPGeneric.append(BMP('M113', 64, 11, 70, 1050000))
listOfBMPGeneric.append(BMP('BMP-1', 65, 8, 30, 40000))
listOfBMPGeneric.append(BMP('Warrior', 75, 7, 155, 2100000))


def purposefulSearchMethod(dictOfWishes):
    listOfAlternatives = []

    listOfTanks = copy.deepcopy(listOfTanksGeneric)
    listOfShips = copy.deepcopy(listOfShipsGeneric)
    listOfBMP = copy.deepcopy(listOfBMPGeneric)
    listOfPVO = copy.deepcopy(listOfPVOGeneric)
    listOfPlanes = copy.deepcopy(listOfPlanesGeneric)

    listOfLists = [listOfTanks, listOfShips, listOfBMP, listOfPVO, listOfPlanes]

    end = False
    while not end:

        dictOfResults = {'Tank': '', 'Plane': '', 'Ship': '', 'PVO': '', 'BMP': '', 'price': 0}
        sum = 0

        for tank in listOfTanks:
            if tank.flag:
                tank.flag = False
                if not (tank.maxSpeed < dictOfWishes['wishTankMaxSpeed'] or
                                tank.powerOfMarch < dictOfWishes['wishTankPowerOfMarch'] or
                                tank.caliber < dictOfWishes['wishTankCaliber']):
                    dictOfResults['Tank'] = tank.name
                    sum += tank.cost
                    break

        for plane in listOfPlanes:
            if plane.flag:
                plane.flag = False
                if not (plane.maxSpeed < dictOfWishes['wishPlaneMaxSpeed'] or
                                plane.flightAltitude < dictOfWishes['wishPlaneFlightAltitude'] or
                                plane.attackRadius < dictOfWishes['wishPlaneAttackRadius'] or
                                plane.calibre < dictOfWishes['wishPlaneCalibre']):
                    dictOfResults['Plane'] = plane.name
                    sum += plane.cost
                    break

        for ship in listOfShips:
            if ship.flag:
                ship.flag = False
                if not (ship.maxSpeed < dictOfWishes['wishShipMaxSpeed'] or
                                ship.carrying < dictOfWishes['wishShipCarrying'] or
                                ship.planesOnBoard < dictOfWishes['wishShipPlanesOnBoard'] or
                                ship.soldiers < dictOfWishes['wishShipSoldiers']):
                    dictOfResults['Ship'] = ship.name
                    sum += ship.cost
                    break

        for PVO in listOfPVO:
            if PVO.flag:
                PVO.flag = False
                if not (PVO.attackRadius < dictOfWishes['wishPVOAttackRadius'] or
                                PVO.warheadSpeed < dictOfWishes['wishPVOWarheadSpeed'] or
                                PVO.attackHeight < dictOfWishes['wishPVOAttackHeight']):
                    dictOfResults['PVO'] = PVO.name
                    sum += PVO.cost
                    break

        for BMP in listOfBMP:
            if BMP.flag:
                BMP.flag = False
                if not (BMP.maxSpeed < dictOfWishes['wishBMPMaxSpeed'] or
                                BMP.soldiers < dictOfWishes['wishBMPSoldiers'] or
                                BMP.armor < dictOfWishes['wishBMPArmor']):
                    dictOfResults['BMP'] = BMP.name
                    sum += BMP.cost
                    break

        dictOfResults['price'] = sum

        if len(dictOfResults['Tank']) > 0 and len(dictOfResults['Plane']) > 0 and \
                        len(dictOfResults['Ship']) > 0 and len(dictOfResults['PVO']) > 0 and \
                        len(dictOfResults['BMP']) > 0 and dictOfWishes['budget'] >= sum:
            listOfAlternatives.append(dictOfResults)

        for listOfTechType in listOfLists:
            flags_disjunction = False
            for techClass in listOfTechType:
                flags_disjunction = flags_disjunction or techClass.flag
            end = end or not flags_disjunction

    listOfAlternatives = sorted(listOfAlternatives, key=lambda k: k['price'])
    for i in range(len(listOfAlternatives)):
        listOfAlternatives[i]['id'] = i + 1

    return listOfAlternatives