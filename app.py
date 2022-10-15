"""
Issues(*) / ToDo(-):
    - Home page needs to be populated.
    - DES two and three needs images for buttons and buttons need repositioning.
    - 
"""

import PySimpleGUI as sg
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

sg.theme('DarkBlack')

# Excel file imported as a variable
df = pd.read_excel('test_data_set_sdv602_milestone_2.xlsx', sheet_name='Sheet1')

# Windows that displays the data for each colour combo in colour_combo_layout when button clicked (DES Two)
def CCL_Azorius():
    """
    Function for Colour Combo Window for Azorius (White/Blue)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Azorius Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Azorius Window", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Boros():
    """
    Function for Colour Combo Window for Boros (White/Red)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Boros Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Boros Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Dimir():
    """
    Function for Colour Combo Window for Dimir (Blue/Black)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Dimir Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Dimir Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Golgari():
    """
    Function for Colour Combo Window for Golgari (Black/Green)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Golgari Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Golgari Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Gruul():
    """
    Function for Colour Combo Window for Grull (Red/Green)
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Gruul Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Gruul Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Izzet():
    """
    Function for Colour Combo Window for Izzet (Blue/Red)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Izzet Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Izzet Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Orzhov():
    """
    Function for Colour Combo Window for Orzhov (White/Black)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Orzhov Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Orzhov Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Rakdos():
    """
    Function for Colour Combo Window for Rakdos (Black/Red)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Rakdos Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Rakdos", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Selesnya():
    """
    Function for Colour Combo Window for Selesnya (Green/White)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Selesnya Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Selesnya Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CCL_Simic():
    """
    Function for Colour Combo Window for Simic (Blue/Green)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Simic Top 10", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Simic Top 10", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

# Windows that displays the data for each colour in colour_layout when button clicked (DES Three)
def CL_Multicolour():
    """
    Function for Colour Window for Multicolour (all colours)
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Top 10 Multicolour Commanders", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Top 10 Multicolour Commanders", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CL_White():
    """
    Function for Colour Window for White Cards
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Top 10 White Commanders", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Data placeholder
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Top 10 White Commanders", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CL_Red():
    """
    Function for Colour Window for Red Cards
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Top 10 Red Commanders", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                # Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                # Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Top 10 Red Commanders", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CL_Blue():
    """
    Function for Colour Window for Blue Cards
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Top 10 Blue Commanders", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Top 10 Blue Commanders", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CL_Green():
    """
    Function for Colour Window for Green Cards
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Top 10 Green Commanders", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Top 10 Green Commanders", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # print input to output
        
    window.close()

def CL_Black():
    """
    Function for Colour Window for Black Cards
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    layout = [[sg.Text("Top 10 Black Commanders", justification='center', size=(125,1))],
                # Summery Information Placeholder
                [sg.Text("Summery Information:"),
                sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                # Canvas for graph
                [sg.Canvas(size=(700, 600), key='-CANVAS-')],
                #Chat 
                [sg.Text('Output', size=(40, 1))],
                [sg.Output(size=(115, 3), font=('Helvetica 10')),
                # Zoom Buttons
                sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                [sg.Text('Input', size=(40, 1))],
                [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
                sg.Button('SEND', bind_return_key=True, size=(8, 1)), 
                #Settings Button
                sg.Button('Settings', size=(8, 1))]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg
    
    window = sg.Window("Top 10 Black Commanders", layout, modal=True, finalize=True)
    choice = None
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))
    
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True) # EXECUTE THE COMMAND
        
    window.close()

def main():
    """
    Function that contains the Main page that opens on startup
    
    """
    def Excel_Graph(Card_Name, Percentage_of_Decks): 
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
    
    # introduction / Home page
    home_layout = [  
                    [sg.Text("Introduction", justification='center', size=(125,1))],
                    [sg.Text("Information about the application will be placed here, this is a placeholder.", size=(85,1))],
                    [sg.Button('EXIT', size=(8, 1)), sg.Button('Sign Out', size=(8, 1))]]

    # The first DES displays the top 10 cards in a grid (DES One)
    top_10_layout = [[sg.Text("Top 10 Cards", justification='center', size=(125,1))],
                    # Summery Information Placeholder
                    [sg.Text("Summery Information:")],
                    [sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                    # Canvas for graph
                    [sg.Canvas(size=(600, 600), key='-CANVAS-')],
                    #Chat 
                    [sg.Text('Output', size=(40, 1))],
                    [sg.Output(size=(115, 3), font=('Helvetica 10')),
                    # Zoom Buttons
                    sg.Button('Zoom In', size=(8, 1)), sg.Button('Zoom Out', size=(8, 1))],
                    [sg.Text('Input', size=(40, 1))],
                    [sg.Multiline(size=(115, 2), enter_submits=False, key='-QUERY-', do_not_clear=False),
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
                    sg.Tab("Top 10", top_10_layout),
                    sg.Tab("Colour Cobos Top 10", colour_combo_layout),
                    sg.Tab("Top 10 For Each Colour", colour_layout)]]
                )]]
    
    def draw_figure(canvas, figure):
        """
        Function that draws the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

    # Create the Window
    window = sg.Window("Application", tab_group, use_default_focus=False, finalize=True)
    
    # Draws the graph to the canvas
    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks']))

    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):    # closes window
            break
        if event == "open_Azorius":     # closes colour_combo_layout windows
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
        elif event == "open_Multi": # closes colour_layout windows
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
            print('User 1: {}'.format(query), flush=True) # print input to output

    window.close()

if __name__ == "__main__":
    main()
    pass