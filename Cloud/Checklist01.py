import PySimpleGUI as sg
from datetime import datetime
import pandas as pd

df = pd.read_csv(r"C:\Users\avivy\PycharmProjects\pythonProject\pysimplegui\test_for_main.csv", index_col=False)
first_col = df.iloc[:, 0].values
second_col = df.iloc[:, 1].values
third_col = df.iloc[:, 2].values

# print(df.loc[df['name'] == 'aviv'])
# print(df.loc[df['name'].str.contains('ha')])
# print(df['ID'].value_counts())
# print(df['ID'].value_counts())

buttons_names = [first_col[0], first_col[1], first_col[2]]


def make_win2():
    sg.ChangeLookAndFeel('DarkGreen4')
    layout = [
                 [sg.Submit('Submit', font='consolas 10'), sg.Button('Exit', font='consolas 10')],
                 [sg.Button('All checked', font='consolas 10', enable_events=True, key='Check_All'),
                  sg.Button('All unchecked', font='consolas 10', enable_events=True, key='Uncheck_All')],
                 [sg.HorizontalSeparator()]] + [
                 [sg.Checkbox(f'{first_col[i]}', enable_events=True, font='consolas 10', key=f'{first_col[i]}')
                  for i in range(len(first_col))],
                 [sg.T(first_col[0]), sg.InputOptionMenu(first_col)],
                 [sg.T(df.sort_values('AWS'), font='consolas 10')],
                 [sg.InputOptionMenu(first_col)]]
    window = sg.Window('Checklist01', layout, finalize=True)

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            dateTimeObj = datetime.now()
            f = open('lolo.py', 'a+')
            f.write(str('Checklist01 = [' + '\n'))
            f.write("'" + str(dateTimeObj) + "'" ',\n')
            f.write(str(values) + ']\n')
            sg.popup('You have successfully submitted')
            f.close()

        if event == 'Check_All':
            for i in range(len(first_col)):
                window[f'{first_col[i]}'].update(True)
        elif event == 'Uncheck_All':
            for i in range(len(first_col)):
                window[f'{first_col[i]}'].update(False)

    window.close()


def main():
    make_win2()
    while True:  # Event Loop
        window, event, values = sg.read_all_windows()

        if window == sg.WIN_CLOSED:  # if all windows were closed
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
        else:
            window['-OUTPUT-'].update('Other window is closed')


main()
