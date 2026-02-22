# -----------------------------------------------------------
# demonstriert eine Klasse Punkt1d für einen Punkt im 
# eindimensionalen Raum
#o
# (C) 2024-2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from punkt import Punkt

class Punkt1d (Punkt):
  bezeichnung = ""
  positionX = 0

  def __init__(self, bezeichnung, positionX):
    """ initialisiere das Objekt mit den übergebenen Werten """
    self.setBezeichnung(bezeichnung)
    self.setPositionX(positionX)
    return

  def setPositionX(self, positionX):
    """ setze die Position des Punkts x auf den übergebenen Wert """
    self.positionX = positionX
    return
    
  def getPositionX(self):
    """ gebe den gespeicherten Wert des Punkts zurück """
    return self.positionX

  def comparePositionX(self, positionX):
    """ prüfe, ob der übergebene Wert mit dem gespeicherten Wert 
        des Punktes übereinstimmt """
    if self.positionX == positionX:
      return True

    return False

  def compareBezeichnung(self, bezeichnung):
    """ prüfe, ob die übergebene Bezeichnung mit der gespeicherten 
        Bezeichnung des Punktes übereinstimmt """
    if self.bezeichnung == bezeichnung:
      return True

    return False

  def info(self):
    """ gib Informationen zum Punkt aus -- Name und Position """
    print("Name des Punkts:", self.getBezeichnung())
    print("Position des Punkts:", self.getPositionX())
    return

if __name__ == '__main__':
  p1 = Punkt1d("Startpunkt", 5)
  p1.info()

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
      print("Position stimmt überein:", position)
