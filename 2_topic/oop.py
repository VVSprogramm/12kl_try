#OOP

saraksts = [1,2,3]

print(type(saraksts))

#class
#self
#__str__


class Piem:   #Klases definējam ar lielo burtu
  pass

a = Piem()

print(type(a))


class Car:
  def __init__(self, model):
    self.model = model

ford = Car(model = "Focus")

opel = Car(model = "Astra")

print(ford.model)
print(opel.model)