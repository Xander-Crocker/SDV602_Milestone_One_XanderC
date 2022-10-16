"""
This file creates the GUI for the Colour_Layout tab when green button clicked.

"""

import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from view.des_view import DesView

def CL_Green(df, draw_figure):
    """
    Function that creates Green Cards window when clicked in Colour_Layout tab.  
    
    """
    
    green_card_view = DesView("Top 10 Green Cards", 
                            [[sg.Text("Top 10 Green Cards", justification='center', size=(135,1))],
                            # Summery Information Placeholder
                            [sg.Text("Summery Information:"),
                            sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                            # Canvas for graph
                            [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                            # Chat Box
                            [sg.Text('Output', size=(40, 1))],
                            [sg.Output(size=(125, 3), font=('Helvetica 10')),
                            # Zoom Buttons
                            sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                            # Chat Box
                            [sg.Text('Input', size=(40, 1))],
                            [sg.Multiline(size=(125, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                            sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                            # Settings Button
                            sg.Button('Settings', size=(8, 1))]], 
                        df, draw_figure)
    
    green_card_view.accept()
    
