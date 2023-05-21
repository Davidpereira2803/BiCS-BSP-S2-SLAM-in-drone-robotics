"""This class contains the methods needed to extract the information
from the text documents and compute multiple divergence between sensors/environments"""

class DivergenceCalculator:
    """Class DivergenceCalculator, with a sensors list and environments dictionnary,
    which contains the environment and its difficulty"""
    sensors=[]
    environments ={}

    def addsensors(self,sensor):
        """adds a new sensor to the sensors list"""
        if ((sensor == 'mono' or sensor == 'monoi' or sensor == 'stereo' or sensor == 'stereoi' or sensor == 'RGB') and not(sensor in self.sensors)):
            self.sensors.append(sensor)

    def addenvironments(self,environment, difficulty):
        """adds a new environment to the environments list"""
        if (difficulty == 'easy' or difficulty == 'medium' or difficulty == 'difficult'):
            self.environments[environment] = difficulty

    def readfiles(self,file1):
        """Returns a dictionnary where the values represent a line in the file"""
        file1 = 'ressources/TextFiles/'+file1
        with open(file1, 'r') as f:
            content = f.readlines()
        endcontent = {}
        for indexi,elementi in enumerate(content):
            newcontent = content[indexi].strip()
            for indexj,elementj in enumerate(newcontent):
                endcontent[indexj] = newcontent.split(' ')
        return endcontent
    
    def keyframedivergence(self,sensor, groundtruth):
        """Returns the percentage of keyframes captured by the selected sensor"""
        sensorkf = len(sensor)
        groundtruthkf = len(groundtruth)
        return str(round((sensorkf/groundtruthkf)*100, 2))+"%"
    
    def allkfdivergence(self):
        """Return a dictionnary with all the keyframes percentages"""
        final = {}
        environmentsnames = list(self.environments.keys())
        for i,elementj in enumerate(environmentsnames):
            for j,elementi in enumerate(self.sensors):
                file1 = 'kf_dataset-'+elementj+'_'+elementi+'.txt'
                file2 = elementj+'_GT.txt'
                final[elementj+'_'+elementi
                     ] = (self.keyframedivergence(self.readfiles(file1), self.readfiles(file2)))
        return final
    
    def kfenvironment(self):
        """Returns a list of only the values of the kf divergences"""
        allkfdivergencelist=list(self.allkfdivergence().values())
        final=[]
        for i, element in enumerate(allkfdivergencelist):
            final.append(float(element[:len(element)-1]))
        return final
    
    def kfenvironmenttostring(self, kf):
        """Returns a string with the kf divergences in percentage"""
        result=""
        for i, element in enumerate(kf):
            if(i<len(kf)-1):
                result= result+str(element)+"%, "
            else:
                result= result+str(element)+"%"
        return result

    def sensorkfbydifficultyincreasing(self,name):
        """Returns a list of environments per name, given as parameter"""
        result=[]
        for i, element in enumerate(self.environments):
            if(element[:2]==name):
                result.append(element)
        return result
    
    def timetolist(self):
        """This function extracts the information of the time.txt file
        it returns a dictionnary containing the environment+sensor as key
        and the time needed to perform the scanning in seconds as value"""
        file='ressources/time.txt'
        with open(file, 'r') as f:
            content = f.readlines()
            final={}
        for indexi,elementi in enumerate(content):
            if(indexi!=0):
                newcontent = content[indexi].strip()
                endcontent = newcontent.split(' ')
                final[endcontent[0]+endcontent[1]]=endcontent[3]
        return final

