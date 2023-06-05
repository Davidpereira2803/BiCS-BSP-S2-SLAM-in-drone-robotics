"""GUI class, which is responsible for the graphical
user interface and the interactions"""

import customtkinter
import main as m
import graphcreator


class Actions():
    """Class containing the functions triggered by the buttons"""

    gc = graphcreator.GraphCreator()

    def autoinitialize(self):
        """This function auto initializes the
        lists with some examples"""
        main.initialize_sensors("mono")
        main.initialize_sensors("monoi")
        main.initialize_sensors("stereo")
        main.initialize_sensors("stereoi")
        main.initialize_environments("MH01", "easy")
        main.initialize_environments("MH03", "medium")
        print(main.get_environments())
        print(main.get_sensors())
        self.showsensorsandenvironments()

    def getkfdivergence(self):
        """Get the Key Frame divergence of the selected environment"""
        if(environmententry.get() in main.get_environments()):
            string=main.calculator.kf_environment_tostring(
            main.calculator.kf_environment(environmententry.get()))
            kfresultlabel.configure(text=str(environmententry.get())+" Key Frame percentages: "+string)

    def kf_bargraphcalculator(self):
        """This function creates a bargraph of the
        environment typed in the environment field"""
        self.gc.kf_bargraph(environmententry.get())
        self.showsensorsandenvironments()

    def kf_linegraph(self):
        """This function creates a line graph
        of the sensor currently in the sensors field"""
        self.gc.kf_linegraph(sensorentry.get(), environmententry.get()[:2])
        self.showsensorsandenvironments()

    def gettimedifference(self):
        """Get time difference"""
        if(environmententry.get() in main.get_environments(
        ) and environmententry2.get() in main.get_environments()):
            string=str(main.tcalculator.time_difference_per_environments_percentage(
            environmententry.get(), environmententry2.get(), computationentry.get()))
            timeresultlabel.configure(text=str(environmententry.get())+
            " "+str(environmententry2.get())+" time difference percentages: "+string)

    def time_linegraph(self):
        """Create time line graph of one sensor over multiple environments"""
        if(sensorentry.get() in main.get_sensors()):
            self.gc.time_linegraph(sensorentry.get())
            self.showsensorsandenvironments()

    def time_bargraph(self):
        """Create time bar graph of 2 environments"""
        if(environmententry.get() in main.get_environments()
        and environmententry2.get() in main.get_environments()):
            self.gc.time_bargraph(environmententry.get(
            ), environmententry2.get(), computationentry.get())
            self.showsensorsandenvironments()

    def addsensor(self):
        """Adds the sensor written in the sensor entry to the list"""
        main.initialize_sensors(sensorentry.get())
        print(main.get_sensors())
        self.showsensorsandenvironments()

    def removesensor(self):
        """Removes the sensor written in the sensor entry from the list"""
        main.remove_sensors(sensorentry.get())
        print(main.get_sensors())
        self.showsensorsandenvironments()

    def addenvironment(self):
        """Adds the environment written in the environment/difficulty entry to the dictionnary"""
        main.initialize_environments(
            environmententry.get(), environmentdifentry.get())
        print(main.get_environments())
        self.showsensorsandenvironments()

    def removeenvironment(self):
        """Removes the environment written in the environment entry from the dictionnary"""
        main.remove_environment(environmententry.get())
        print(main.get_environments())
        self.showsensorsandenvironments()

    def showsensorsandenvironments(self):
        """Shows the sensors/environments in a label"""
        sensors = str(main.get_sensors())
        enviroments = str(main.get_environments())
        result = "You added the following sensors: "+sensors+"\n" + \
            "\n"+"You added the following environments: "+enviroments
        listlabel.configure(text=result)

    def openwindow(self):
        """Open InformationWindow"""
        window =InformationWindow(root)
        window.grab_set()

class InformationWindow(customtkinter.CTkToplevel):
    """Second UI window which has some information on how to use the app"""
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry('1000x210')
        self.title('Information Window')
        self.textbox=customtkinter.CTkTextbox(self,width=1000,height=210,corner_radius=1)
        self.textbox.grid(row=0,column=0)
        self.textbox.insert("0.0", "Auto initialize: Initializes the sensors and the environments (4 sensors, 2 environments)."+"\n")
        self.textbox.insert("2.0", "Add/Remove Sensor/Environment: Add and remove sensors or environments from the app(Note: Environments need difficulty level)\n")
        self.textbox.insert("4.0", "Second environment entry and computation entry are needed for the time difference between 2 environments. The Computation can be either greater or less.\n")
        self.textbox.insert("6.0", "KF Bar Graph: Create a Bar Graph of the KF divergence of all sensors currently in the app from the environment in the environment entry.\n")
        self.textbox.insert("8.0", "KF Line Graph: Create a Line Graph of the sensor in the sensor entry, over all the environments of the name written in the environment entry. Example:MH01-> all environments starting with MH\n")
        self.textbox.insert("10.0", "Get Divergence: Compute the Key Frame divergence of all sensors, for environment in the environment entry. \n")
        self.textbox.insert("12.0", "Time Bar Graph: Create a Graph of the time difference percentage between two environments.\n")
        self.textbox.insert("14.0", "Time Line Graph: Create a Line Graph of the time needed for the sensor in the entry in the different environments. \n")
        self.textbox.insert("16.0", "Get Time: Compute the time difference percentage of the sensors between two environments passed in both entries with the computation.\n")
        self.textbox.insert("18.0", "Note: To create the Graphs the entries must be filled in correctly with the desired information.\n")
        
