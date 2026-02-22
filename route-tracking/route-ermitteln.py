# -----------------------------------------------------------
# demonstriert die Ermittlung einer Route in einem Graphen im
# zweidimensionalen Raum
#
# work in progress
# 
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

    distanz = 0

def ermittleWegpunkte(listeDerWegpunkte):
    """ berechne die Route anhand der Namen der Wegpunkte """
    wegpunkte = []
    for punkt in listeDerWegpunkte:
        name = punkt.getBezeichnung()
        wegpunkte.append(name)
    return wegpunkte

def ermittleGraphstruktur(streckenliste, ausgangspunkt, zielpunkt):
    """ ermittle eine Graphstruktur zwischen Start- und Zielpunkt """
    ergebnis = []
    weitereRouten = []

    if streckenliste != []:
        testliste = []
        for eintrag in streckenliste:
            startpunkt = eintrag.getWegpunkt1().getBezeichnung()
            if startpunkt == ausgangspunkt:
                testliste.append(eintrag)

        print("Testliste:", testliste)

        bereinigteStreckenliste = []
        for teilstrecke in streckenliste:
            if teilstrecke not in testliste:
                bereinigteStreckenliste.append(teilstrecke)

        print("bereinigte Streckenliste:", bereinigteStreckenliste)

        for teilstrecke in testliste:
            #startpunkt = teilstrecke[0]
            endpunkt = teilstrecke.getWegpunkt2().getBezeichnung()
            if endpunkt == zielpunkt:
                ergebnis.append(teilstrecke)
                break
            else:
                print("suche nach Teilstrecken beginnend mit", endpunkt)
                weitereRouten = ermittleGraphstruktur(bereinigteStreckenliste, endpunkt, zielpunkt)
                print("gefunden: ", weitereRouten)

                if weitereRouten:
                    zwischenergebnis = [teilstrecke]

                    if len(weitereRouten) == 1:
                        zwischenergebnis.append(weitereRouten[0])
                    else:
                        zwischenergebnis.append(weitereRouten)
                    ergebnis.append(zwischenergebnis)

    return ergebnis

def ermittleRouten(graphstruktur):
    print("aufgerufen mit Graphstruktur:", graphstruktur)
    # print("aufgerufen mit Streckenliste:", streckenliste)
    ergebnis = []

    print("prüfe Graphstruktur:", graphstruktur)
    if isinstance(graphstruktur, Strecke2d):
        ergebnis.append(graphstruktur)
    else:
        for eintrag in graphstruktur:
            print("prüfe Eintrag", eintrag)
            if isinstance(eintrag, Strecke2d):
                ergebnis.append(eintrag)

            if isinstance(eintrag, list):
                print("prüfe Varianten aus:", eintrag)
                for variante in eintrag:
                    print("prüfe Variante:", variante)
                    gefundeneRouten = ermittleRouten(variante)
                    neueRouten = []
                    for unterRoute in gefundeneRouten:
                        print("füge Variante hinzu:", [variante, unterRoute])
                        ergebnis.append([variante, unterRoute])

    return ergebnis

# lege die Wegpunkte fest [Name, x-Koordinate, y-Koordinate]
listeDerWegpunkte = [
    ["A", 1, 1],
    ["B", 2, 2],
    ["C", 3, 2],
    ["D", 2, 3],
    ["E", 4, 0],
    ["F", 5, 0],
    ["Z", 0, 0]
]

# übertrage die Wegpunkte in Objekte der Klasse Punkt2d
listeDerWegpunkte2 = []
for datensatz in listeDerWegpunkte:
    wegpunkt = Punkt2d(datensatz[0], datensatz[1], datensatz[2])
    print("erzeuge Wegpunkt:")
    wegpunkt.info()
    listeDerWegpunkte2.append(wegpunkt)

# lege die Teilstrecken fest: [Startpunkt, Endpunkt]
listeDerTeilstrecken = [
    ["A", "B"],
    ["B", "C"],
    ["B", "D"],
    ["C", "E"],
    ["D", "E"],
    ["E", "F"],
    ["Z", "A"]
]

# übertrage die Teilstrecken in Objekte der Klasse Strecke2d
listeDerTeilstrecken2 = []
for datensatz in listeDerTeilstrecken:
    startpunkt = datensatz[0]
    zielpunkt = datensatz[1]

    streckenanfang = None
    streckenende = None
    for eintrag in listeDerWegpunkte2:
        if startpunkt == eintrag.getBezeichnung():
            streckenanfang = eintrag
            break
    for eintrag in listeDerWegpunkte2:
        if zielpunkt == eintrag.getBezeichnung():
            streckenende = eintrag
            break
    teilstrecke = Strecke2d("Teilstrecke", streckenanfang, streckenende)
    print("lege neue Teilstrecke an:")
    teilstrecke.info()
    listeDerTeilstrecken2.append(teilstrecke)

#listeDerRouten = []


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
graph = ermittleGraphstruktur(listeDerTeilstrecken2, "A", "C")
print(graph)

# for eintrag in graph:
#     if isinstance(eintrag, Strecke2d):
#         print(eintrag.getWegpunkt1().getBezeichnung(), "->", eintrag.getWegpunkt2().getBezeichnung())
#     else:
#    	print(eintrag)

# listeDerRouten = ermittleRouten(graph)
# print(listeDerRouten)
#for einzelneRoute in listeDerRouten:
#    print("gefundene Route:", einzelneRoute)
