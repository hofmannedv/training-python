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

def ermittleRouten(streckenliste, ausgangspunkt, zielpunkt):
    ergebnis = []
    weitereRouten = []

    if streckenliste != []:
        testliste = []
        for eintrag in streckenliste:
            startpunkt = eintrag[0]
            if startpunkt == ausgangspunkt:
                testliste.append(eintrag)

        print("Testliste:", testliste)

        bereinigteStreckenliste = []
        for teilstrecke in streckenliste:
            if teilstrecke not in testliste:
                bereinigteStreckenliste.append(teilstrecke)

        print("bereinigte Streckenliste:", bereinigteStreckenliste)

        for teilstrecke in testliste:
            startpunkt = teilstrecke[0]
            endpunkt = teilstrecke[1]
            if endpunkt != zielpunkt:
                print("suche nach Teilstrecken beginnend mit", endpunkt)
                weitereRouten = ermittleRouten(bereinigteStreckenliste, endpunkt, zielpunkt)
                print("gefunden: ", weitereRouten)

                if weitereRouten == []:
                    ergebnis.append([teilstrecke])  
                else:
                    ergebnis.append([teilstrecke] + weitereRouten)
            else:
                ergebnis.append(teilstrecke)

    return ergebnis

listeDerWegpunkte = [
    ["A", 1, 1],
    ["B", 2, 2],
    ["C", 3, 2],
    ["D", 2, 3],
    ["E", 4, 0],
    ["F", 5, 0]
]

listeDerTeilstrecken = [
    ["A", "B"],
    ["B", "C"],
    ["B", "D"],
    ["C", "E"],
    ["D", "E"],
    ["E", "F"]
]

listeDerRouten = []


# Länge der Routen berechnen
# distanz1 = berechneDistanz(listeDerWegpunkte1)
# distanz2 = berechneDistanz(listeDerWegpunkte2)

# Wegpunkte der Routen ermitteln
# wegpunkte1 = ermittleWegpunkte(listeDerWegpunkte1)
# wegpunkte2 = ermittleWegpunkte(listeDerWegpunkte2)

# Ausgabe vorbereiten
# routenverlauf1 = "(" + " - ".join(wegpunkte1) + ")"
# routenverlauf2 = "(" + " - ".join(wegpunkte2) + ")"
# print("Länge der Route 1 %s: %f" % (routenverlauf1, distanz1))
# print("Länge der Route 2 %s: %f" % (routenverlauf2, distanz2))

# Kürzeste Route bestimmen (Annahme: Route 1)
# kuerzesteRoute = 1
# if distanz2 < distanz1:
#     kuerzesteRoute = 2
# print("die kürzeste Route ist Route", kuerzesteRoute)
print(ermittleRouten(listeDerTeilstrecken, "A", "F"))
