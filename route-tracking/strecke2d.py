from strecke1d import Strecke1d
from punkt2d import Punkt2d

class Strecke2d (Strecke1d):
  bezeichnung = ""
  wegpunkt1 = None
  wegpunkt2 = None

  def __init__(self, bezeichnung, wegpunkt1, wegpunkt2):
    self.bezeichnung = bezeichnung
    self.wegpunkt1 = wegpunkt1
    self.wegpunkt2 = wegpunkt2
    return

  def setBezeichnung(self, bezeichnung):
    self.bezeichnung = bezeichnung
    return
    
  def getBezeichnung(self):
    return self.bezeichnung
    
  def hasBezeichnung(self):
    return self.bezeichnung != ""
    
  def setWegpunkt1(self, wegpunkt):
    self.wegpunkt1 = wegpunkt
    return
    
  def getWegpunkt1(self):
    return self.wegpunkt1

  def setWegpunkt2(self, wegpunkt):
    self.wegpunkt2 = wegpunkt
    return
    
  def getWegpunkt2(self):
    return self.wegpunkt2
    
  def startswithWegpunkt(self, wegpunkt):
    if wegpunkt.getBezeichnung() == self.wegpunkt1.getBezeichnung():
      if wegpunkt.getPositionX() == self.wegpunkt1.getPositionX():
        if wegpunkt.getPositionY() == self.wegpunkt1.getPositionY():
          return True
    
    return False

  def endswithWegpunkt(self, wegpunkt):
    if wegpunkt.getBezeichnung() == self.wegpunkt2.getBezeichnung():
      if wegpunkt.getPositionX() == self.wegpunkt2.getPositionX():
        if wegpunkt.getPositionY() == self.wegpunkt2.getPositionY():
          return True

    return False
