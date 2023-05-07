""""""

import customtkinter

import os
os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
os.environ['DISPLAY']=':1.0'
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("1000x1000")

def login():
    print("hfhj")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label= customtkinter.CTkLabel(master=frame,text="jfjfjf")
label.pack(pady=12, padx=10)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="user")
entry1.pack(pady=12, padx= 10)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="password",show="*")
entry2.pack(pady=12, padx= 10)

button= customtkinter.CTkButton(master=frame, text="login", command=login)
entry2.pack(pady=12, padx= 10)

root.mainloop()