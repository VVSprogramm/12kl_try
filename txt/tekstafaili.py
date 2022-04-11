#Teksta faila izveide
# w - writing jeb rediģēšanas, rakstīšanas stāvoklis
# r - read - lasīšana
# a - pievieno faila beigās

fails = open("pirmais.txt","w",encoding="utf-8")

fails.write("Sveiki!")

saturs = ["Ir 2022.gads\n", "Ārā snieg\n"]

fails.writelines(saturs)

fails.close()


with open("pirmais.txt","r",encoding="utf-8") as f:
  print(f.readline())
  print(f.read())

  f.seek(0)

  print(f.readline())


with open("pirmais.txt","a",encoding="utf-8") as f:  
  f.write("Es esmu te")

with open("pirmais.txt","w",encoding="utf-8") as f:  
  f.write("Kas notika?")
  