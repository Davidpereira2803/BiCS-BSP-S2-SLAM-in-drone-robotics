"""Class graphcreator, responsible to create line/bar graphs for different use cases"""

import math
import matplotlib.pyplot as plt
import kfdivergence as kfd
import timedivergence as td


class GraphCreator:
    """Class which is responsible for creating graphs"""
    
    kfcalculator = kfd.KFDivergenceCalculator()
    tcalculator = td.TimeDivergenceCalculator()

    def kf_bargraph(self, environment):
        """This function creates a bar graph with
        the keyframe percentages of every sensor
        in an environment"""
        heights = self.kfcalculator.kf_environment(environment)
        bar_labels = self.kfcalculator.sensors
        plt.bar(bar_labels, heights, width=0.5, color=['blue', 'black'])
        plt.grid(True)
        plt.xlabel('Sensors')
        plt.ylabel('KeyFrame percentage')
        plt.title(environment+" bar graph")
        plt.savefig(environment+"_bargraph.pdf")
        plt.show()

    def kf_linegraph(self, sensor, environmentname):
        """This function creates a line graph with
        the keyframe percentage of a single sensor
        across multiple environments of the same type"""
        list = []
        for i, value in enumerate(self.kfcalculator.environments):
            if environmentname[:2] in value:
                list.append(value)
        y = self.kfcalculator.kf_sensor(sensor, environmentname)
        x = list
        plt.plot(x, y, color="red")
        plt.grid(True)
        plt.xlabel('Environments')
        plt.ylabel('KeyFrame divergence percentage')
        plt.title(sensor+" sensor line graph in the environments: " +
                  self.tostring(list))
        plt.savefig(sensor+"_"+environmentname+"_line.pdf")
        plt.show()

    def time_linegraph(self, sensor):
        """This function creates a line graph with the time difference
        of a sensor in different environments"""
        values = (self.tcalculator.time_of_sensor(
            sensor, self.tcalculator.timedict()))
        x = self.tcalculator.environments.keys()
        y = []
        for i, value in enumerate(values):
            y.append(round(float(value), 3))
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Environments')
        plt.ylabel('Time in seconds')
        plt.title(sensor)
        plt.savefig(sensor+"_timeline.pdf")
        plt.show()

    def time_bargraph(self, environment1, environment2, computation):
        """The function creates a bar graph showing the time difference percentage
        of the sensors between both environments"""
        value = self.tcalculator.time_difference_per_environments_percentage(
            environment1, environment2, computation)
        bar_labels = self.tcalculator.sensors
        plt.bar(bar_labels, value.values(), width=0.5, color=['blue', 'black'])
        plt.grid(True)
        plt.xlabel('Sensors')
        plt.ylabel('Time difference percentage')
        plt.title(environment1+" "+environment2+" "+computation+" bar graph")
        plt.savefig(environment1+"_"+environment2+"_timebargraph.pdf")
        plt.show()

    def tostring(self, list):
        """This function takes a list as parameter
        and outputs the elements separated by a comma"""
        result = ""
        for i in enumerate(list):
            if i[0] == 0:
                result = str(i[1])
            else:
                result = result + ", " + str(i[1])
        return result