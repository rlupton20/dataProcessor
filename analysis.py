from dataFunc import *
from linRegression import *

colourFirstFew = lambda plot: colourFirstFewMinR2(plot)
#colourFirstFew = lambda plot: colourFirstFewNN(plot, 10, 8, 3/4)

def colourFirstFewMinR2(plot):
    i = indexOfMaximalR2(plot) + 1
    colouredPlot = dataPlot( ([a + ["red"] for a in plot[:i]] + [a + ["black"] for a in plot[i:]] ) )
    return colouredPlot

def colourFirstFewNN(plot, tol1, tol2, few):
    maxNeigh = dimPlot(nearNeighboursPlot(plot, tol1, tol2), 1)
    initial = takeInitial(plot.listOfTuples(), lambda p: nearNeighbours(plot, p, tol1, tol2) < few*maxNeigh )
    colouredPlot = dataPlot( ([a + ["red"] for a in initial] + [a + ["black"] for a in plot[len(initial):]] ) )
    return colouredPlot

def getInitialLine(plot):
    workingPlot = dataPlot(takeInitial(colourFirstFew(plot), lambda p: p[2]=="red"))
    return workingPlot

def dataAndrea(plot):
    try: return gradient(getInitialLine(plot))
    except: return "ERROR"

