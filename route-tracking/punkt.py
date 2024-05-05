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
    
