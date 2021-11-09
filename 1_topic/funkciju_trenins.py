"""
Uzraksti funkciju, kura atgriež vērtību True, ja abi dotie vārdi sākas ar vienu burtu
"""
"""
sakas_vienadi("Liela Lama") -----> True
sakas_vienadi("Maza Lama") ------> False
"""

"""
Noderīgas metodes:

.split()
.lower()
"""

def sakas_vienadi(teksts):
  teksts = teksts.lower().split()

  print(type(teksts))

  if teksts[0][0] == teksts[1][0]:
    return True
  else:
    return False

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("Maza Lama"))

def sakas_vienadi(teksts):
  teksts = teksts.lower().split()

  return teksts[0][0] == teksts[1][0]

print(sakas_vienadi("Liela Lama"))
print(sakas_vienadi("Maza Lama"))


'''
Uzraksti funkciju, kura atgriež mazāko skaitli, ja abi skaitļi ir pāra skaitļi.
Ja viens no skaitļiem vai abi ir nepāra skaitļi, tad funkcija atgriež lielāko skaitli.
atgriez_skaitli(2,4) --> 2
atgriez_skaitli(2,5) --> 5
'''
'''
4%2=0
'''

def atgriez_skaitli(a,b):
  if a%2==0 and b%2==0:
    return min(a,b)
  else:
    return max(a,b)


    