"""
DES Three (CL_) - Colour Layouts
This file creates the GUI for the Colour_Layout tab when corresponding button clicked.

"""

import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from view.des_view import DesView

def CL_Multicolour(df, draw_figure):
    """
    Multicolour Cards layout that opens when 'Multicolour' button clicked in Colour tab.   
    
    """  
    multicolour_card_view = DesView("Top 10 Multicolour Cards", 
                                [[sg.Text("Top 10 Multicolour Cards", justification='center', size=(135,1))],
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
    
    multicolour_card_view.accept()

def CL_White(df, draw_figure):
    """
    White Cards layout that opens when 'White' button clicked in Colour tab. 
    
    """
    white_card_view = DesView("Top 10 White Cards", 
                                [[sg.Text("Top 10 White Cards", justification='center', size=(135,1))],
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
    
    white_card_view.accept()

def CL_Red(df, draw_figure):
    """
    Red Cards layout that opens when 'Red' button clicked in Colour tab.  
    
    """
    red_card_view = DesView("Top 10 Red Cards", 
                                [[sg.Text("Top 10 Red Cards", justification='center', size=(135,1))],
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
    
    red_card_view.accept()

def CL_Green(df, draw_figure):
    """
    Green Cards layout that opens when 'Green' button clicked in Colour tab. 
    
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

def CL_Blue(df, draw_figure):
    """
    Blue Cards layout that opens when 'Blue' button clicked in Colour tab.   
    
    """
    blue_card_view = DesView("Top 10 Blue Cards", 
                                [[sg.Text("Top 10 Blue Cards", justification='center', size=(135,1))],
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
    
    blue_card_view.accept()

def CL_Black(df, draw_figure):
    """
    Black Cards layout that opens when 'Black' button clicked in Colour tab.   
    
    """
    black_card_view = DesView("Top 10 Black Cards", 
                                [[sg.Text("Top 10 Black Cards", justification='center', size=(135,1))],
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
    
    black_card_view.accept()