import PySimpleGUI as sg

sg.theme('DarkBlack')

# introduction / Home page.
home_layout = [  
                [sg.Text("Introduction", justification='center', size=(85,1))],
                [sg.Button('Exit')]  ]

# The first DES 
top_50_layout = [  
                    [sg.Text("Top 50 Cards", justification='center', size=(85,1))],
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
                    [sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png"), 
                    sg.Image(filename="./images/Magic_card_back_small.png")],]

# The second DES
colour_layout = [   
                    [sg.Text('Some text on Row 1')],
                    [sg.Text('Enter something on Row 2'), sg.InputText()]]

# The Third DES
colour_combo_layout = [ 
                        [sg.Text('Some text on Row 1')],
                        [sg.Text('Enter something on Row 2'), sg.InputText()]]

# Putting the Home page and three DES pages into tabs
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
                    border_width=5
                )]
            ]

# Colour Combo Layouts (nested tabs in DES Two)
colour_combo_layout_Azorius = [
                                [sg.Text("Azorius", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Boros = [
                                [sg.Text("Boros", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Dimir = [
                                [sg.Text("Dimir", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Golgari = [
                                [sg.Text("Golgari", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Gruul = [
                                [sg.Text("Gruul", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Izzet = [
                                [sg.Text("Izzet", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Orzhov = [
                                [sg.Text("Orzhov", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Rakdos = [
                                [sg.Text("Rakdos", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Selesnya = [
                                [sg.Text("Selesnya", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

colour_combo_layout_Simic = [
                                [sg.Text("Simic", justification='center', size=(85,1))],
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")], 
                                [sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png"), 
                                sg.Image(filename="./images/Magic_card_back_small.png")]]

# Colour Combo Tab Group (nested tabs in DES Two)
colour_combo_layout_tab_group = [
                                    [sg.TabGroup(
                                        [[
                                            sg.Tab("Azorius", colour_combo_layout_Azorius),
                                            sg.Tab("Boros", colour_combo_layout_Boros),
                                            sg.Tab("Dimir", colour_combo_layout_Dimir),
                                            sg.Tab("Golgari", colour_combo_layout_Golgari),
                                            sg.Tab("Gruul", colour_combo_layout_Gruul),
                                            sg.Tab("Izzet", colour_combo_layout_Izzet),
                                            sg.Tab("Orzhov", colour_combo_layout_Orzhov),
                                            sg.Tab("Rakdos", colour_combo_layout_Rakdos),
                                            sg.Tab("Selesnya", colour_combo_layout_Selesnya),
                                            sg.Tab("Simic", colour_combo_layout_Simic)]],
                                        tab_location='centertop',
                                        title_color='White', 
                                        tab_background_color='purple',
                                        selected_title_color='Green',
                                        border_width=5
                                    )]
                                ]

# Create the Window
window = sg.Window("Application", tab_group)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED: # closes window
        break

window.close()