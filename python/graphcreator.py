"""Class graphcreator, responsible to create line/bar graphs for different use cases"""
import matplotlib.pyplot as plt
import divergence as d


calculator = d.DivergenceCalculator()

def kfbargraph(environment):
    """This function creates a bar graph with
    the keyframe percentages of every sensor
    in an environment"""

    left_coordinates= calculator.kfenvironment()
    heights=[20,40,80,100]
    bar_labels=['mono','monoi','stereo','stereoi']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.5,color=['red','black'])
    plt.grid(True)
    plt.xlabel('Sensors')
    plt.ylabel('KeyFrame percentage')
    plt.title(environment+" bar graph")
    plt.savefig(environment+"_bargraph.pdf")
    plt.show()

def kflinegraph(sensor,environmentname,values,environments):
    """This function creates a line graph with
    the keyframe percentage of a single sensor
    across multiple environments of the same type"""
    list=[]
    for i,value in enumerate(environments):
        if environmentname[:2] in value:
            list.append(value)
    y=values
    x=list
    plt.plot(x,y, color="red")
    plt.grid(True)
    plt.xlabel('Environments')
    plt.ylabel('KeyFrame divergence percentage')
    plt.title(sensor+" sensor line graph in the environments: "+tostring(list))
    plt.savefig(sensor+"_"+environments[0]+"_line.pdf")
    plt.show()

def tostring(list):
    """This function takes a list as parameter
    and outputs the elements separated by a comma"""
    result=""
    for i in enumerate(list):
        if i[0]==0:
            result=str(i[1])
        else:
            result= result +", "+ str(i[1])
    return result

