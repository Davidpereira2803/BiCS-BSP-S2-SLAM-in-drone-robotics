"""fff"""

import divergence as d

class Main:
    """hffbh"""

    calculator = d.DivergenceCalculator()

    def initializesensors(self,sensor):
        """fjknfjn"""
        self.calculator.addsensors(sensor)

    def initializeenvironments(self,environment,difficulty):
        """fjhjfj"""
        self.calculator.addenvironments(environment,difficulty)
    
    def getsensors(self):
        """ff"""
        return self.calculator.sensors

    def getenvironments(self):
        """ff"""
        return self.calculator.environments

    def removesensors(self,sensor):
        """ff"""
        for i in self.calculator.sensors:
            if(sensor==i):
                self.calculator.sensors.remove(i)
        return self.calculator.sensors
    
    def removeenvironment(self,environment):
        """ff"""
        return self.calculator.environments.pop(environment)
    
    def getenvironmentsbyname(self,name):
        """hfhfhf"""
        return self.calculator.sensorkfbydifficultyincreasing(name)

