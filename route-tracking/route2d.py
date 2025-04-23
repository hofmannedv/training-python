# -----------------------------------------------------------
# demonstriert eine Klasse Route2d für ein Weg im 
# zweidimensionalen Raum
#o
# (C) 2024-2025 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from strecke2d import Strecke2d
from punkt2d import Punkt2d
import math

class Route2d:
  bezeichnung = ""
  strecken = []

  def __init__(self, bezeichnung, strecken):
    self.bezeichnung = bezeichnung
    self.strecken = strecken
    return

  def setBezeichnung(self, bezeichnung):
    self.bezeichnung = bezeichnung
    return
    
  def getBezeichnung(self):
    return self.bezeichnung
    
  def hasBezeichnung(self):
    return self.bezeichnung != ""
    
  def setStrecken(self, strecken):
    self.strecken = strecken
    return
    
  def getStrecken(self):
    return self.strecken
    
  def info(self):
    print("Name der Route:", self.getBezeichnung())

    for strecke in self.strecken:
        strecke.info()

    return

  def getLaenge(self):
    result = 0 #  default value
    for strecke in self.strecken:
        result = result + strecke.getLaenge()

    return result

if __name__ == '__main__':
  startpunkt1 = Punkt2d("A", 1, 1)
  endpunkt1 = Punkt2d("B", 2, 2)
  strecke1 = Strecke2d("Strecke 1", startpunkt1, endpunkt1)

  startpunkt2 = endpunkt1
  endpunkt2 = Punkt2d("C", 3, 2)
  strecke2 = Strecke2d("Strecke 2", startpunkt2, endpunkt2)
  
  streckenliste = [strecke1, strecke2]
  route = Route2d("Route 1", streckenliste)
  route.info()

  print("prüfe Bezeichnung auf Vorhandensein ... ")
  if route.hasBezeichnung():
    print("Bezeichnung ist vorhanden:", route.getBezeichnung())

  print("Länge der Route:", route.getLaenge())
