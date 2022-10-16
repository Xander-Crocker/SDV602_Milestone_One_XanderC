"""
Issues(*) / ToDo(-):
    - Write ReadMe
    - Home page needs to be populated.
    - DES windows needs to be populated.
    - DES two and three needs images for buttons and buttons need repositioning.
    
    - Login and Sign up need to be created.
    - Sign out button on home page. (Take user back to login)
    - Settings page needs to be created.
    - Zoom in and zoom out buttons need to function correctly.
    - Chat needs to function correctly.
    
    * Cant place data for graphs in a separate file.
"""

import PySimpleGUI as sg
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Excel file imported as a variable
df = pd.read_excel('test_data_set_sdv602_milestone_2.xlsx', sheet_name='Sheet1')

sg.theme('DarkBlack')

def Excel_Graph(Card_Name, Percentage_of_Decks): 
        """
        Plots graph from excel file. (Placeholder for Milestone 3)
        
        """
        plt.figure(figsize=(10.5, 6))
        plt.bar(df['Card_Name'], df['Percentage_of_Decks'])
        plt.xlabel("Card Name", weight='bold')
        plt.ylabel("Percentage of Decks", weight='bold')
        plt.title("Excel Graph Bar Chart", weight='bold')
        plt.plot()
        
        return plt.gcf()

