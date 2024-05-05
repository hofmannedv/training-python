from punkt1d import Punkt1d

class Punkt2d (Punkt1d):
  bezeichnung = ""
  positionX = 0
  positionY = 0

  def __init__(self, bezeichnung, positionX, positionY):
    self.bezeichnung = bezeichnung
    self.positionX = positionX
    self.positionY = positionY
    return

  def setPositionX(self, positionX):
    self.positionX = positionX
    return
    
  def getPositionX(self):
    return self.positionX
    
  def setPositionY(self, positionY):
    self.positionY = positionY
    return
    
  def getPositionY(self):
    return self.positionY
    
