class Transportlidzeklis:

  krasa = "Melna"

  def __init__(self, nosaukums, max_atrums, nobraukums):
    self.nosaukums = nosaukums
    self.max_atrums = max_atrums
    self.nobraukums = nobraukums

  def sedvietu_skaits(self,skaits):
    self.skaits = skaits
    return f"Sēdvietu skaits {self.nosaukums} ir {self.skaits}."

  def biletes(self):
    return self.skaits * 0.5

modelisX = Transportlidzeklis("Mersedess", 180, 2000)
print(modelisX.max_atrums, modelisX.nobraukums, modelisX.nosaukums)

class Buss(Transportlidzeklis):
  def sedvietu_skaits(self, skaits = 50):
    return super().sedvietu_skaits(skaits)

  def biletes(self):
    return super().biletes()


modelisX = Buss("Audi", 240, 1800)
print(modelisX.max_atrums, modelisX.nobraukums, modelisX.nosaukums)

skolas_buss = Buss("EcoLine", 130, 3500)
print(skolas_buss.sedvietu_skaits(200))

modelisX = Buss("Audi", 240, 1800)
print(modelisX.max_atrums, modelisX.nobraukums, modelisX.nosaukums, modelisX.krasa)
print(modelisX.sedvietu_skaits())
print(modelisX.biletes())
