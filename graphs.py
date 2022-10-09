"""
Issues(*) / ToDo(-):
    - Use """ """ comments
    
    - Swap Data Placeholders for excel data.
    - Present Data as graphs.
    
    * 'read_excel' not working properly (not importing data from excel file).
    * Cant display data within the window when opened.
    
"""

import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\xande\OneDrive\Documents\_Course_2022\_SDV602\SDV602_Project\test_data_set_sdv602_milestone_2.xlsx', sheet_name='Sheet1')
#print(df)

# plt.plot(df['Card_Name'], df['Percentage_of_Decks'])
# plt.xlabel('Card_Name')
# plt.ylabel('Percentage of Decks')
# plt.title('Test Excel Graph')

#plt.show()

def Excel_Graphs(**kwargs): 
    """
    
    """

    plt.bar(df['Card_Name'], df['Percentage_of_Decks'])

    plt.xlabel("Card Name")
    plt.ylabel("Percentage of Decks")
    plt.title("Bar Chart Example")

    plt.plot()
    
    return plt.gcf()

def show_figFunc(pFigureFunction, **kwargs):
    """
    Shows a figure
    
    """
    current_fig = fig_with_kwargs(pFigureFunction,**kwargs)
    plt.figure(current_fig.number)
    plt.show()

def fig_with_kwargs(pFigureFunction, **kwargs):
    """
    Returns a figure after applying the kwargs

    """
    kwarg_fig = None
    if kwargs :
        kwarg_fig = pFigureFunction(**kwargs)
    else:
        kwarg_fig = pFigureFunction()

    return kwarg_fig

if __name__ == "__main__":
    show_figFunc(Excel_Graphs)
    pass