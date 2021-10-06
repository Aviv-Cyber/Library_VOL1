import PySimpleGUI as sg
from datetime import datetime


def make_win2():
    sg.ChangeLookAndFeel('DarkGreen4')
    layout = [
                 [sg.Submit('Submit', font='consolas 10'), sg.Button('Exit', font='consolas 10')],
                 [sg.Button('All checked', font='consolas 10', enable_events=True, key='Check_All'),
                  sg.Button('All unchecked', font='consolas 10', enable_events=True, key='Uncheck_All')],
                 [sg.HorizontalSeparator()]] + [
                 [sg.Checkbox(f'position ({j}, {i})', enable_events=True, font='consolas 10', key=f'position{j}{i}')
                  for i in range(2)] for j in range(2)
             ]

    window = sg.Window('Checklist02', layout, finalize=True)

    while True:
        event, values = window.read(timeout=100)
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Submit':
            dateTimeObj = datetime.now()
            f = open('lolo.py', 'a+')
            f.write(str('Checklist03 = [' + '\n'))
            f.write("'" + str(dateTimeObj) + "'" ',\n')
            f.write(str(values) + ']\n')
            sg.popup('You have successfully submitted')
            f.close()

        if event == 'Check_All':
            for j in range(2):
                for i in range(2):
                    window[f'position{j}{i}'].update(True)
        elif event == 'Uncheck_All':
            for j in range(2):
                for i in range(2):
                    window[f'position{j}{i}'].update(False)

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


