from route2d import Route2d
from strecke2d import Strecke2d
from punkt2d import Punkt2d

listeDerWegpunkte = [
    ["A", 1, 1],
    ["B", 2, 2],
    ["C", 3, 2]
]
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
route.info()
print("Länge der Route:", route.getLaenge())
