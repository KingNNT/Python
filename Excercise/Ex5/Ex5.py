import numpy as np
import codecs
import sys
import pandas as pd
import PySimpleGUI as sg

sys.stdin = codecs.getreader('utf_8')(sys.stdin)

def main():
    # define the window layout
    layout = [
                [sg.Text('Nhập môn học máy: Kỹ năng thao tác file csv', size=(80, 1), justification='center', font='Helvetica 10')],
                [sg.Text('Tên file csv'), sg.InputText()],
                [sg.Button('Đọc file', size=(10, 1), font='Helvetica 12'),sg.Text('(tải vào pandas dataframe)')],
                [sg.Button('Thoát', size=(10, 1), font='Helvetica 12')]
            ]

    window = sg.Window('Khoa CNTT Đại học Điện Lực',layout, location=(800, 400))

    while True:
        event, values = window.read()
        if event == 'Thoát' or event == sg.WIN_CLOSED:
            return
        elif event == 'Đọc file':
            if values[0] != '':
                try:
                    df = pd.read_csv(values[0])# ('iris.csv')
                    print(df)
                except:
                    print('Error')

if __name__ == "__main__":
    main()