# -----------------------------------------------------------
# demonstriert eine Klasse Strecke für eine Strecke im 
# zweidimensionalen Raum
#o
# (C) 2024-2025 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from punkt import Punkt

class Strecke:
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
    
  def compareBezeichnung(self, bezeichnung):
    return bezeichnung == self.bezeichnung

  def setWegpunkt1(self, wegpunkt):
    self.wegpunkt1 = wegpunkt
    return
    
  def getWegpunkt1(self):
    return self.wegpunkt1

  def hasWegpunkt1(self):
    return self.wegpunkt1 != None

  def hasWegpunkt2(self):
    return self.wegpunkt2 != None

  def setWegpunkt2(self, wegpunkt):
    self.wegpunkt2 = wegpunkt
    return
    
  def getWegpunkt2(self):
    return self.wegpunkt2
    
  def startswithWegpunkt(self, wegpunkt):
    if wegpunkt.getBezeichnung() == self.wegpunkt1.getBezeichnung():
      return True
    else:
      return False

  def endswithWegpunkt(self, wegpunkt):
    if wegpunkt.getBezeichnung() == self.wegpunkt2.getBezeichnung():
      return True
    else:
      return False

  def info(self):
    print("Name der Strecke:", self.getBezeichnung())
    wegpunkt1 = self.getWegpunkt1()
    if self.hasWegpunkt1():
      print("Von %s" % wegpunkt1.getBezeichnung())
    wegpunkt2 = self.getWegpunkt2()
    if self.hasWegpunkt2():
      print("Bis %s" % wegpunkt2.getBezeichnung())
    return

if __name__ == '__main__':
  startpunkt = Punkt("Startpunkt")
  endpunkt = Punkt("Endpunkt")
  abschnitt = Strecke("Strecke 1", startpunkt, endpunkt)

  abschnitt.info()

  print("prüfe Bezeichnung auf Vorhandensein ... ")
  if abschnitt.hasBezeichnung():
    print("Bezeichnung ist vorhanden")

  for bezeichnung in ("Hauptstrecke", "Nebenstrecke", "Strecke 1"):
    print("teste Bezeichnung auf %s ... " % bezeichnung)
    if abschnitt.compareBezeichnung(bezeichnung):
      print("Bezeichnung stimmt überein:", bezeichnung)
