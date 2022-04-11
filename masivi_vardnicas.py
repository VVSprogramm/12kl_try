#Masīvs jeb list

#[]
#Pirmais indekss ir 0
#Pēdējais masīva indekss = masīva garums - 1

'''
Vērtība| A | B | C | D | E |
Indekss| 0 | 1 | 2 | 3 | 4 |
'''

masivs = ["A", "B", "C", "D", "E"]

print(masivs)
print(masivs[3])

for x in masivs:
  print(x)


#Vārdnīca jeb dictionary

#{}
#Katrai vērtībai ir atslēga

'''
Atslēga| Vārds | Izglītība | Vecums |
Vērtība| Jānis | Augstākā  | 45      |
'''

vardnica = {
  "Vārds":"Jānis",
  "Izglītība":"Augstākā",
  "Vecums":45
}

print(vardnica)
print(vardnica["Vārds"])
vardnica["Alga"]=2500
print(vardnica)


#Kombinācija - vārdnīca masīvā

personas = [
  {
  "Vārds":"Jānis",
  "Izglītība":"Augstākā",
  "Vecums":45
  },
  {
  "Vārds":"Pēteris",
  "Izglītība":"Vidējā",
  "Vecums":20
  }
]

for persona in personas:
  print(persona["Vārds"])