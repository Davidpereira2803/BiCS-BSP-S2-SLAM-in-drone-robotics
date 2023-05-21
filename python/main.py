"""Main python class, which adds up the required functions to use in the gui"""

import divergence as d

class Main:
    """Class main, which has a varible calculator to acces the
    function in the class DivergenceCalculator()"""

    calculator = d.DivergenceCalculator()

    def initializesensors(self,sensor):
        """Add sensors to the sensor list"""
        self.calculator.addsensors(sensor)

    def initializeenvironments(self,environment,difficulty):
        """Add environments to the environment dictionnary"""
        self.calculator.addenvironments(environment,difficulty)
    
    def getsensors(self):
        """Access the sensors list"""
        return self.calculator.sensors

    def getenvironments(self):
        """Access the environments dictionnary"""
        return self.calculator.environments

    def removesensors(self,sensor):
        """Remove the specific sensor passed
        as parameter from the list"""
        for i in self.calculator.sensors:
            if(sensor==i):
                self.calculator.sensors.remove(i)
        return self.calculator.sensors
    
    def removeenvironment(self,environment):
        """Remove the environment passed as parameter
        from the environment dictionnary"""
        return self.calculator.environments.pop(environment)
    
    def getenvironmentsbyname(self,name):
        """Returns a list containing the sensor kf divergence by
        difficulty increasing of the environment name passed as parameter"""
        return self.calculator.sensorkfbydifficultyincreasing(name)

