#Kontaktu grāmatiņa

import d_gramatina

sakums = """Sveicināti!
--------------------------
Lūdzu, izvēlies darbību:
1 - Kontakta pievienošana
2 - Kontakta meklēšana
3 - Kontakta rediģēšana
4 - Kontakta dzēšana
5 - Iziet
--------------------------
"""

#Jaunu kontaktu pievienošana
def kontaktu_piev():
  vards = input("Lūdzu, ievadiet kontakta vārdu: ")
  numurs = input("Lūdzu, ievadiet kontakta numuru: ")

  print(f"Pievieno {vards} ar numuru - {numurs}")

  d_gramatina.piev_kontaktu(vards, numurs)


#Kontaktu atrašana. (Meklē pēc pilna vārda un simbola)
def kont_atrasana():
  vards = input("Lūdzu, ievadi kontakta vārdu, kuru meklē: ")
  numurs = d_gramatina.atrod_kontaktu(vards)
  
  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    sakrit = d_gramatina.kont_meklesana(vards)
    if sakrit:
      for k in sakrit:
        print(f"{k} numurs ir {sakrit[k]}")
    else:
      print(f"Izskatās, ka {vards} nav sarakstā")


#Kontaktu rediģēšana
def kontaktu_red():
  iepr_v = input("Ievadi kontakta vārdu, kuru vēlies rediģēt: ")
  iepr_numurs = d_gramatina.atrod_kontaktu(iepr_v)

  if iepr_numurs:
    jaunais_v = input(f"Ievadi {iepr_v} kontakta jauno vārdu (ja nevēlies mainīt vārdu, atstāj tukšu): ").strip() 
    jaunais_n = input(f"Ievadi {iepr_numurs} kontakta jauno nunuru (ja nevēlies mainīt numuru, atstāj tukšu): ").strip()

    if not jaunais_n:
      jaunais_n = iepr_numurs

    if not jaunais_v:
      d_gramatina.mainit_numuru(iepr_v, jaunais_n)

    else:
      d_gramatina.mainit_kontaktu(iepr_v, jaunais_v, jaunais_n)
  
  else:
    print(f"Izskatās, ka {iepr_v} nav sarakstā")

#Kontaktu dzēšana
def kont_dzesana():
  vards = input("Ievadi kontakta vārdu, kuru vēlies dzēst: ")
  numurs = d_gramatina.atrod_kontaktu(vards)

  if numurs:
    lemums = input(f"Vai Jūs tiešām vēlaties izdzēst šo kontaktu: {vards} - {numurs}? (1 - Jā, 2 - Nē)")

    if lemums == "1":
      d_gramatina.dzest_kont(vards)
    else:
      print(f"Kontakts {vards} netika dzēsts")
      
  else:
    print(f"Izskatās, ka {vards} nav sarakstā")


'''
11.01. uzdevums

#Definēt sākuma izvēlni
#Pievienot funkciju, kas ļaus izvēlēties darbības
#Izveidot ciklu, lai ir iespējams veikt vairākas darbības pēc kārtas
'''

def galvena_izv():
  print(sakums)
  izvele = input("Tava izvēlētā darbība: ")

  if izvele == "1":
    kontaktu_piev()
  elif izvele == "2":
    kont_atrasana()
  elif izvele == "3":
    kontaktu_red()  
  elif izvele == "4":
    kont_dzesana()
  elif izvele == "5":
    quit()
  else:
    print("Neeksistējoša darbība, lūdzu, mēģini vēlreiz!")

while True:
  galvena_izv()
  input("\nNospied Enter, lai turpinātu\n\n")