"""Custom Tkinter interface"""
customtkinter.set_appearance_mode("gray")
customtkinter.set_default_color_theme("blue")

action = Actions()
main = m.Main()
root = customtkinter.CTk()

root.geometry("1000x1000")  
root.title("SLAM Sensor Benchmark")

"""Main frame of the UI"""
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=5, padx=5, fill="both", expand=True)

"""Second frame containing get buttons"""
buttonframe = customtkinter.CTkFrame(master=root)
buttonframe.pack(pady=5, padx=5, fill="both", expand=True)

"""Autoinitialize"""
autoinitializebutton = customtkinter.CTkButton(
    master=frame, text="Auto initialize", command=action.autoinitialize)
autoinitializebutton.pack(pady=5, padx=5)
autoinitializebutton.place(x=425, y=20)

"""Sensor Text Field, add/remove buttons"""
sensorentry = customtkinter.CTkEntry(master=frame, placeholder_text="Sensor")
sensorentry.pack(pady=5, padx=5)
sensorentry.place(x=425, y=50)
addsensor = customtkinter.CTkButton(
    master=frame, text="Add Sensor", command=action.addsensor)
addsensor.pack(pady=5, padx=5)
addsensor.place(x=425, y=80)
removesensor = customtkinter.CTkButton(
    master=frame, text="Remove Sensor", command=action.removesensor)
removesensor.pack(pady=5, padx=5)
removesensor.place(x=425, y=110)

"""Environment/Difficulty Text Field, add/remove buttons"""
environmententry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Environment Name")
environmententry.pack(pady=5, padx=5)
environmententry.place(x=425, y=140)
environmentdifentry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Environment Difficulty")
environmentdifentry.pack(pady=5, padx=5)
environmentdifentry.place(x=425, y=170)
addenvironment = customtkinter.CTkButton(master=frame, text="Add Environment",
                                        command=action.addenvironment)
addenvironment.pack(pady=5, padx=5, anchor=customtkinter.CENTER)
addenvironment.place(x=425, y=200)
removeenvironment = customtkinter.CTkButton(master=frame, text="Remove Environment",
                                            command=action.removeenvironment)
removeenvironment.pack(pady=5, padx=5)
removeenvironment.place(x=425, y=230)
"""Second Environment and computation for time comparison"""
environmententry2 = customtkinter.CTkEntry(
    master=frame, placeholder_text="Environment Name")
environmententry2.pack(pady=5, padx=5)
environmententry2.place(x=580, y=140)
computationentry = customtkinter.CTkEntry(
    master=frame, placeholder_text="Computation")
computationentry.pack(pady=5, padx=5)
computationentry.place(x=580, y=170)

"""Result labels for kf and time"""
kfresultlabel = customtkinter.CTkLabel(master=frame, text="KF-Results")
kfresultlabel.pack(pady=12, padx=10)
kfresultlabel.place(x=50, y=315)
timeresultlabel = customtkinter.CTkLabel(master=frame, text="Time-Results")
timeresultlabel.pack(pady=12, padx=10)
timeresultlabel.place(x=50, y=350)

"""Get buttons for Key Frame data"""
kfbutton = customtkinter.CTkButton(
    master=buttonframe, text="Get Environment Key Frame Divergence", command=action.getkfdivergence)
kfbutton.pack(pady=5, padx=10)
kfbutton.place(x=650, y=80)
kfbargraph_button = customtkinter.CTkButton(
    master=buttonframe, text="KF Bar Graph", command=action.kf_bargraphcalculator)
kfbargraph_button.pack(pady=5, padx=10)
kfbargraph_button.place(x=200, y=80)
kflinegraph_button = customtkinter.CTkButton(
    master=buttonframe, text="KF Line Graph", command=action.kf_linegraph)
kflinegraph_button.pack(pady=5, padx=10)
kflinegraph_button.place(x=425, y=80)

"""Get buttons for time data"""
timebutton = customtkinter.CTkButton(
    master=buttonframe, text="Get Time Difference between 2 environments", command=action.gettimedifference)
timebutton.pack(pady=5, padx=10)
timebutton.place(x=650, y=140)
timebargraph_button = customtkinter.CTkButton(
    master=buttonframe, text="Time Bar Graph", command=action.time_bargraph)
timebargraph_button.pack(pady=5, padx=10)
timebargraph_button.place(x=200, y=140)
timelinegraph_button = customtkinter.CTkButton(
    master=buttonframe, text="Time Line Graph", command=action.time_linegraph)
timelinegraph_button.pack(pady=5, padx=10)
timelinegraph_button.place(x=425, y=140)

"""Label displaying the added sensors/environments"""
listlabel = customtkinter.CTkLabel(master=frame, text="Empty")
listlabel.pack(pady=12, padx=10, anchor=customtkinter.CENTER)
listlabel.place(x=270, y=400)

"""Buttons to open Information Window"""
info_button= customtkinter.CTkButton(master=buttonframe,text="Open Information Window",command=action.openwindow)
info_button.pack(pady=5, padx=10)
info_button.place(x=412, y=200)

root.mainloop()