import tkinter as tk

window = tk.Tk()

lbl_sveiki = tk.Label(
  text = "Sveika, Pasaule!",
  foreground="white", # Teksta krāsa - balta
  background="black" # Fona krāsa - melna
)

lbl_citads = tk.Label(
text = "Jāpamēģina!",
background="#34A2FE",
width=10, #Platums
height=5 #Augstums
)

btn_poga = tk.Button(
text="Noklikšķini!",
width=25,
height=5,
bg="blue", #saīsinājums background
fg="yellow", #saīsinājums foreground
)

def noklikskina(event):
  print("Noklikšķināja!")

btn_poga.bind("<Button-1>", noklikskina)

def noklikskina_lab(event):
  print("Noklikšķināja labo taustiņu!")

btn_poga.bind("<Button-3>", noklikskina_lab)

lbl_sveiki.pack(fill=tk.X)
lbl_citads.pack(side=tk.LEFT)
btn_poga.pack(side = tk.BOTTOM)

window.mainloop()