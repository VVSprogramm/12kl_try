import random

while True:
  print("Akmens, šķēres, papīrīts - aiziet!")
  izveele = input("Izvēlies - Akmens(A), Šķēres (S), Papīrs (P): ")
  print("Tu izvēlējies " + izveele)

  defizveeles = ['A','S','P']
  pretIzveele = random.choice(defizveeles)

  print("Es izvēlējos: " +pretIzveele)

  if pretIzveele == izveele:
    print("Neizšķirts!")
  
  #Definēt apgalvojumus pārējām situācijām
  #Pārbaudīt vai spēle strādā
  #Aizsūtīt izmaiņas uz repozitoriju
  
  elif pretIzveele == "S" and izveele == "P":
     

  