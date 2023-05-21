"""This class has a timer to gather the
time needed for each sensor to scan each environments"""

import time

"""start and end variables to store the times"""
start=0
end=0

def starttime():
    """This function returns the start time"""
    return time.time()

def stoptime():
    """This function returns the stop time"""
    return time.time()


def writefile():
    """This function computes the difference between the
    start and stop time and writes it to a given text file"""
    time=end-start
    sensor=input("Sensor name: ")
    environment=input("Environment name: ")
    with open('ressources/time.txt','a') as f:
        print(time)
        f.writelines("\n"+str(environment)+", "+str(sensor)+" Time: "+str(time))
    f.close()

start=starttime()
input("Stop timer")
end=stoptime()
writefile()
