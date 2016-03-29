#!/usr/bin/env python
# -*- coding: utf-8 -*-

message = "Hello Berlin, Москва, 北京, world!"
print (message)


# Zahlenwert (Integer)
anzahl = 15

# Zahlenwert (Gleitkommazahl)
umsatzsteuer_7 = 1.07
umsatzsteuer_19 = 1.19

# Zeichenkette
bezeichner = "Zahnbürste"

# Liste
artikelListe = [anzahl, umsatzsteuer_19, bezeichner]
print(artikelListe)

artikel = {
	"menge": anzahl,
	"ust": umsatzsteuer_19,
	"bezeichner": bezeichner
}

# Ausgabe der Artikelmenge
print (artikel["menge"])

# Menge
farben = {"rot", "grün", "blau"}

# Prüfen auf Enthaltensein
if "blau" in farben:
	print ("blau ist in der Farbmenge enthalten")

if "gelb" not in farben:
	print ("gelb ist nicht in der Farbmenge enthalten")

# Mengen definieren
farben = ("rot", "grün", "blau")
rgb = {
	"rot" : "#F00",
	"grün": "#0F0",
	"blau": "#00F"
}

for eintrag in farben:
	print ("Farbe: %s" % eintrag)
	print ("RGB-Code:", rgb[eintrag])

# mit while-Schleife
farben = ("rot", "grün", "blau")

# Anzahl der Mengenelemente ermitteln
anzahlFarben = len(farben)
print(anzahlFarben)

i = 0
while i < anzahlFarben:
    print ("%i: %s" % (i, farben[i]))
    i = i + 1
    
input('Drücken Sie die Enter-Taste um das Programm zu beenden')

import sys

# Funktion aus dem importierten Modul benutzen
# - Kommandozeilenargument 0
print (sys.argv[0])

# - Rückkehr mit Exit-Code 1
sys.exit(1)

# Funktion definieren
def meineFunktion():
    """ Gibt die Zeichenkette 'Berlin' zurück."""
	ort = "Berlin"

	return ort

# Funktion aufrufen
ergebnis = meineFunktion()
print (ergebnis)

def umrechnung(parameter1, parameter2):
	zusatzwert = 15

	return [parameter2, parameter1, zusatzwert]

ergebnisliste = umrechnung(2,4)
print (ergebnisliste)
