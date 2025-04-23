# README

* [punkt.py](punkt.py)
** Modul mit Klasse `Punkt` im eindimensionalen Raum

* [punkt1d.py](punkt1d.py)
** Modul mit Klasse `Punkt1d` im eindimensionalen Raum
** basiert auf Klasse `Punkt` aus [punkt.py](punkt.py)

* [punkt2d.py](punkt2d.py)
** Modul mit Klasse `Punkt2d` im zweidimensionalen Raum
** basiert auf Klasse `Punkt1d` aus [punkt1d.py](punkt1d.py)

* [strecke.py](strecke.py)
** Modul mit Klasse `Strecke` im eindimensionalen Raum
** basiert auf Klasse `Punkt` aus [punkt.py](punkt.py)

* [strecke1d.py](strecke1d.py)
** Modul mit Klasse `Strecke1d` im eindimensionalen Raum
** basiert auf den beiden Klassen `Strecke` und `Punkt1d` aus [strecke.py](strecke.py) und [punkt1d.py](punkt1d.py)

* [strecke2d.py](strecke2d.py)
** Modul mit Klasse `Strecke2d` im zweidimensionalen Raum
** basiert auf den beiden Klassen `Strecke1d` und `Punkt2d`aus [strecke1d.py](strecke1d.py) und [punkt2d.py](punkt2d.py)
** benötigt Modul `math`

* [route2d.py](route2d.py)
** Modul mit Klasse `Route2d` im zweidimensionalen Raum
** basiert auf den beiden Klassen `Strecke2d` und `Punkt2d` aus [strecke2d.py](strecke2d.py) und [punkt2d.py](punkt2d.py)
** benötigt Modul `math`

* [route-berechnen.py](route-berechnen.py)
** Anwendungsbeispiel zur Ermittlung der Länge einer Route auf der Basis von Wegpunkten als Punktliste
** vergleiche zwei Routen und gib die kürzere Route aus
