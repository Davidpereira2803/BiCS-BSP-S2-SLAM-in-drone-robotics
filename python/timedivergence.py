"""This class contains the methods needed to extract the information
from the text documents and compute multiple divergence between sensors/environments"""

import kfdivergence as kfd


class TimeDivergenceCalculator:
    """Class DivergenceCalculator, with a sensors list and environments dictionnary,
    which contains the environment and its difficulty"""
    kfdcalculator = kfd.KFDivergenceCalculator()
    sensors = kfdcalculator.sensors
    environments = kfdcalculator.environments

    def add_sensors(self, sensor):
        """adds a new sensor to the sensors list"""
        self.kfdcalculator.add_sensors(sensor)

    def add_environments(self, environment, difficulty):
        """adds a new environment to the environments list"""
        self.kfdcalculator.add_environments(environment, difficulty)

    def timetodict(self):
        """This function extracts the information of the time.txt file
        it returns a dictionnary containing the environment+sensor as key
        and the time needed to perform the scanning in seconds as value"""
        file = 'ressources/time.txt'
        with open(file, 'r') as f:
            content = f.readlines()
            final = {}
        for indexi, elementi in enumerate(content):
            newcontent = content[indexi].strip()
            endcontent = newcontent.split(' ')
            final[endcontent[0]+endcontent[1]] = endcontent[3]
        return final

    def timedict(self):
        """Returns a reduced time dictionnary with only the time
        from the environments and sensors in the attributes sensors and environments"""
        times = self.timetodict()
        result = {}
        for i, element in enumerate(times.keys()):
            for i, environment in enumerate(self.environments):
                for i, sensor in enumerate(self.sensors):
                    if element[:4] == environment and element[5:] == sensor:
                        result[element] = times[element]
        return result

    def time_of_sensor(self, sensor, dict):
        """This function takes a sensor and the dictionnary of the time
        as parameter and retruns a list of the times in all the environments
        of the given sensor"""
        result = []
        for index, element in enumerate(dict.keys()):
            if(sensor == element[5:]):
                result.append(dict[element])
        return result

    def time_of_environment(self, environment, dict):
        """This function takes a environment and the dictionnary of the time
        as parameter and retruns a list of the times for each sensor in that
        environment"""
        result = []
        for index, element in enumerate(dict.keys()):
            if(environment == element[:4]):
                result.append(dict[element])
        return result

    def time_difference_per_environments_percentage(self, environment1, environment2, computation):
        """This function takes one sensor as parameter and
        computes the sensors time differences percentage between both environments"""
        result = {}
        time_1 = self.time_of_environment(environment1, self.timedict())
        time_2 = self.time_of_environment(environment2, self.timedict())
        if computation == "greater":
            try:
                for i, element in enumerate(time_1):
                    result[self.sensors[i]] = (self.percentage_greater(
                        float(time_1[i]), float(time_2[i])))
                return result
            except IndexError:
                print("time_1 and time_2 have different lengths")
        elif computation == "less":
            try:
                for i, element in enumerate(time_1):
                    result[self.sensors[i]] = (self.percentage_less(
                        float(time_1[i]), float(time_2[i])))
                return result
            except IndexError:
                print("time_1 and time_2 have different lengths")

    def percentage_greater(self, time_1, time_2):
        """time_1 > time_2,
        it returns the percentage which time_1 is greater than time_2"""
        return ((time_1-time_2)/time_2)*100

    def percentage_less(self, time_1, time_2):
        """time_1 < time_2,
        it returns the percentage which time_1 is less than time_2"""
        return ((time_2-time_1)/time_2)*100