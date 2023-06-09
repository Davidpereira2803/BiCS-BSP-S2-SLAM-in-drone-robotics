"""This class contains the methods needed to extract the information
from the text documents and compute multiple divergence between sensors/environments"""

class KFDivergenceCalculator:
    """Class DivergenceCalculator, with a sensors list and environments dictionnary,
    which contains the environment and its difficulty"""
    sensors = []
    environments = {}

    def add_sensors(self, sensor):
        """adds a new sensor to the sensors list"""
        condition1=(sensor == 'mono' or sensor == 'monoi'
        or sensor == 'stereo' or sensor == 'stereoi' or sensor == 'RGB')
        condition2=not(sensor in self.sensors)
        if (condition1 and condition2):
            self.sensors.append(sensor)

    def add_environments(self, environment, difficulty):
        """adds a new environment to the environments list"""
        if (difficulty == 'easy' or difficulty == 'medium' or difficulty == 'difficult'):
            self.environments[environment] = difficulty

    def readfiles(self, file1):
        """Returns a dictionnary where the values represent a line in the file"""
        file1 = 'ressources/TextFiles/'+file1
        with open(file1, 'r') as f:
            content = f.readlines()
        endcontent = {}
        for indexi, elementi in enumerate(content):
            newcontent = content[indexi].strip()
            for indexj, elementj in enumerate(newcontent):
                endcontent[indexj] = newcontent.split(' ')
        return endcontent

    def allkf_divergence(self):
        """Return a dictionnary with all the keyframes percentages"""
        final = {}
        environmentsnames = list(self.environments.keys())
        for i, elementj in enumerate(environmentsnames):
            for j, elementi in enumerate(self.sensors):
                file1 = 'kf_dataset-'+elementj+'_'+elementi+'.txt'
                file2 = elementj+'_GT.txt'
                final[elementj+'_'+elementi
                      ] = (self.keyframe_divergence(self.readfiles(file1),
                                                    self.readfiles(file2)))
        return final

    def keyframe_divergence(self, sensor, groundtruth):
        """Returns the percentage of keyframes captured by the selected sensor"""
        sensorkf = len(sensor)
        groundtruthkf = len(groundtruth)
        return round((sensorkf/groundtruthkf)*100, 2)

    def kf_environment(self, environment):
        """Returns a list of only the values of the kf divergences from the actual
        sensors in the lists for the environment passed as parameter"""
        allkfdivergencelist = list(self.allkf_divergence().keys())
        final = []
        for i, element in enumerate(allkfdivergencelist):
            for i, sensor in enumerate(self.sensors):
                if element[:4] == environment and element[5:] == sensor:
                    final.append(self.allkf_divergence()[element])
        return final

    def kf_sensor(self, sensor, environmentname):
        """Returns a list of key frame divergence percentage for
        a specific sensor in a sepcific environment name"""
        allkfdivergencelist = list(self.allkf_divergence().keys())
        final = []
        for i, element in enumerate(allkfdivergencelist):
            for i, environment in enumerate(self.environments):
                if (element[:2] == environmentname and
                element[5:] == sensor and element[:4] == environment):
                    final.append(self.allkf_divergence()[element])
        return final

    def kf_environment_tostring(self, kf):
        """Returns a string with the kf divergences in percentage"""
        result = ""
        for i, element in enumerate(kf):
            if(i < len(kf)-1):
                result = result+str(element)+"%, "
            else:
                result = result+str(element)+"%"
        return result

    def sensor_kf_by_difficulty_increasing(self, name):
        """Returns a list of environments per name, given as parameter"""
        result = []
        for i, element in enumerate(self.environments):
            if(element[:2] == name):
                result.append(element)
        return result