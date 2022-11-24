"""
This file creates a new window for each button in the DES Two (CCL_) and DES Three (CL_) tabs when clicked.
Also holds the event loop for each of these new windows.
"""

import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from view.figures import Excel_Graph


class DesView(object):
    """
    Creates a new window for each button in the DES Two (CCL_) and DES Three (CL_) tabs.
    Holds the event loop for each new window.
    """
    def __init__(self, Name, layout, df, draw_figure):
        self.layout = layout
        self.window = sg.Window(Name, layout, modal=True, finalize=True)
        draw_figure(self.window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks'], df))
        
    def accept(self):
        while True:
            event, values = self.window.read()
            if event == "Exit" or event == sg.WIN_CLOSED:
                break
            if event == 'SEND':                                 # If send button clicked, print input to output.
                query = values['-QUERY-'].rstrip()
                print('User 1: {}'.format(query), flush=True) 
            
        self.window.close()
