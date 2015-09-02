from dataFunc import *
from linRegression import *

colourFirstFew = lambda plot: colourFirstFewMinR2(plot)

def colourFirstFewMinR2(plot):
    i = indexOfMaximalR2(plot) + 1
    colouredPlot = dataPlot( ([a + ["red"] for a in plot[:i]] + [a + ["black"] for a in plot[i:]] ) )
    return colouredPlot

def getInitialLine(plot):
    workingPlot = dataPlot(takeInitial(colourFirstFew(plot), lambda p: p[2]=="red"))
    return workingPlot

def dataAndrea(plot):
    try: return gradient(getInitialLine(plot))
    except: return "ERROR"

