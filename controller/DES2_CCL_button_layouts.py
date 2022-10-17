"""
DES Two (CCL_) - Colour Combo Layouts
This file creates the GUI for the Colour_Combo_Layout tab when corresponding button clicked.

"""

import PySimpleGUI as sg
import matplotlib
matplotlib.use('TkAgg')
from view.des_view import DesView

def CCL_Azorius(df, draw_figure):
    """
    Azorius Cards layout that opens when 'Azorius' button clicked in Colour Combo tab.  
    
    """
    azorius_card_view = DesView("Top 10 Azorius Cards", 
                                [[sg.Text("Top 10 Azorius Cards", justification='center', size=(135,1))],
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
    
    azorius_card_view.accept()

def CCL_Boros(df, draw_figure):
    """
    Boros Cards layout that opens when 'Boros' button clicked in Colour Combo tab.  
    
    """
    boros_card_view = DesView("Top 10 Boros Cards", 
                                [[sg.Text("Top 10 Boros Cards", justification='center', size=(135,1))],
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
    
    boros_card_view.accept()

def CCL_Dimir(df, draw_figure):
    """
    Dimir Cards layout that opens when 'Dimir' button clicked in Colour Combo tab.   
    
    """
    Dimir_card_view = DesView("Top 10 Dimir Cards", 
                                [[sg.Text("Top 10 Dimir Cards", justification='center', size=(135,1))],
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
    
    Dimir_card_view.accept()

def CCL_Golgari(df, draw_figure):
    """
    Golgari Cards layout that opens when 'Golgari' button clicked in Colour Combo tab.  
    
    """
    golgari_card_view = DesView("Top 10  Cards", 
                                [[sg.Text("Top 10 Golgari Cards", justification='center', size=(135,1))],
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
    
    golgari_card_view.accept()

def CCL_Gruul(df, draw_figure):
    """
    Gruul Cards layout that opens when 'Gruul' button clicked in Colour Combo tab.  
    
    """
    gruul_card_view = DesView("Top 10 Gruul Cards", 
                                [[sg.Text("Top 10 Gruul Cards", justification='center', size=(135,1))],
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
    
    gruul_card_view.accept()

def CCL_Izzet(df, draw_figure):
    """
    Izzet Cards layout that opens when 'Izzet' button clicked in Colour Combo tab.  
    
    """
    izzet_card_view = DesView("Top 10 Izzet Cards", 
                                [[sg.Text("Top 10 Izzet Cards", justification='center', size=(135,1))],
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
    
    izzet_card_view.accept()

def CCL_Orzhov(df, draw_figure):
    """
    Orzhov Cards layout that opens when 'Orzhov' button clicked in Colour Combo tab.   
    
    """
    orzhov_card_view = DesView("Top 10 Orzhov Cards", 
                                [[sg.Text("Top 10 Orzhov Cards", justification='center', size=(135,1))],
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
    
    orzhov_card_view.accept()

def CCL_Rakdos(df, draw_figure):
    """
    Rakdos Cards layout that opens when 'Rakdos' button clicked in Colour Combo tab.    
    
    """
    rakdos_card_view = DesView("Top 10 Rakdos Cards", 
                                [[sg.Text("Top 10 Rakdos Cards", justification='center', size=(135,1))],
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
    
    rakdos_card_view.accept()

def CCL_Selesnya(df, draw_figure):
    """
    Selesnya Cards layout that opens when 'Selesnya' button clicked in Colour Combo tab.    
    
    """
    selesnya_card_view = DesView("Top 10 Selesnya Cards", 
                                [[sg.Text("Top 10 Selesnya Cards", justification='center', size=(135,1))],
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
    
    selesnya_card_view.accept()

def CCL_Simic(df, draw_figure):
    """
    Simic Cards layout that opens when 'Simic' button clicked in Colour Combo tab.   
    
    """
    simic_card_view = DesView("Top 10 Simic Cards", 
                                [[sg.Text("Top 10 Simic Cards", justification='center', size=(135,1))],
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
    
    simic_card_view.accept()