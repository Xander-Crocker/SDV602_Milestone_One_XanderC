"""
Issues(*) / ToDo(-):
    - Home page needs to be populated.
    - DES two and three needs images for buttons and needs repositioning.
    - Use """ """ comments
    
    - Swap Data Placeholders for excel data.
    * Cant display graph data within the window when opened.
    
"""

import graphs as ce 

import PySimpleGUI as sg
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

sg.theme('DarkBlack')

# Excel file
df = pd.read_excel('test_data_set_sdv602_milestone_2.xlsx', sheet_name='Sheet1')
# print(df)

# Puts Excel_Graphs function from graphs.py into a variable 
data = ce.Excel_Graphs()

def testing_graphs_2():
    
    def Excel_Graphs(Card_Name, Percentage_of_Decks): 
        """
        plots graph from excel file.
        
        """
        plt.figure(figsize=(10, 5))
        plt.bar(df['Card_Name'], df['Percentage_of_Decks'])
        plt.xlabel("Card Name")
        plt.ylabel("Percentage of Decks")
        plt.title("Bar Chart Example")
        plt.plot()
        
        return plt.gcf()

    layout = [[sg.Text('Bar Graph')],
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                [sg.Exit()]]

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    window = sg.Window('PySimpleGUI + MatPlotLib Bar Graphs', layout, finalize=True, )

    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graphs(df['Card_Name'], df['Percentage_of_Decks']))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()


# -----------------------------

# Windows that displays the data for each colour combo in colour_combo_layout when button clicked (DES Two)
def Azorius():
    layout = [[sg.Text("Azorius Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"),  
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"),  
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Azorius Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Boros():
    layout = [[sg.Text("Boros Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Boros Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Dimir():
    layout = [[sg.Text("Dimir Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Dimir Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Golgari():
    layout = [[sg.Text("Golgari Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Golgari Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Gruul():
    layout = [[sg.Text("Gruul Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Gruul Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Izzet():
    layout = [[sg.Text("Izzet Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Izzet Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Orzhov():
    layout = [[sg.Text("Orzhov Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Orzhov Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Rakdos():
    layout = [[sg.Text("Rakdos Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Rakdos", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Selesnya():
    layout = [[sg.Text("Selesnya Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Selesnya Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Simic():
    layout = [[sg.Text("Simic Top 10", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Simic Top 10", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

# Windows that displays the data for each colour in colour_layout when button clicked (DES Three)
def Multicolour():
    layout = [[sg.Text("Top 10 Multicolour Commanders", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Top 10 Multicolour Commanders", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def White():
    layout = [[sg.Text("Top 10 White Commanders", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Top 10 White Commanders", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Red():
    layout = [[sg.Text("Top 10 Red Commanders", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Top 10 Red Commanders", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Blue():
    layout = [[sg.Text("Top 10 Blue Commanders", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Top 10 Blue Commanders", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Green():
    layout = [[sg.Text("Top 10 Green Commanders", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"),
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Top 10 Green Commanders", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def Black():
    layout = [[sg.Text("Top 10 Black Commanders", justification='center', size=(100,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                [sg.Image(filename="./images/Magic_card_back.png"), # Placeholder images
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")], 
                [sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png"), 
                sg.Image(filename="./images/Magic_card_back.png")],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(90, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(90, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    window = sg.Window("Top 10 Black Commanders", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # EXECUTE THE COMMAND
        
    window.close()

# main page that opens on startup
def main():
    # introduction / Home page
    home_layout = [  
                    [sg.Text("Introduction", justification='center', size=(85,1))],
                    [sg.Text("Information about the application will be placed here, this is a placeholder.", size=(85,1))],
                    [sg.Button('Excel_Graph', key=('open_Excel_Graph_2')),],
                    [sg.Button('EXIT', size=(8, 1)), sg.Button('Sign Out', size=(8, 1))]]

    # The first DES displays the top 50 cards in a grid (DES One)
    top_50_layout = [[sg.Text("Top 50 Cards", justification='center', size=(85,1))],
                    # Summery Information Placeholder
                    [sg.Text("Summery Information:")],
                    [sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                    # Data placeholder
                    [sg.Image(filename="./images/Magic_card_back_small.png"), # Placeholder images
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],
                    [sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],
                    [sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],
                    [sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],
                    [sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],
                    #Chat 
                    [sg.Text('Output', size=(40, 1))],
                    [sg.Output(size=(70, 3), font=('Helvetica 10')),
                    # Zoom Buttons
                    sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                    [sg.Text('Input', size=(40, 1))],
                    [sg.Multiline(size=(70, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                    sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                    #Settings Button
                    sg.Button('Settings', size=(8, 1))]]

    # The second DES 
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

    # The Third DES 
    colour_layout = [[sg.Button("Multicolour", key="open_Multi"),
                    sg.Button("White", key="open_White"),
                    sg.Button("Red", key="open_Red")],
                    [sg.Button("Blue", key="open_Blue"),
                    sg.Button("Green", key="open_Green"),
                    sg.Button("Black", key="open_Black")]]

    # Putting the Home page and three DES pages into tabs. Calling tab_group in sg.Window() to display the tabs
    tab_group = [[sg.TabGroup(
                    [[sg.Tab("Home", home_layout),
                    sg.Tab("Top 50", top_50_layout),
                    sg.Tab("Colour Cobos Top 10", colour_combo_layout),
                    sg.Tab("Top 10 Commanders", colour_layout)]]
                )]]

    # Create the Window
    window = sg.Window("Application", tab_group, use_default_focus=False, finalize=True)

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):    # closes window
            break
        if event == "open_Azorius":     # closes colour_combo_layout windows
            Azorius()
        elif event == "open_Boros":
            Boros()
        elif event == "open_Dimir":
            Dimir()
        elif event == "open_Golgari":
            Golgari()
        elif event == "open_Gruul":
            Gruul()
        elif event == "open_Izzet":
            Izzet()
        elif event == "open_Orzhov":
            Orzhov()
        elif event == "open_Rakdos":
            Rakdos()
        elif event == "open_Selesnya":
            Selesnya()
        elif event == "open_Simic":
            Simic()
        elif event == "open_Multi": # closes colour_layout windows
            Multicolour()
        elif event == "open_White":
            White()
        elif event == "open_Red":
            Red()
        elif event == "open_Blue":
            Blue()
        elif event == "open_Green":
            Green()
        elif event == "open_Black":
            Black()
        elif event == "open_Excel_Graph_2":     # Test Data Excel Graph
            testing_graphs_2()
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output

    window.close()

if __name__ == "__main__":
    main()
    show_figFunc(testing_graphs_2)
    pass
    dictionary_of_figure_functions = {'TEST EXCEL GRAPH':(ce.Excel_Graphs,{})}
    testing_graphs_2(dictionary_of_figure_functions)