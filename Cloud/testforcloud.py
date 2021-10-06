import PySimpleGUI as sg, sys
import pandas as pd

df = pd.read_csv(r"C:\Users\avivy\PycharmProjects\pythonProject\pysimplegui\test_for_main.csv", header=None)
first_col = df.iloc[:, 0].values

a = "\n".join(first_col)
print (a)


form = sg.FlexForm("Dynamic Combo")
col = [[sg.Checkbox(f'{i}', enable_events=True, font='consolas 10')
        for i in a]]
layout = [[sg.Text('<-- Scroll with Checkbox -->')],
          [sg.Column(col, size=(150, 150), scrollable=True)],
          [sg.Cancel('Exit')]
          ]

form = sg.Window('Checkbox practice').Layout(layout)

while True:
    event, values = form.Read()
    if event == "SELECT ALL":
        # IN THE RANGE ALWAYS PUT A NUMBER MORE TO GET THAT NUMBER
        for x in range(1, 19):
            form.FindElement(x).Update(True)
    if event == "DESELECT ALL":
        # IN THE RANGE ALWAYS PUT A NUMBER MORE TO GET THAT NUMBER
        for x in range(1, 19):
            form.FindElement(x).Update(False)
    if event == "Exit":
        sys.exit()
