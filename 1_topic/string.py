'''
Mainīgais string
Teksta mainīgais
'''

dog = "Reksis"

print(dog, end = " ")
print(dog)
print(dog, dog)

print(dog, end = "\n\n")
print(dog)

dog = "Vētra"

print(dog)

print(dog[0])
print(dog[1:5])


print(dog.upper())

#%s
a = "drūms"
print("ārā ir %s laiks" %a)

#.format metode
print("ārā ir {0} un {1} laiks" .format("drūms", "apmācies"))

#f strings metode
print(f"ārā ir {a} laiks")

#teksta un mainīgā savienošana?:D
print("ārā ir " + a + " laiks")