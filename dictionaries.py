#Mainīgais dictionaries jeb bibliotēka

pirmais = {'atsl1':'vert1', 'atsl2':'vert2'}

print(pirmais)

print(pirmais['atsl1'])

#Var glabāt dažādus datu tipus: string, numbers, lists, dictionaries

otrais = {'atsl1':[1,2,3], "atsl2":"vert2"}

print(otrais)

print(pirmais.keys())

tresais = {'atsl1':{'atsl2':[1,2,3]}}

print(tresais)

print(tresais["atsl1"])
print(tresais['atsl1']['atsl2'])
print(tresais['atsl1']['atsl2'][1])