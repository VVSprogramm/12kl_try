#Uzraksti funkciju, kas aprēķina ābolu ievārījuma izmaksas, ja dota cena cukuram, āboliem un garšvielām un to daudzums receptē.


recepte1 = {"cukurs":0.6, "kanelis":0.008, "aboli":2.0, "udens":0.2}
cenas1 = {"cukurs":0.75, "kanelis":30.0, "aboli":0.0, "udens":0.0}

def izmaksas_receptei(recepte,cenas):
  #Aprēķina izmakas dotajai receptei

  summa = 0
  for sastavdala in recepte:
    daudzums = recepte[sastavdala]
    summa += daudzums * cenas[sastavdala]

  return summa


def izmaksas_kopa(abolu_svars, recepte, cenas):

  #Izmaksas uz vienu kg ābolu
  izmaksas_kg = izmaksas_receptei(recepte,cenas)/recepte['aboli']

  ievarijuma_izmaksas = abolu_svars * izmaksas_kg

  return ievarijuma_izmaksas

print(izmaksas_kopa(15.0,recepte1,cenas1))





