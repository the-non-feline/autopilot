#1/11/18 - got inheritance figured out, will start work on part definition
#1/12/18 - started work on partslist and locations
#1/15/18 - redid locations and tiles occupied based on part center, should make creating future algorithm easier

import base64
from math import pi
import math

#no purpose right now
def getRadiusFromHp(hp, HArmor: bool):
#WILL be used to determine where weapon set is, estimates circle needed to fulfill hp requirements
#coordinates on build plane are 10 apart
#therefore, HArmor has 32 hp per 400 area and VArmor has 5 hp per 400 area
    if HArmor == True:
        area = 12.5 * hp
    else:
        area = 80 * hp    
    radius = math.sqrt(area/pi)
    return int(radius)
    
"""
#subject to future deletion?
def armorCodeFromHp(hp):
#example of creating a ship code

    partsList = []
    radius = getRadiusFromHp(hp, True)
    partsText = ""
    currentHp = 0
    coordsOccupied= []

    armorCode = '{"parts":['+l+'],"name":"","aiRules":[]}'
    armorCode = armorCode.encode('utf-8')
    return "ship" + base64.b64encode(armorCode).decode('utf-8')
"""

class Part:
#superclass for all parts, has basic properties
    def __init__(self, name, mass, hp, cost, size):
        self.name = name
        self.mass = mass
        self.hp = hp
        self.cost = cost
        self.size = size
        self.XYPos = [None, None]
        
    def getPartText(self):
        return '{"pos":['+str(self.XYPos[0])+','+str(self.XYPos[1])+'],"type":"'+self.name+'","dir":0}'

#center of block, used for coordinate placing in ship code
    def getCoordsOccupied(self):
        returnCoords = []
        j = self.getXYPos()
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                scaledX = j[0] + x * 20 - self.size[0] * 10 + 10
                scaledY = j[1] + y * 20 - self.size[1] * 10 + 10
                returnCoords.append([scaledX, scaledY])
        print(returnCoords)
        
        return returnCoords
    
#getters for above variables
    def getName(self):
        return self.name
    def getMass(self):
        return self.mass
    def getHp(self):
        return self.hp
    def getCost(self):
        return self.cost
    def getSize(self):
        return self.size
    def getXYPos(self):
        return self.XYPos
        
class EPart(Part):
#inherits from part, super for reactors, battery, solar panel
    def __init__(self, eGen, eCap):
        self.eGen = eGen
        self.eCap = eCap
    #lets child classes call Part __init__
    def callPartInit(self, name, mass, hp, cost, size):
        super().__init__(name, mass, hp, cost, size)
        
#getters for variables specific to e parts
    def geteGen(self):
        return self.eGen
    def geteCap(self):
        return self.eCap
        
class Engine(Part):
    def __init__(self, thrust, eUse, turnSpeed):
        self.thrust = thrust
        self.eUse = eUse
        self.turnSpeed = turnSpeed
#lets child classes call Part __init__
    def callPartInit(self, name, mass, hp, cost, size):
        super().__init__(name, mass, hp, cost, size)
        return

#define parts
class HArmor1x1(Part):
    def __init__(self, XYPos: list):
        super().__init__("HArmor1x1", 10, 16, 2, [1,1])
        self.XYPos = XYPos
    
    def getXYPos(self):
        return self.XYPos
        
class VArmor1x1(Part):
    def __init__(self, XYPos: list):
        super().__init__(self, "VArmor1x1", 1.3, 5, 1, [1,1])
        self.XYPos = XYPos
        
    def getXYPos(self):
        return self.XYPos
        
class Battery1x1(EPart):
    def __init__(self, XYPos: list):
        super().__init__(0, 8000)
        super().callPartInit("Battery1x1", 10, 5, 10, [1,1])
        self.XYPos = XYPos
        
    def getXYPos(self):
        return self.XYPos
        
class Engine04(Engine):
    
#scout thruster
    def __init__(self, XYPos: list):
        super().__init__(130, 144, 57)
        super().callPartInit("Engine04", 10, 0, 20, [1,2])
        self.XYPos = XYPos
        
    def getXYPos(self):
        return self.XYPos        
        
        