import PySimpleGUI as sg

masivs = [(1,'Anna',15),(2,'Vilhelmīne',36)]

layout = []

for i in range (1,6):
  layout += [sg.Text(f'{i}'),sg.In(key=i)],
layout += [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('Saraksts',layout)
event,values = window.read()