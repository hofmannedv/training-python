class Punkt:
  bezeichnung = ""

  def __init__(self, bezeichnung):
    self.bezeichnung = bezeichnung
    return

  def setBezeichnung(self, bezeichnung):
    self.bezeichnung = bezeichnung
    return
    
  def getBezeichnung(self):
    return self.bezeichnung
    
  def hasBezeichnung(self):
    return self.bezeichnung != ""
    
  def compareBezeichnung(self, bezeichnung):
    return self.bezeichnung == bezeichnung

if __name__ == '__main__':
  p1 = Punkt("Startpunkt")
  print ("Name des Punkts:", p1.getBezeichnung())

  p1.setBezeichnung("Endpunkt")
  print ("Name des Punkts:", p1.getBezeichnung())

  print("prüfe Bezeichnung auf Vorhandensein ... ")
  if p1.hasBezeichnung():
    print("Bezeichnung ist vorhanden")

  for bezeichnung in ("Startpunkt", "Endpunkt"):
    print("teste Bezeichnung auf %s ... " % bezeichnung)
    if p1.compareBezeichnung(bezeichnung):
      print("Bezeichnung stimmt überein:", bezeichnung)
