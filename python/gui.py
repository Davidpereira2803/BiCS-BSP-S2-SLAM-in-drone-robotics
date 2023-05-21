"""GUI class, which is responsible for the graphical
user interface and the interactions"""
import subprocess
import customtkinter
import main as m
import graphcreator as gc

customtkinter.set_appearance_mode("gray")
customtkinter.set_default_color_theme("blue")

main= m.Main()
root = customtkinter.CTk()

root.geometry("1000x1000")

def autoinitialize():
    """This function auto initializes the
    lists with some examples"""
    main.initializesensors("mono")
    main.initializesensors("monoi")
    main.initializesensors("stereo")
    main.initializesensors("stereoi")
    main.initializeenvironments("MH01","easy")
    main.initializeenvironments("MH03","medium")
    main.initializeenvironments("MH05","difficult")
    print(main.getenvironments())
    showsensorsandenvironments()

def kfbargraphcalculator():
    """This function creates a bargraph of the
    environment typed in the environment field"""
    gc.kfbargraph(environmententry.get())
    resultlabel.configure(text="Key Frame percentages: "
    + main.calculator.kfenvironmenttostring(main.calculator.kfenvironment()))
    path = environmententry.get()+'_bargraph.pdf'
    subprocess.Popen([path], shell=True)
    showsensorsandenvironments()
    linegraph()

def linegraph():
    """This function creates a line graph
    of the sensor currently in the sensors field"""
    gc.kflinegraph(sensorentry.get(),environmententry.get(),[90,80,70],list(main.getenvironments().keys()))
    path = sensorentry.get()+'_'+environmententry.get()+'_line.pdf'
    subprocess.Popen([path], shell=True)
    showsensorsandenvironments()

def addsensor():
    """Adds the sensor written in the sensor entry to the list"""
    main.initializesensors(sensorentry.get())
    print(main.getsensors())
    showsensorsandenvironments()

def removesensor():
    """Removes the sensor written in the sensor entry from the list"""
    main.removesensors(sensorentry.get())
    print(main.getsensors())
    showsensorsandenvironments()

def addenvironment():
    """Adds the environment written in the environment/difficulty entry to the dictionnary"""
    main.initializeenvironments(environmententry.get(),environmentdifentry.get())
    print(main.getenvironments())
    showsensorsandenvironments()

def removeenvironment():
    """Removes the environment written in the environment entry from the dictionnary"""
    main.removeenvironment(environmententry.get())
    print(main.getenvironments())
    showsensorsandenvironments()

def showsensorsandenvironments():
    """Shows the sensors/environments in a label"""
    sensors= str(main.getsensors())
    enviroments= str(main.getenvironments())
    result="You added the following sensors: "+sensors+"\n"+"You added the following environments: "+enviroments
    resultlabel1.configure(text=result)

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5, padx=5, fill="both", expand=True)

outputframe = customtkinter.CTkFrame(master=root)
outputframe.pack(pady=5, padx=5, fill="both", expand=True)

autoinitializebutton= customtkinter.CTkButton(master=frame, text="Auto initialize", command=autoinitialize)
autoinitializebutton.pack(pady=5, padx= 5)

sensorentry= customtkinter.CTkEntry(master=frame,placeholder_text="Sensor")
sensorentry.pack(pady=5, padx=5)
sensorbutton= customtkinter.CTkButton(master=frame, text="Add Sensor", command=addsensor)
sensorbutton.pack(pady=5, padx= 5)
removesensor= customtkinter.CTkButton(master=frame, text="Remove Sensor", command=removesensor)
removesensor.pack(pady=5, padx= 5)

environmententry= customtkinter.CTkEntry(master=frame,placeholder_text="Environment Name")
environmententry.pack(pady=5, padx=5)
environmentdifentry= customtkinter.CTkEntry(master=frame,placeholder_text="Environment Difficulty")
environmentdifentry.pack(pady=5, padx=5)
environmentbutton= customtkinter.CTkButton(master=frame, text="Add Environment",
                                        command=addenvironment)
environmentbutton.pack(pady=5, padx= 5,anchor=customtkinter.CENTER)
removeenvironment= customtkinter.CTkButton(master=frame, text="Remove Environment",
                                        command=removeenvironment)
removeenvironment.pack(pady=5, padx= 5)

resultlabel= customtkinter.CTkLabel(master=frame,text="Result")
resultlabel.pack(pady=12, padx=10)

label= customtkinter.CTkLabel(master=outputframe,
                            text="KeyFrame Divergence of the "+ "MH01" + " environment")
label.pack(pady=1, padx=10)

button= customtkinter.CTkButton(master=outputframe, text="Get", command=kfbargraphcalculator)
button.pack(pady=5, padx= 10)

resultlabel1= customtkinter.CTkLabel(master=outputframe,text="Empty")
resultlabel1.pack(pady=12, padx=10)

root.mainloop()
