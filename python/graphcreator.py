import matplotlib.pyplot as plt
import divergencecalculator as dc
import divergence as d


calculator = d.DivergenceCalculator()

def kfgraph():
    x=[89.84,90.62,89.06,89.84]
    y=[2,4,6,1]
    plt.plot(x,y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple line graph")
    plt.savefig("plot.pdf")

def kfbargraph(environment):
    left_coordinates= calculator.kfenvironment()
    heights=[20,40,80,100]
    bar_labels=['mono','monoi','stereo','stereoi']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.5,color=['red','black'])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple bar graph")
    plt.savefig("bargraph.pdf")

def test():
    left_coordinates=[1.4,2.5,3.0,4.9,5.7]
    heights=[10,20,30,15,40]
    bar_labels=['One','Two','Three','Four','Five']
    plt.bar(left_coordinates,heights,tick_label=bar_labels,width=0.3,color=['red','black'])
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("A simple bar graph")
    plt.savefig("bargraph.pdf")