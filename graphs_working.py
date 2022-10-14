"""
Issues(*) / ToDo(-):
    
    - Swap Data Placeholders for excel data.
    * Cant display data within the window when opened.
    
"""
import PySimpleGUI as sg
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

df = pd.read_excel('test_data_set_sdv602_milestone_2.xlsx', sheet_name='Sheet1')
#print(df)

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

if __name__ == "__main__":
    testing_graphs_2()
    pass