def draw_figure(canvas, figure):
        """
        Function that uses a figure agg to draw the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

# Windows that displays the data for each colour combo in colour_combo_layout when button clicked. (DES Two)
def CCL_Azorius():
    """
    Function that opens Azorius window (White/Blue) when clicked in Colour Combo tab. 
    
    """
    layout = [[sg.Text("Top 10 Azorius Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Azorius Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Boros():
    """
    Function that opens Boros window (White/Red) when clicked in Colour Combo tab. 
    
    """
    layout = [[sg.Text("Top 10 Boros Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Boros Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Dimir():
    """
    Function that opens Dimir window (Blue/Black) when clicked in Colour Combo tab. 
    
    """
    layout = [[sg.Text("Top 10 Dimir Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Dimir Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Golgari():
    """
    Function that opens Golgari window (Black/Green) when clicked in Colour Combo tab.
    
    """
    layout = [[sg.Text("Top 10 Golgari Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Golgari Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Gruul():
    """
    Function that opens Grull window (Red/Green) when clicked in Colour Combo tab. 
    """
    layout = [[sg.Text("Top 10 Gruul Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Gruul Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Izzet():
    """
    Function that opens Izzet window (Blue/Red) when clicked in Colour Combo tab.
    
    """
    layout = [[sg.Text("Top 10 Izzet Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Izzet Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Orzhov():
    """
    Function that opens Orzhov window (White/Black) when clicked in Colour Combo tab.  
    
    """
    layout = [[sg.Text("Top 10 Orzhov Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Orzhov Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Rakdos():
    """
    Function that opens Rakdos window (Black/Red) when clicked in Colour Combo tab.  
    
    """
    layout = [[sg.Text("Top 10 Rakdos Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Rakdos Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Selesnya():
    """
    Function that opens Selesnya window (Green/White) when clicked in Colour Combo tab.  
    
    """
    layout = [[sg.Text("Top 10 Selesnya Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Selesnya Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CCL_Simic():
    """
    Function that opens Simic window (Blue/Green) when clicked in Colour Combo tab.  
    
    """
    layout = [[sg.Text("Top 10 Simic Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Simic Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

# Windows that displays the data for each colour in colour_layout when button clicked. (DES Three)
def CL_Multicolour():
    """
    Function that opens Multicolour window (any colour combo) when clicked in Colour tab.  
    
    """    
    layout = [[sg.Text("Top 10 Multicolour Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Multicolour Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CL_White():
    """
    Function that opens White Cards window when clicked in Colour tab. 
    
    """
    layout = [[sg.Text("Top 10 White Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 White Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CL_Red():
    """
    Function that opens Red Cards window when clicked in Colour tab.  
    
    """
    layout = [[sg.Text("Top 10 Red Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]
    
    window = sg.Window("Top 10 Red Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CL_Blue():
    """
    Function that opens Blue Cards window when clicked in Colour tab.  
    
    """
    layout = [[sg.Text("Top 10 Blue Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Blue Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CL_Green():
    """
    Function that creates Green Cards window when clicked in Colour tab.  
    
    """
    layout = [[sg.Text("Top 10 Green Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Green Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def CL_Black():
    """
    Function that opens Black Cards window when clicked in Colour tab.  
    
    """
    layout = [[sg.Text("Top 10 Black Cards", justification='center', size=(135,1))],
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
                sg.Button('Settings', size=(8, 1))]]

    window = sg.Window("Top 10 Black Cards", layout, modal=True, finalize=True)
    
    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # If send button clicked, print input to output.
        
    window.close()

def main():
    """
    Function that contains the Home/Main page that opens on startup
    
    """
    # Introduction / Home page.
    home_layout = [  
                    [sg.Text("Introduction", justification='center', size=(135,1))],
                    [sg.Text("Information about the application will be placed here, this is a placeholder.", size=(85,1))],
                    [sg.Button('EXIT', size=(8, 1)), sg.Button('Sign Out', size=(8, 1))]]

    # The first DES displays the top 10 cards in a grid (DES One).
    top_10_layout = [[sg.Text("Top 10 Cards", justification='center', size=(135,1))],
                    # Summery Information Placeholder
                    [sg.Text("Summery Information:")],
                    [sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                    # Canvas for graph
                    [sg.Canvas(size=(600, 600), key='-CANVAS-')],
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
                    sg.Button('Settings', size=(8, 1))]]

    # The second DES. (CCL_)
    colour_combo_layout = [
                    [sg.Button("Azorius", key="open_Azorius"),
                    sg.Button("Boros", key="open_Boros"),
                    sg.Button("Dimir", key="open_Dimir"),
                    sg.Button("Golgari", key="open_Golgari"),
                    sg.Button("Gruul", key="open_Gruul")],
                    [sg.Button("Izzet", key="open_Izzet"),
                    sg.Button("Orzhov", key="open_Orzhov"),
                    sg.Button("Rakdos", key="open_Rakdos"),
                    sg.Button("Selesnya", key="open_Selesnya"),
                    sg.Button("Simic", key="open_Simic")]]

    # The Third DES. (CL_)
    colour_layout = [[sg.Button("Multicolour", key="open_Multi"),
                    sg.Button("White", key="open_White"),
                    sg.Button("Red", key="open_Red")],
                    [sg.Button("Blue", key="open_Blue"),
                    sg.Button("Green", key="open_Green"),
                    sg.Button("Black", key="open_Black")]]

    # Putting the Home page and three DES pages into tabs. Calling tab_group in sg.Window() to display the tabs.
    tab_group = [[sg.TabGroup(
                    [[sg.Tab("Home", home_layout),
                    sg.Tab("Top 10 Cards", top_10_layout),
                    sg.Tab("Top 10 Cards for Each Colour Combo", colour_combo_layout),
                    sg.Tab("Top 10 Cards for Each Colour", colour_layout)]]
                )]]

    # Creates the Main/Home Window.
    window = sg.Window("Application", tab_group, use_default_focus=False, finalize=True)

    # Draws the graph to the canvas.
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))

    # Event Loop to process "events" and get the "values" of the inputs.
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):    # Closes window.
            break
        if event == "open_Azorius":     # Closes colour_combo_layout windows.
            CCL_Azorius()
        elif event == "open_Boros":
            CCL_Boros()
        elif event == "open_Dimir":
            CCL_Dimir()
        elif event == "open_Golgari":
            CCL_Golgari()
        elif event == "open_Gruul":
            CCL_Gruul()
        elif event == "open_Izzet":
            CCL_Izzet()
        elif event == "open_Orzhov":
            CCL_Orzhov()
        elif event == "open_Rakdos":
            CCL_Rakdos()
        elif event == "open_Selesnya":
            CCL_Selesnya()
        elif event == "open_Simic":
            CCL_Simic()
        elif event == "open_Multi":     # Closes colour_layout windows.
            CL_Multicolour()
        elif event == "open_White":
            CL_White()
        elif event == "open_Red":
            CL_Red()
        elif event == "open_Blue":
            CL_Blue()
        elif event == "open_Green":
            CL_Green()
        elif event == "open_Black":
            CL_Black()
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True)   # If send button clicked, print input to output.

    window.close()

if __name__ == "__main__":
    main()
    pass