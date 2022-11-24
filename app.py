"""
Issues(*) / ToDo(-):
    - Write ReadMe
    - Home page needs to be populated.
    - DES windows needs to be populated.
    - DES two and three needs images for buttons and buttons need repositioning.
   
    - Settings page needs to be created.
    - Zoom in and zoom out buttons need to function correctly.
    - Chat needs to function correctly.

"""

# Imported Modules
import PySimpleGUI as sg
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Imported Files
from view.figures import Excel_Graph
from view.des_view import DesView
from view.user_login_view import LoginView

# Imported Functions for DES Two (CCL_)
from controller.DES2_CCL_button_layouts import CCL_Azorius
from controller.DES2_CCL_button_layouts import CCL_Boros
from controller.DES2_CCL_button_layouts import CCL_Dimir
from controller.DES2_CCL_button_layouts import CCL_Golgari
from controller.DES2_CCL_button_layouts import CCL_Gruul
from controller.DES2_CCL_button_layouts import CCL_Izzet
from controller.DES2_CCL_button_layouts import CCL_Orzhov
from controller.DES2_CCL_button_layouts import CCL_Rakdos
from controller.DES2_CCL_button_layouts import CCL_Simic
from controller.DES2_CCL_button_layouts import CCL_Selesnya

# Imported Functions for DES Three (CL_)
from controller.DES3_CL_button_layouts import CL_Multicolour
from controller.DES3_CL_button_layouts import CL_White
from controller.DES3_CL_button_layouts import CL_Red
from controller.DES3_CL_button_layouts import CL_Green
from controller.DES3_CL_button_layouts import CL_Blue
from controller.DES3_CL_button_layouts import CL_Black

# Excel file imported as a variable
df = pd.read_excel('test_data_set_sdv602_milestone_2.xlsx', sheet_name='Sheet1')    

sg.theme('DarkBlack')


def draw_figure(canvas, figure):
        """
        Function that uses a figure agg to draw the graph (figure) to the canvas.
        
        """
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
        return figure_canvas_agg

def main():
    """
    Opens on startup.
    
    Function that contains:
    
        Layouts:
        - Home / Main page layout       (home_layout)             
        - DES One layout                (top_10_layout)
        - DES Two (CCL_) layout         (colour_combo_layout)   
        - DES Three (CL_) layout        (colour_layout)
        - Putting layouts into Tabs     (tab_group)
        
        Functionality:
        - Window for Application        (window)
        - Draw graph to canvas          (draw_figure)
        
        Event loop:
        - Exit button closes window when clicked.
        - Opens DES Two (CCL_) windows when button clicked.     x 10
        - Opens DES Three (CL_) windows when button clicked.    x 6
        - Send button prints input to output in chat box.
    """
    
    home_layout = [  
                    [sg.Text("Introduction", justification='center', size=(135,1))],
                    [sg.Text("Information about the application will be placed here, this is a placeholder.", size=(85,1))],
                    [sg.Button('EXIT', size=(8, 1)), sg.Button('Sign Out', size=(8, 1))]]

    top_10_layout = [[sg.Text("Top 10 Cards", justification='center', size=(135,1))],
                    # Summery Information Placeholder
                    [sg.Text("Summery Information:")],
                    [sg.Text("Information about the DES will be placed here, this is a placeholder.", size=(85,1))],
                    # Canvas for graph
                    [sg.Canvas(size=(600, 620), key='-CANVAS-')],
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

    colour_layout = [[sg.Button("Multicolour", key="open_Multi"),
                    sg.Button("White", key="open_White"),
                    sg.Button("Red", key="open_Red")],
                    [sg.Button("Blue", key="open_Blue"),
                    sg.Button("Green", key="open_Green"),
                    sg.Button("Black", key="open_Black")]]

    tab_group = [[sg.TabGroup(
                    [[sg.Tab("Home", home_layout),
                    sg.Tab("Top 10 Cards", top_10_layout),
                    sg.Tab("Top 10 Cards for Each Colour Combo", colour_combo_layout),
                    sg.Tab("Top 10 Cards for Each Colour", colour_layout)]]
                )]]

    window = sg.Window("Application", tab_group, use_default_focus=False, finalize=True)

    draw_figure(window['-CANVAS-'].TKCanvas, Excel_Graph(df['Card_Name'], df['Percentage_of_Decks'], df))

    # Event Loop to process "events" and get the "values" of the inputs.
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'EXIT'):    # Closes windows
            break
        # Opens colour_combo_layout windows
        elif event == "open_Azorius":     
            CCL_Azorius(df, draw_figure)
        elif event == "open_Boros":
            CCL_Boros(df, draw_figure)
        elif event == "open_Dimir":
            CCL_Dimir(df, draw_figure)
        elif event == "open_Golgari":
            CCL_Golgari(df, draw_figure)
        elif event == "open_Gruul":
            CCL_Gruul(df, draw_figure)
        elif event == "open_Izzet":
            CCL_Izzet(df, draw_figure)
        elif event == "open_Orzhov":
            CCL_Orzhov(df, draw_figure)
        elif event == "open_Rakdos":
            CCL_Rakdos(df, draw_figure)
        elif event == "open_Selesnya":
            CCL_Selesnya(df, draw_figure)
        elif event == "open_Simic":
            CCL_Simic(df, draw_figure)
        # Opens colour_layout windows
        elif event == "open_Multi":     
            CL_Multicolour(df, draw_figure)
        elif event == "open_White":
            CL_White(df, draw_figure)
        elif event == "open_Red":
            CL_Red(df, draw_figure)
        elif event == "open_Blue":
            CL_Blue(df, draw_figure)
        elif event == "open_Green":
            CL_Green(df, draw_figure)
        elif event == "open_Black":
            CL_Black(df, draw_figure)
        # Send Button
        if event == 'SEND':
            query = values['-QUERY-'].rstrip()
            print('User 1: {}'.format(query), flush=True)   

    window.close()

if __name__ == "__main__":
    
    # login_view = LoginView()
    # login_view.set_up_layout()
    # login_view.render()
    # login_view.accept_input()

    main()
    pass