# Mainīgais list jeb saraksts

# Definē ar []

my_list = [1,2,3]
print(my_list) 

my_list = ['Teksts', 2, 3.5]
print(my_list)


#Funkcija len()

print("Mana saraksta mainīgo daudzums: ", len(my_list))

#Var izmantot Index

print(my_list[0:2])

#Elementa maiņu

my_list[0] = "Saruna"
print(my_list)

#Elementa pievienošana

print(my_list + ["Sanāca"])

print(my_list)

my_list = my_list + ["Ir!!!"]

print(my_list)

#Var izmantot *

print(my_list *2)

#Append

my_list.append('append me')
print(my_list)

#Pop

my_list.pop(0)
print(my_list)

#Pop elementu parādīšana

popped_item = my_list.pop()
print(popped_item)