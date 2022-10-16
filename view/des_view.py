"""
This file ???

"""

import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from view.figures import Excel_Graph


class DesView(object):
    def __init__(self, Name, layout, df, draw_figure):
        self.layout = layout
        self.window = sg.Window(Name, layout, modal=True, finalize=True)
        draw_figure(self.window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks'], df))
        
    def accept(self):
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == 'SEND':
                query = values['-QUERY-'].rstrip()
                print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
            
        self.window.close()
        