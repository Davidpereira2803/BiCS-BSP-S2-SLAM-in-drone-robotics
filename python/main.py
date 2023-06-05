"""Main python class, which adds up the required functions to use in the gui"""

import kfdivergence as d
import timedivergence as td


class Main:
    """Class main, which has a varible calculator to acces the
    function in the class DivergenceCalculator()"""

    calculator = d.KFDivergenceCalculator()
    tcalculator = td.TimeDivergenceCalculator()

    def initialize_sensors(self, sensor):
        """Add sensors to the sensor list"""
        self.calculator.add_sensors(sensor)

    def initialize_environments(self, environment, difficulty):
        """Add environments to the environment dictionnary"""
        self.calculator.add_environments(environment, difficulty)

    def get_sensors(self):
        """Access the sensors list"""
        return self.calculator.sensors

    def get_environments(self):
        """Access the environments dictionnary"""
        return self.calculator.environments

    def remove_sensors(self, sensor):
        """Remove the specific sensor passed
        as parameter from the list"""
        for i in self.calculator.sensors:
            if(sensor == i):
                self.calculator.sensors.remove(i)
        return self.calculator.sensors

    def remove_environment(self, environment):
        """Remove the environment passed as parameter
        from the environment dictionnary"""
        return self.calculator.environments.pop(environment)

    def get_environments_by_name(self, name):
        """Returns a list containing the sensor kf divergence by
        difficulty increasing of the environment name passed as parameter"""
        return self.calculator.sensor_kf_by_difficulty_increasing(name)