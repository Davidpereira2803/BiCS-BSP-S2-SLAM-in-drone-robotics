import numpy
import matplotlib

sensors=[]
environments={}


#This function takes a text file as input and converts it to a dictionnary
#where each key value pair represents a line of the file
def readfiles(file1):
    file1= 'D:\TextFiles/'+file1

    with open(file1,'r') as f:
        content = f.readlines()
    #print(content1)

    endcontent={}
    for i in range(len(content)):
        newcontent=content[i].strip()
        for j in range(len(newcontent)):
            endcontent[j]=newcontent.split(' ')

    return endcontent


#This function counts the keyframes captured by the SLAM and compares it to the Ground Truth keyframes count
def keyframedivergence(sensor, groundtruth):
    sensorkf=len(sensor)
    groundtruthkf=len(groundtruth)
    return str(round((sensorkf/groundtruthkf)*100,2))+"%"


#This function will check every file that is in the given folder(saved in a textfile)
#and compute the keyframedivergence and give a dictionnary where the key is the environment followed by the sensor
#and the value is the result of the keyframedivergence function
def allkfdivergence():
    final={}
    environmentsnames=list(environments.keys())
    for j in range(len(environmentsnames)):
        for i in range(len(sensors)):
            file1='kf_dataset-'+environmentsnames[j]+'_'+sensors[i]+'.txt'
            file2=environmentsnames[j]+'_GT.txt'
            final[environmentsnames[j]+'_'+sensors[i]]=(keyframedivergence(readfiles(file1),readfiles(file2)))
    return final

#Takes the first name of the type of the environment as a parameter
# and returns a list containing the difference of percentage with climbing difficulty by 1 in a same environment type
def difficultyleveldivergence(environment):
    if(environment=='MH' or environment=='V1' or environment=='V2' ):
        allkfdivergencelist=allkfdivergence()
        percentage=[]
        final=[]
        for i in range(len(allkfdivergencelist.keys())):
            if(environment in str(list(allkfdivergencelist.keys())[i])):
                percentage.append(allkfdivergencelist[list(allkfdivergencelist.keys())[i]])
        for j in range(len(percentage)):
            if(j<len(percentage)-4):
                result=round(abs(float(percentage[j][:len(percentage[j])-1])-float(percentage[j+4][:len(percentage[j+4])-1])),6)
                final.append(result)
        print(final)

#Takes two environment names of different difficulty levels and one sensor as parameters and returns the key frame difference of the two environments sensor
def difficultylevelkfaccuracy(environmentname1, environmentname2,sensor):
    allkfdivergencelist=allkfdivergence()
    for i in range(len(allkfdivergencelist.keys())):
            if(str(environmentname1+'_'+sensor) == str(list(allkfdivergencelist.keys())[i])):
                result=abs(round(float(allkfdivergencelist[environmentname1+'_'+sensor][:len(allkfdivergencelist[environmentname1+'_'+sensor])-1])-float(allkfdivergencelist[environmentname2+'_'+sensor][:len(allkfdivergencelist[environmentname2+'_'+sensor])-1]),4))
    return result

def alldifficultylevelkfaccuracy():
    difficultylevelkfaccuracy('MH01','MH03','mono')



#check if sensor is mono, monoi, stereo, steroi, RGB
def addsensors(sensor):
    if(sensor=='mono'or sensor=='monoi'or sensor=='stereo' or sensor=='stereoi' or sensor=='RGB'):
        sensors.append(sensor)

#implement check if difficulty is easy medium or difficult
def addenvironments(environment,difficulty):
    if(difficulty=='easy'or difficulty=='medium' or difficulty=='difficult'):
        environments[environment]=difficulty



print('4 2')
addenvironments('MH01','easy')
addenvironments('MH05','difficult')
addenvironments('V101','easy')
addenvironments('V102','medium')
addenvironments('V103','difficult')
addsensors('mono')
addsensors('monoi')
addsensors('stereo')
addsensors('stereoi')
print(allkfdivergence())
#alldivergencedictsplitter(alldivergence())
#
# print(difficultyleveldivergence())
difficultyleveldivergence('MH')
#difficultyleveldivergence('V1')
print(difficultylevelkfaccuracy('V101','V102','mono'))
