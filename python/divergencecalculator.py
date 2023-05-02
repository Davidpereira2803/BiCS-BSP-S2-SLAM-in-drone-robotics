"""This file contains every function needed"""
"""to extract the data from the provided text files and make some computations"""
import matplotlib.pyplot as plt
sensors = []
environments = {}


# This function takes a text file as input and converts it to a dictionnary
# where each key value pair represents a line of the file
def readfiles(file1):
    """Returns a dictionnary where the values represent a line in the file"""

    file1 = 'ressources/TextFiles/'+file1
    with open(file1, 'r') as f:
        content = f.readlines()
    # print(content1)
    endcontent = {}
    for i in range(len(content)):
        newcontent = content[i].strip()
        for j in range(len(newcontent)):
            endcontent[j] = newcontent.split(' ')
    return endcontent


# This function counts the keyframes captured by the SLAM and compares it to the Ground Truth keyframes count
def keyframedivergence(sensor, groundtruth):
    """Returns the percentage of keyframes captured by the selected sensor"""
    sensorkf = len(sensor)
    groundtruthkf = len(groundtruth)
    return str(round((sensorkf/groundtruthkf)*100, 2))+"%"

# This function will check every file that is in the given folder(saved in a textfile)
# and compute the keyframedivergence and give a dictionnary where the key is the environment followed by the sensor
# and the value is the result of the keyframedivergence function
def allkfdivergence():
    """Return a dictionnary with all the keyframes percentages"""
    final = {}
    environmentsnames = list(environments.keys())
    for j in range(len(environmentsnames)):
        for i in range(len(sensors)):
            file1 = 'kf_dataset-'+environmentsnames[j]+'_'+sensors[i]+'.txt'
            file2 = environmentsnames[j]+'_GT.txt'
            final[environmentsnames[j]+'_'+sensors[i]
                  ] = (keyframedivergence(readfiles(file1), readfiles(file2)))
    return final

def kfenvironment(environment):
    allkfdivergencelist=list(allkfdivergence().values())
    final=[]
    for i in range(len(allkfdivergencelist)):
        final.append(float(allkfdivergencelist[i][:len(allkfdivergencelist[i])-1]))
    return final

# Takes two environment names of different difficulty levels and one sensor as parameters and returns the key frame difference of the two environments sensor


def difficultylevelkfaccuracy(environmentname1, environmentname2, sensor):
    """Returns the difference of the kf percentage of two difficulties of a specific sensor"""
    result=0
    allkfdivergencelist = allkfdivergence()
    for i in range(len(allkfdivergencelist.keys())):
        if (str(environmentname1+'_'+sensor) == str(list(allkfdivergencelist.keys())[i])):
            result = abs(round(float(allkfdivergencelist[environmentname1+'_'+sensor][:len(allkfdivergencelist[environmentname1+'_'+sensor])-1])-float(
                allkfdivergencelist[environmentname2+'_'+sensor][:len(allkfdivergencelist[environmentname2+'_'+sensor])-1]), 4))
    return result


def alldifficultylevelkfaccuracy():
    """returns a dict of all the kf differences of all environnments"""
    list1 = []
    list2 = []
    final = {}
    for j in range(len(sensors)):
        list1.append(difficultylevelkfaccuracy('V101', 'V102', sensors[j]))
    for j in range(len(sensors)):
        list2.append(difficultylevelkfaccuracy('V102', 'V103', sensors[j]))
    final['V1'] = list1

    return list1


def kfgraph():
    x=[89.84,90.62,89.06,89.84]
    y=[2,4,6,1]
    plt.plot(x,y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple line graph")
    plt.savefig("plot.pdf")

def kfbargraph(environment):
    left_coordinates=kfenvironment(environment)
    heights=[20,40,80,100]
    bar_labels=['mono','monoi','stereo','stereoi']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.3,color=['red','black'])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple bar graph")
    plt.savefig("bargraph.pdf")

def test():
    left_coordinates=[1.4,2.5,3.0,4.9,5.7]
    heights=[10,20,30,15,40]
    bar_labels=['One','Two','Three','Four','Five']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.3,color=['red','black'])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple bar graph")
    plt.savefig("bargraph.pdf")

# check if sensor is mono, monoi, stereo, steroi, RGB
def addsensors(sensor):
    """adds a new sensor to the sensors list"""
    if (sensor == 'mono' or sensor == 'monoi' or sensor == 'stereo' or sensor == 'stereoi' or sensor == 'RGB'):
        sensors.append(sensor)

# implement check if difficulty is easy medium or difficulty
def addenvironments(environment, difficulty):
    """adds a new environment to the environments list"""
    if (difficulty == 'easy' or difficulty == 'medium' or difficulty == 'difficult'):
        environments[environment] = difficulty



#addenvironments('MH01', 'easy')
#addenvironments('MH05', 'difficult')
addenvironments('MH01', 'easy')

addsensors('mono')
addsensors('monoi')
addsensors('stereo')
addsensors('stereoi')
#print(allkfdivergence())
#print(difficultyleveldivergence())
# difficultyleveldivergence('MH')
# difficultyleveldivergence('V1')
#print(difficultylevelkfaccuracy('V101','V102','mono'))
#print(alldifficultylevelkfaccuracy().values())
#kfbargraph("MH01")
print(kfenvironment("MH01"))
kfbargraph("MH01")

