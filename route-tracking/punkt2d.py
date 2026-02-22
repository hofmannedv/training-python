# -----------------------------------------------------------
# demonstriert eine Klasse Punkt2d für einen Punkt im 
# zweidimensionalen Raum
#o
# (C) 2024-2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from punkt1d import Punkt1d

class Punkt2d (Punkt1d):
  bezeichnung = ""
  positionX = 0
  positionY = 0

  def __init__(self, bezeichnung, positionX, positionY):
    """ initialisiere das Objekt mit den übergebenen Werten """
    self.setBezeichnung(bezeichnung)
    self.setPositionX(positionX)
    self.setPositionY(positionY)
    return

  def setPositionY(self, positionY):
    """ setze die Y-Position des Punkts auf den übergebenen Wert """
    self.positionY = positionY
    return
    
  def getPositionY(self):
    """ gebe den gespeicherten Y-Wert des Punkts zurück """
    return self.positionY

  def comparePositionY(self, positionY):
    """ prüfe, ob der übergebene Wert mit dem gespeicherten Y-Wert 
        des Punktes übereinstimmt """
    if self.positionY == positionY:
      return True
    return False

  def info(self):
    """ gib Informationen zum Punkt aus -- Name sowie X- und Y-Position """
    print("Name des Punkts:", self.getBezeichnung())
    print("X-Position des Punkts:", self.getPositionX())
    print("Y-Position des Punkts:", self.getPositionY())
    return
    
if __name__ == '__main__':
  p1 = Punkt2d("Startpunkt", 5, 10)
  p1.info()

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
