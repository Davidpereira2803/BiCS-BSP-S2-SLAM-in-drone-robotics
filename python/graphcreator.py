import matplotlib.pyplot as plt
import divergence as d


calculator = d.DivergenceCalculator()

def kfbargraph(environment):
    """jfjd"""
    left_coordinates= calculator.kfenvironment()
    heights=[20,40,80,100]
    bar_labels=['mono','monoi','stereo','stereoi']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.5,color=['red','black'])
    plt.xlabel('Sensors')
    plt.ylabel('KeyFrame percentage')
    plt.title(environment+" bar graph")
    plt.savefig(environment+"_bargraph.pdf")

def kflinegraph(sensor,values,environments):
    """jhgjh"""
    y=[values[0],values[1],values[2]]
    x=[environments[0],environments[1],environments[2]]
    plt.plot(x,y)
    plt.xlabel('Environments')
    plt.ylabel('KeyFrame divergence percentage')
    plt.title(sensor+" sensor line graph in the environments: "+str(environments))
    plt.savefig(sensor+"_"+environments[0]+"_line.pdf")

#kflinegraph("mono",[90,80,70],["MH01","MH03","MH05"])
