"""kjfgjkfjk"""

import customtkinter
import main as m
import graphcreator as gc
import subprocess


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

main= m.Main()
root = customtkinter.CTk()

root.geometry("1000x1000")

def initialize():
    """fjjfej"""
    main.initializesensors("mono")
    main.initializesensors("monoi")
    main.initializesensors("stereo")
    main.initializesensors("stereoi")
    main.initializeenvironments("MH01","easy")
    label2= customtkinter.CTkLabel(master=frame,text= main.calculator.kfenvironmenttoString(main.calculator.kfenvironment()))
    label2.pack(pady=12, padx=10)
    gc.kfbargraph('MH01')
    path = 'bargraph.pdf'
    subprocess.Popen([path], shell=True)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame,text="KeyFrame Divergence of the MH01 environment")
label.pack(pady=12, padx=10)

button= customtkinter.CTkButton(master=frame, text="Get", command=initialize)
button.pack(pady=12, padx= 10)

root.mainloop()
"""
entry1= customtkinter.CTkEntry(master=frame, placeholder_text="user")
entry1.pack(pady=12, padx= 10)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="password",show="*")
entry2.pack(pady=12, padx= 10)
"""