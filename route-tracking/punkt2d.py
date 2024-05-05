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

  def setPositionY(self, positionY):
    self.positionY = positionY
    return
    
  def getPositionY(self):
    return self.positionY

  def comparePositionY(self, positionY):
    if self.positionY == positionY:
      return True

    return False

if __name__ == '__main__':
  p1 = Punkt2d("Startpunkt", 5, 10)
  print ("Name des Punkts:", p1.getBezeichnung())
  print ("X-Position des Punkts:", p1.getPositionX())
  print ("Y-Position des Punkts:", p1.getPositionY())

  p1.setBezeichnung("Endpunkt")
  p1.setPositionX(6)
  p1.setPositionY(11)
  print ("Neuer Name des Punkts:", p1.getBezeichnung())
  print ("Neue X-Position des Punkts:", p1.getPositionX())
  print ("Neue Y-Position des Punkts:", p1.getPositionY())

  print("prüfe Bezeichnung auf Vorhandensein ... ")
  if p1.hasBezeichnung():
    print("Bezeichnung ist vorhanden")

  for bezeichnung in ("Startpunkt", "Endpunkt"):
    print("teste Bezeichnung auf %s ... " % bezeichnung)
    if p1.compareBezeichnung(bezeichnung):
      print("Bezeichnung stimmt überein:", bezeichnung)   

  for position in (4, 5, 6):
    print("teste X-Position auf %i ... " % position)
    if p1.comparePositionX(position):
      print("X-Position stimmt überein:", position)   

  for position in (4, 9, 11):
    print("teste Y-Position auf %i ... " % position)
    if p1.comparePositionY(position):
      print("Y-Position stimmt überein:", position)   
