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

  def comparePositionX(self, positionX):
    if self.positionX == positionX:
      return True

    return False

if __name__ == '__main__':
  p1 = Punkt1d("Startpunkt", 5)
  print ("Name des Punkts:", p1.getBezeichnung())
  print ("Position des Punkts:", p1.getPositionX())

  p1.setBezeichnung("Endpunkt")
  p1.setPositionX(6)
  print ("Neuer Name des Punkts:", p1.getBezeichnung())
  print ("Neue Position des Punkts:", p1.getPositionX())

  print("prüfe Bezeichnung auf Vorhandensein ... ")
  if p1.hasBezeichnung():
    print("Bezeichnung ist vorhanden")

  for bezeichnung in ("Startpunkt", "Endpunkt"):
    print("teste Bezeichnung auf %s ... " % bezeichnung)
    if p1.compareBezeichnung(bezeichnung):
      print("Bezeichnung stimmt überein:", bezeichnung)   

  for position in (4, 5, 6):
    print("teste Position auf %i ... " % position)
    if p1.comparePositionX(position):
      print("X-Position stimmt überein:", position)
