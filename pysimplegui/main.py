import sys
import PySimpleGUI as sg
import os
import pandas as pd
import threading
import time

SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'

df = pd.read_csv(r"C:\Users\avivy\PycharmProjects\pythonProject\pysimplegui\test_for_main.csv", header=None)
first_col = df.iloc[:, 0].values
second_col = df.iloc[:, 1].values
third_col = df.iloc[:, 2].values
forth_col = df.iloc[:, 3].values

print(first_col)

buttons_names = [first_col[0], second_col[0], third_col[0]]
fonts = ['consolas 10', 'calbiri 12', 'david 11']
coloros = ['Black', 'BlueMono', 'BluePurple', 'BrightColors', 'BrownBlue', 'Dark', 'Dark2', 'DarkAmber', 'DarkBlack',
           'DarkBlack1', 'DarkBlue', 'DarkBlue1', 'DarkBlue10', 'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 'DarkBlue14',
           'DarkBlue15', 'DarkBlue16', 'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 'DarkBlue4', 'DarkBlue5', 'DarkBlue6',
           'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 'DarkBrown', 'DarkBrown1', 'DarkBrown2', 'DarkBrown3', 'DarkBrown4',
           'DarkBrown5', 'DarkBrown6', 'DarkBrown7', 'DarkGreen', 'DarkGreen1', 'DarkGreen2', 'DarkGreen3',
           'DarkGreen4',
           'DarkGreen5', 'DarkGreen6', 'DarkGreen7', 'DarkGrey', 'DarkGrey1', 'DarkGrey10', 'DarkGrey11', 'DarkGrey12',
           'DarkGrey13', 'DarkGrey14', 'DarkGrey2', 'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 'DarkGrey6', 'DarkGrey7',
           'DarkGrey8',
           'DarkGrey9', 'DarkPurple', 'DarkPurple1', 'DarkPurple2', 'DarkPurple3', 'DarkPurple4', 'DarkPurple5',
           'DarkPurple6',
           'DarkPurple7', 'DarkRed', 'DarkRed1', 'DarkRed2', 'DarkTanBlue', 'DarkTeal', 'DarkTeal1', 'DarkTeal10',
           'DarkTeal11',
           'DarkTeal12', 'DarkTeal2', 'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 'DarkTeal6', 'DarkTeal7', 'DarkTeal8',
           'DarkTeal9',
           'Default', 'Default1', 'DefaultNoMoreNagging', 'GrayGrayGray', 'Green', 'GreenMono', 'GreenTan',
           'HotDogStand', 'Kayak',
           'LightBlue', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightBlue5', 'LightBlue6',
           'LightBlue7', 'LightBrown',
           'LightBrown1', 'LightBrown10', 'LightBrown11', 'LightBrown12', 'LightBrown13', 'LightBrown2', 'LightBrown3',
           'LightBrown4',
           'LightBrown5', 'LightBrown6', 'LightBrown7', 'LightBrown8', 'LightBrown9', 'LightGray1', 'LightGreen',
           'LightGreen1', 'LightGreen10',
           'LightGreen2', 'LightGreen3', 'LightGreen4', 'LightGreen5', 'LightGreen6', 'LightGreen7', 'LightGreen8',
           'LightGreen9',
           'LightGrey', 'LightGrey1', 'LightGrey2', 'LightGrey3', 'LightGrey4', 'LightGrey5', 'LightGrey6',
           'LightPurple', 'LightTeal',
           'LightYellow', 'Material1', 'Material2', 'NeutralBlue', 'Purple', 'Python', 'Reddit', 'Reds',
           'SandyBeach', 'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 'Tan', 'TanBlue', 'TealMono']


def collapse(layout, key):
    return sg.pin(sg.Column(layout, key=key))


def window1():
    sg.ChangeLookAndFeel(f'{coloros[13]}')
    section1 = [[sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)],
                [sg.Button(f'{first_col[0]}', font='{}'.format(fonts[0])),
                 sg.Button('{}'.format(buttons_names[1]), font='{}'.format(fonts[0])),
                 sg.Button('{}'.format('change'), font='{}'.format(fonts[0])),
                 sg.Button('{}'.format('check'), font='{}'.format(fonts[0])),
                 sg.Button('{}'.format('refresh'), font='{}'.format(fonts[0])),
                 sg.Button('{}'.format('color change'), font='{}'.format(fonts[0])),
                 sg.Button('{}'.format(buttons_names[2]), font='{}'.format(fonts[0]))
                 ]]

    section2 = [[sg.I('', k='-IN2-')],
                [sg.I(k='-IN21-')],
                [sg.B('{}'.format(buttons_names[0]), font='{}'.format(fonts[0])),
                 sg.B('{}'.format(buttons_names[1]), font='{}'.format(fonts[0])),
                 sg.B('{}'.format(buttons_names[2]), font='{}'.format(fonts[0]))]]

    tab1_layout = [
        [sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:]))],
        [sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:]))],
        [sg.B('{}'.format(buttons_names[1]), font=fonts[0])]]

    tab2_layout = [
        [sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:]))]]
    tab3_layout = [
        [sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:])), sg.InputOptionMenu((first_col[1:]))]]
    tab4_layout = [
        [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)]]
    tab5_layout = [
        [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)]]
    tab6_layout = [
        [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)]]
    tab7_layout = [
        [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)]]
    tab8_layout = [
        [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)]]
    tab9_layout = [
        [sg.Slider(range=(1, 1000), orientation='h', size=(34, 20), default_value=0)]]

    layout = [[sg.Text('Window with 2 collapsible sections')],
              [sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout), sg.Tab('Tab 3', tab3_layout),
                             sg.Tab('Tab 4', tab4_layout), sg.Tab('Tab 5', tab5_layout), sg.Tab('Tab 6', tab6_layout),
                             sg.Tab('Tab 7', tab7_layout), sg.Tab('Tab 8', tab8_layout),
                             sg.Tab('Tab 9', tab9_layout)]])],
              [sg.Checkbox('Blank checkbox'),
               sg.Checkbox('Hide Section 2', enable_events=True, key='-OPEN SEC2-CHECKBOX')],
              # Section 1 part
              [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='purple'),
               sg.T('Section 1', enable_events=True, text_color='white', k='-OPEN SEC1-TEXT')],
              [collapse(section1, '-SEC1-')],
              # Section 2 part
              [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
               sg.T('Section 2', enable_events=True, text_color='white', k='-OPEN SEC2-TEXT')],
              [collapse(section2, '-SEC2-')],
              # Buttons at bottom
              [sg.Button('What have i done so far?', font=fonts[0]), sg.Button('Button2', font=fonts[0]),
               sg.Button('Exit', font=fonts[0])]]

    window = sg.Window('Main Window', layout, finalize=True)

    opened1, opened2 = True, True

    while True:  # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            quit()

        if event.startswith('-OPEN SEC1-'):
            opened1 = not opened1
            window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
            window['-SEC1-'].update(visible=opened1)

        if event.startswith('-OPEN SEC2-'):
            opened2 = not opened2
            window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
            window['-OPEN SEC2-CHECKBOX'].update(not opened2)
            window['-SEC2-'].update(visible=opened2)

        if event.startswith(buttons_names[0]):
            window.hide()
            os.system('python Checklist01.py')
            window.un_hide()

        if event.startswith('change'):
            if first_col[0] == 'Name':
                first_col[0] = 'koko'
            elif first_col[0] == 'koko':
                first_col[0] = 'Name'

        if event.startswith('check'):
            print(first_col[0])

        if event.startswith('koko'):
            print('do nothing')

        if event.startswith('refresh'):
            window.close()
            window == window1()

        if event.startswith('color change'):
            window.close()
            coloros[13] = coloros[5]
            window == window1()

        if event.startswith(buttons_names[1]):
            window.hide()
            os.system('python Checklist02.py')
            window.un_hide()

        if event.startswith(buttons_names[2]):
            window.hide()
            os.system('python Checklist03.py')
            window.un_hide()

        if event.startswith('What have i done so far?'):
            window.hide()
            if os.path.isfile('lolo.py'):
                with open('lolo.py') as f:
                    lines = f.readlines()
                    sg.popup(lines)
            window.un_hide()

            if not os.path.isfile('lolo.py'):
                sg.popup(r'you haven\'t submitted nothing yet.')
                window.un_hide()


def main():
    window1()


if __name__ == "__main__":
    main()
