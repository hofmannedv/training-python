# -----------------------------------------------------------
# demonstriert die Berechnung der Weglänge für einen Weg im 
# zweidimensionalen Raum
#o
# (C) 2025 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from route2d import Route2d
from strecke2d import Strecke2d
from punkt2d import Punkt2d

def berechneDistanz(listeDerWegpunkte):
    distanz = 0

    listeDerStrecken = []

    position = 0
    while position < len(listeDerWegpunkte) - 1:
        startpunkt = Punkt2d(
            listeDerWegpunkte[position][0],
            listeDerWegpunkte[position][1],
            listeDerWegpunkte[position][2]
        ) 
        endpunkt = Punkt2d(
            listeDerWegpunkte[position + 1][0],
            listeDerWegpunkte[position + 1][1],
            listeDerWegpunkte[position + 1][2]
        )
        strecke = Strecke2d("Strecke %i" % (position + 1), startpunkt, endpunkt)
        listeDerStrecken.append(strecke)

        position = position + 1

    route = Route2d("Route 1", listeDerStrecken)
    distanz = route.getLaenge()
    return distanz

def ermittleWegpunkte(listeDerWegpunkte):
    wegpunkte = []
    for punkt in listeDerWegpunkte:
        name = punkt[0]
        wegpunkte.append(name)
    return wegpunkte

listeDerWegpunkte1 = [
    ["A", 1, 1],
    ["B", 2, 2],
    ["C", 3, 2]
]
listeDerWegpunkte2 = [
    ["A", 1, 1],
    ["D", 2, 3],
    ["C", 3, 2]
]

# Länge der Routen berechnen
distanz1 = berechneDistanz(listeDerWegpunkte1)
distanz2 = berechneDistanz(listeDerWegpunkte2)

# Wegpunkte der Routen ermitteln
wegpunkte1 = ermittleWegpunkte(listeDerWegpunkte1)
wegpunkte2 = ermittleWegpunkte(listeDerWegpunkte2)

# Ausgabe vorbereiten
routenverlauf1 = "(" + " - ".join(wegpunkte1) + ")"
routenverlauf2 = "(" + " - ".join(wegpunkte2) + ")"
print("Länge der Route 1 %s: %f" % (routenverlauf1, distanz1))
print("Länge der Route 2 %s: %f" % (routenverlauf2, distanz2))

# Kürzeste Route bestimmen (Annahme: Route 1)
kuerzesteRoute = 1
if distanz2 < distanz1:
    kuerzesteRoute = 2
print("die kürzeste Route ist Route", kuerzesteRoute)
