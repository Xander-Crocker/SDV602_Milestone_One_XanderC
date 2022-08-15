import PySimpleGUI as sg

sg.theme('DarkBlack')   # Add a touch of color

# All the stuff inside your window.
home_layout = [  
                [sg.Text('Introduction')],
                [sg.Button('Exit')]  ]

top_50_layout = [  
                    [sg.Text('Top 50 Cards')],
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
                    sg.Image(filename="./images/Magic_card_back_small.png")],[sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],[sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],[sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],]

colour_layout = [   
                    [sg.Text('Some text on Row 1')],
                    [sg.Text('Enter something on Row 2'), sg.InputText()]]

colour_combo_layout = [ 
                        [sg.Text('Some text on Row 1')],
                        [sg.Text('Enter something on Row 2'), sg.InputText()]]

tab_group = [ 
                [sg.TabGroup(
                    [[
                        sg.Tab("Home", home_layout),
                        sg.Tab("Top 50", top_50_layout),
                        sg.Tab("Colours Top 10", colour_layout),
                        sg.Tab("Colour Cobos Top 10", colour_combo_layout)]],
                        tab_location='centertop',
                        title_color='White', 
                        tab_background_color='purple',
                        selected_title_color='Green',
                        border_width=5)
                ]
            ]

# Create the Window
window = sg.Window("Application", tab_group)
#margins=(300,250)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break

window.close()