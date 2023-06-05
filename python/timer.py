"""This class has a timer to gather the
time needed for each sensor to scan each environments"""

import time
import subprocess

"""start and end variables to store the times"""
START_TIME = 0
END_TIME = 0


def start_time():
    """This function returns the start time"""
    return time.time()


def stop_time():
    """This function returns the stop time"""
    return time.time()


def write_file():
    """This function computes the difference between the
    start and stop time and writes it to a given text file"""
    time = END_TIME-START_TIME
    inputstring = input("Environment, sensor name: ")
    with open('ressources/time.txt', 'a') as f:
        print(time)
        f.writelines("\n"+str(inputstring)+" Time: "+str(time))
    f.close()


"""Command List, containing some commands needed to run the simulations
in different environments with different sensors(not all are included here)"""

COMMANDS = ["./Examples/Stereo-Inertial/stereo_inertial_euroc ./Vocabulary/ORBvoc.txt" +
            "./Examples/Stereo-Inertial/EuRoC.yaml ~/Datasets/EuRoc/V101" +
            "./Examples/Stereo-Inertial/EuRoC_TimeStamps/V102.txt dataset-V101_stereoi",
            "./Examples/Stereo/stereo_euroc ./Vocabulary/ORBvoc.txt ./Examples/Stereo/EuRoC.yaml" +
            "~/Datasets/EuRoc/V101 ./Examples/Stereo/EuRoC_TimeStamps/V102.txt dataset-V101_stereo",
            "./Examples/Monocular/mono_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular/EuRoC.yaml" +
            "~/Datasets/EuRoc/V102 ./Examples/Monocular/EuRoC_TimeStamps/V102.txt dataset-V102_mono",
            "./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.txt" +
            "./Examples/Monocular-Inertial/EuRoC.yaml ~/Datasets/EuRoc/V102" +
            "./Examples/Monocular-Inertial/EuRoC_TimeStamps/V102.txt dataset-V102_monoi",
            "./Examples/Stereo/stereo_euroc ./Vocabulary/ORBvoc.txt ./Examples/Stereo/EuRoC.yaml" +
            "~/Datasets/EuRoc/V102 ./Examples/Stereo/EuRoC_TimeStamps/V102.txt dataset-V102_stereo",
            "./Examples/Stereo-Inertial/stereo_inertial_euroc ./Vocabulary/ORBvoc.txt" +
            "./Examples/Stereo-Inertial/EuRoC.yaml ~/Datasets/EuRoc/V102" +
            "./Examples/Stereo-Inertial/EuRoC_TimeStamps/V102.txt dataset-V102_stereoi",
            "./Examples/Monocular/mono_euroc ./Vocabulary/ORBvoc.txt ./Examples/Monocular/EuRoC.yaml" +
            "~/Datasets/EuRoc/V103 ./Examples/Monocular/EuRoC_TimeStamps/V103.txt dataset-V103_mono",
            "./Examples/Monocular-Inertial/mono_inertial_euroc ./Vocabulary/ORBvoc.txt" +
            "./Examples/Monocular-Inertial/EuRoC.yaml ~/Datasets/EuRoc/V103" +
            "./Examples/Monocular-Inertial/EuRoC_TimeStamps/V103.txt dataset-V103_monoi",
            "./Examples/Stereo/stereo_euroc ./Vocabulary/ORBvoc.txt ./Examples/Stereo/EuRoC.yaml" +
            "~/Datasets/EuRoc/V103 ./Examples/Stereo/EuRoC_TimeStamps/V103.txt dataset-V103_stereo",
            "./Examples/Stereo-Inertial/stereo_inertial_euroc ./Vocabulary/ORBvoc.txt" +
            "./Examples/Stereo-Inertial/EuRoC.yaml ~/Datasets/EuRoc/V103" +
            "./Examples/Stereo-Inertial/EuRoC_TimeStamps/V103.txt dataset-V103_stereoi"
            ]

"""For loop to loop through the commands in the COMMANDS list"""
for i in COMMANDS:
    COMMAND = str(i)
    print("Start: "+COMMAND)

    """Start the timer(get the start time)"""
    START_TIME = start_time()

    """Call the command and pass the output lines
    through a pipe to be shown on the console"""
    PROCESS = subprocess.Popen(COMMAND, shell=True, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT, universal_newlines=True)

    for line in PROCESS.stdout:
        print(line.strip())

    PROCESS.communicate()

    """check if the command returned 0,
    if so the command was succesfully completely executed,
    the time stops and the file is written,
    else stop the time anyway and write the file,
    but tell the user that the command didnt finish correctly"""
    if PROCESS.returncode == 0:
        print("ok")
        END_TIME = stop_time()
        write_file()
    else:
        print("ok with Error")
        END_TIME = stop_time()
        write_file()