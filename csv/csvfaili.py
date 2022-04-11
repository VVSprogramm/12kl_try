import csv

fails = open("csv_meg.csv")

lasit_csv = csv.reader(fails)

print(lasit_csv)

header = []
header = next(lasit_csv)

print(header)

saturs = []
for rinda in lasit_csv:
  saturs.append(rinda)

print(saturs)

fails.close()

#Faila izveide

kolonnuNosaukumi = ["Vārds","1.atzīme", "2.atzīme"]
dati = [["Anna",9,8],["Viesturis",6,8],["Kārlis",9,10], ["Sibilla",9,5]]

with open("skolenu_atzimes.csv","w") as f:
  csvwriter = csv.writer(f)
  csvwriter.writerow(kolonnuNosaukumi)
  csvwriter.writerows(dati)


