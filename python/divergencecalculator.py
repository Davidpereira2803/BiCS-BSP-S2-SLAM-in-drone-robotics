"""This file contains every function needed"""
"""to extract the data from the provided text files and make some computations"""
import os
sensors = []
environments = {}


# This function takes a text file as input and converts it to a dictionnary
# where each key value pair represents a line of the file
def readfiles(file1):
    """Returns a dictionnary where the values represent a line in the file"""

    file1 = 'ressources/TextFiles/'+file1
    with open(file1, 'r') as ,f:
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

# Takes two environment names of different difficulty levels and one sensor as parameters and returns the key frame difference of the two environments sensor


def difficultylevelkfaccuracy(environmentname1, environmentname2, sensor):
    """Returns the difference of the kf percentage of two difficulties of a specific sensor"""
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
    for i in range(4):
        list1.append(difficultylevelkfaccuracy('MH01', 'MH05', sensors[i]))
    final['MH'] = list1
    for j in range(4):
        list2.append(difficultylevelkfaccuracy('V101', 'V102', sensors[j]))
    final['V1'] = list2
    return final


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


print('4 2')
addenvironments('MH01', 'easy')
addenvironments('MH05', 'difficult')
addenvironments('V101', 'easy')
addenvironments('V102', 'medium')
addenvironments('V103', 'difficult')
addsensors('mono')
addsensors('monoi')
addsensors('stereo')
addsensors('stereoi')
print(allkfdivergence())
# alldivergencedictsplitter(alldivergence())
#
# print(difficultyleveldivergence())
# difficultyleveldivergence('MH')
# difficultyleveldivergence('V1')
# print(difficultylevelkfaccuracy('MH01','MH05','mono'))
print(alldifficultylevelkfaccuracy())
