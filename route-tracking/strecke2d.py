from strecke1d import Strecke1d
from punkt2d import Punkt2d
import math

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

  def info(self):
    print("Name der Strecke:", self.getBezeichnung())
    wegpunkt1 = self.getWegpunkt1()
    if self.hasWegpunkt1():
      print("Von %s (%i,%i)" % (wegpunkt1.getBezeichnung(), wegpunkt1.getPositionX(), wegpunkt1.getPositionY()))
    wegpunkt2 = self.getWegpunkt2()
    if self.hasWegpunkt2():
      print("Von %s (%i,%i)" % (wegpunkt2.getBezeichnung(), wegpunkt2.getPositionX(), wegpunkt2.getPositionY()))
    return

  def getLaenge(self):
    result = 0 #  default value
    if self.hasWegpunkt1() and self.hasWegpunkt2():
      wegpunkt1 = self.getWegpunkt1()
      wegpunkt2 = self.getWegpunkt2()
      laengeX = wegpunkt2.getPositionX() - wegpunkt1.getPositionX()
      laengeY = wegpunkt2.getPositionY() - wegpunkt1.getPositionY()
      result = math.sqrt(math.pow(laengeX,2) + math.pow(laengeY,2))

    return result

if __name__ == '__main__':
  startpunkt = Punkt2d("Startpunkt", 1, 1)
  endpunkt = Punkt2d("Endpunkt", 2, 2)
  route = Strecke2d("Strecke 1", startpunkt, endpunkt)

  route.info()

  print("prüfe Bezeichnung auf Vorhandensein ... ")
  if route.hasBezeichnung():
    print("Bezeichnung ist vorhanden")

  for bezeichnung in ("Hauptstrecke", "Nebenstrecke", "Strecke 1"):
    print("teste Bezeichnung auf %s ... " % bezeichnung)
    if route.compareBezeichnung(bezeichnung):
      print("Bezeichnung stimmt überein:", bezeichnung)

  print("Länge der Strecke:", route.getLaenge())
