"""
This file plots the graphs for the GUI.

"""

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def Excel_Graph(Card_Name, Percentage_of_Decks, df): 
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