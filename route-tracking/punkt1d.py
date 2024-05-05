from punkt import Punkt

class Punkt1d (Punkt):
  bezeichnung = ""
  positionX = 0

  def __init__(self, bezeichnung, position):
    self.bezeichnung = bezeichnung
    self.positionX = position
    return

  def setPositionX(self, positionX):
    self.positionX = positionX
    return
    
  def getPositionX(self):
    return self.positionX
    
