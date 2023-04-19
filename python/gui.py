#Main Graphical User Interface

import PySimpleGUI as gui
import divergencecalculator as dc

title=gui.Text(text="Outputted Graph",font=('Arial Bold',20),size=18)
input=gui.Input('',enable_events=True, key='-INPUT-', font=('Arial Bold', 20), expand_x=True, justification='left')

layout=[[title],[gui.Text('Enter desired sensor'),input],[gui.Button("OK",key="-OK-")]]
realsize=(1100,800)


window= gui.Window("Sensors Benchmark Results",layout,size=realsize)

window.read()


#def getdivergence():




while True:
    event, values = window.read()
    if event == '-INPUT-':
        if values['-INPUT-'][-1] not in ('0123456789'):
            gui.popup("Only digits allowed")
            window['-INPUT-'].update(values['-INPUT-'][:-1])
    if event == gui.WIN_CLOSED or event == 'Exit':
      break




window.close()