# -----------------------------------------------------------
# demonstriert die Ermittlung einer Route in einem Graphen im
# zweidimensionalen Raum mit Hilfe der Bibliothek networkx
# (networkx: https://pypi.org/project/networkx/)
#
# (C) 2025-2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

from route2d import Route2d
from strecke2d import Strecke2d
from punkt2d import Punkt2d

import networkx as nx

# lege die Wegpunkte fest [Name, x-Koordinate, y-Koordinate]
wegpunktA = Punkt2d("A", 1, 1)
wegpunktB = Punkt2d("B", 2, 2)
wegpunktC = Punkt2d("C", 3, 2)
wegpunktD = Punkt2d("D", 3, 3)
wegpunktE = Punkt2d("E", 4, 0)
wegpunktF = Punkt2d("F", 5, 0)
wegpunktZ = Punkt2d("Z", 0, 0)
listeDerWegpunkte = [wegpunktA, wegpunktB, wegpunktC, wegpunktD, wegpunktE, wegpunktF, wegpunktZ]

# übertrage die Wegpunkte in Objekte der Klasse Punkt2d
for wegpunkt in listeDerWegpunkte:
    print("erzeuge Wegpunkt:")
    wegpunkt.info()

# definiere Streckennetz als leeren Graphen
streckennetz = nx.Graph()

# lege die Teilstrecken fest: [Startpunkt, Endpunkt]
teilstrecke1 = Strecke2d("Teilstrecke 1", wegpunktA, wegpunktB)
teilstrecke2 = Strecke2d("Teilstrecke 2", wegpunktB, wegpunktC)
teilstrecke3 = Strecke2d("Teilstrecke 3", wegpunktB, wegpunktD)
teilstrecke4 = Strecke2d("Teilstrecke 4", wegpunktC, wegpunktE)
teilstrecke5 = Strecke2d("Teilstrecke 5", wegpunktD, wegpunktE)
teilstrecke6 = Strecke2d("Teilstrecke 6", wegpunktE, wegpunktF)
teilstrecke7 = Strecke2d("Teilstrecke 7", wegpunktZ, wegpunktA)

listeDerTeilstrecken = [teilstrecke1, teilstrecke2, teilstrecke3, teilstrecke4, teilstrecke5, teilstrecke6, teilstrecke7]

for teilstrecke in listeDerTeilstrecken:
    print("lege neue Teilstrecke an:")
    teilstrecke.info()

    # füge jede Teilstrecke dem Streckennetz hinzu, Gewicht: 1
    bezeichnung = teilstrecke.getBezeichnung()
    von = teilstrecke.getWegpunkt1().getBezeichnung()
    nach = teilstrecke.getWegpunkt2().getBezeichnung()
    streckennetz.add_edge(von, nach, weight="1")

# ermittle kürzesten Pfad von Wegpunkt A nach D
pfad = nx.shortest_path(streckennetz, "A", "D")
print("gefundener Weg von A nach D:", pfad)
