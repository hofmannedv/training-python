# -----------------------------------------------------------
# demonstriert die Berechnung der Weglänge für einen Weg im 
# zweidimensionalen Raum
#o
# (C) 2025-2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from route2d import Route2d
from strecke2d import Strecke2d
from punkt2d import Punkt2d

def berechneDistanz(listeDerWegpunkte):
    """ berechne die Distanz einer Route anhand von Wegpunkten """
    distanz = 0

    listeDerStrecken = []

    position = 0
    while position < len(listeDerWegpunkte) - 1:
        startpunkt = listeDerWegpunkte[position]
        endpunkt = listeDerWegpunkte[position + 1]
        strecke = Strecke2d("Strecke %i" % (position + 1), startpunkt, endpunkt)
        listeDerStrecken.append(strecke)

        position = position + 1

    route = Route2d("Route 1", listeDerStrecken)
    distanz = route.getLaenge()
    return distanz

def ermittleWegpunkte(listeDerWegpunkte):
    """ berechne die Route anhand der Namen der Wegpunkte """
    wegpunkte = []
    for punkt in listeDerWegpunkte:
        name = punkt.getBezeichnung()
        wegpunkte.append(name)
    return wegpunkte

# definiere vier Wegpunkte A bis D
wegpunkt1 = Punkt2d("A", 1, 1)
wegpunkt2 = Punkt2d("B", 2, 2)
wegpunkt3 = Punkt2d("C", 3, 2)
wegpunkt4 = Punkt2d("D", 2, 3)

# definiere zwei Routen
route1 = [wegpunkt1, wegpunkt2, wegpunkt3]
route2 = [wegpunkt1, wegpunkt4, wegpunkt3]

# Länge der beiden Routen berechnen
distanz1 = berechneDistanz(route1)
distanz2 = berechneDistanz(route2)

# Wegpunkte der beiden Routen ermitteln
wegpunkte1 = ermittleWegpunkte(route1)
wegpunkte2 = ermittleWegpunkte(route2)

# Ausgabe vorbereiten
routenverlauf1 = "(" + " - ".join(wegpunkte1) + ")"
routenverlauf2 = "(" + " - ".join(wegpunkte2) + ")"
print("Länge der Route 1 %s: %f" % (routenverlauf1, distanz1))
print("Länge der Route 2 %s: %f" % (routenverlauf2, distanz2))

# Kürzeste Route bestimmen (Annahme: Route 1)
kuerzesteRoute = 1
if distanz2 < distanz1:
    kuerzesteRoute = 2
print("die kürzere Route ist Route", kuerzesteRoute)
