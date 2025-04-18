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
distanz1 = berechneDistanz(listeDerWegpunkte1)
distanz2 = berechneDistanz(listeDerWegpunkte2)
print("Länge der Route 1:", distanz1)
print("Länge der Route 2:", distanz2)

kuerzesteRoute = 1
if distanz2 < distanz1:
    kuerzesteRoute = 2
print("die kürzeste Route ist Route", kuerzesteRoute)
