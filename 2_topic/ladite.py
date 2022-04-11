#OOP - 2030

#1.uzdevums

print(f'{"Sveiks/a!":^25s}')
print("Šī programma izdrukās vienkāršu rēķinu koka lādītei ar gravējumu!\n\n\n")

klients = input("Pasūtītāja vārds, uzvārds: ")
print("-"*50)
veltijums = input("Nepieciešamais veltījums: ")
print("-"*50)
izmers = input("Lādītes izmērs - platums, garums, augstums - milimetros (Raksti veselus skaitļus): ")
print("-"*50)
materials = input("Kokmateriāla cena EUR/m2: ")

class Rekins():


    def __init__(self, klients, veltijums, izmers, materials):
        
        self.klients = klients
        self.veltijums = veltijums
        self.izmers = izmers
        self.materials = float(materials)

        sad_izm = self.izmers.split(",")
        self.platums = float(sad_izm[0])
        self.garums = float(sad_izm[1])
        self.augstums = float(sad_izm[2])

        self.veltijuma_garums = float(len(self.veltijums))

        self.aprekins()

    def izdrukat(self):

        print("\n\n")
        print('\033[1m'+"Pasūtītāja dati:"+'\033[0m')
        print("-"*50)
        print(f"\x1B[3mPasūtītāja vārds un uzvārds:\x1B[0m \033[1;32m{self.klients}\033[1;0m")
        print(f"\x1B[3mVeltījuma teksts:\x1B[0m \033[1;32m{self.veltijums}\033[1;0m") 
        print(f"\x1B[3mLādītes izmēri:\x1B[0m \n\x1B[3mPlatums:\x1B[0m \033[1;32m{self.platums}\033[1;0m\n\x1B[3mGarums:\x1B[0m \033[1;32m{self.garums}\033[1;0m\n\x1B[3mAugstums:\x1B[0m \033[1;32m{self.augstums}\033[1;0m")
        print(f"\x1B[3mMateriāla cena EUR/m2:\x1B[0m \033[1;32m{self.materials}\033[1;0m")
        print(f"\x1B[3mIzmaksas:\x1B[0m \033[1;32m{self.aprekins()}\033[1;0m")

        self.saglabat()
        print(f"Rēķina dati saglabāti failā {self.klients}.csv")

        

    
    def aprekins(self):

        darba_samaksa = 15
        PVN = 21
        produkta_cena = (self.veltijuma_garums) * 1.2 + (self.platums/100 * self.garums/100 * self.augstums/100)/ 3 * self.materials
        PVN_summa = (produkta_cena + darba_samaksa)*PVN/100 
        rekina_summa = (produkta_cena + darba_samaksa) + PVN_summa

        return rekina_summa

    def saglabat(self):

      import csv

      with open (f'{self.klients}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Klienta vārds','Veltījums','Izmēri','Kokmateriāla cena'])



    



a = Rekins(klients,veltijums,izmers,materials)
# print(a.platums)
# print(a.garums)
# print(a.augstums)
# print(a.veltijuma_garums)
a.izdrukat()

#print(a.aprekins())
