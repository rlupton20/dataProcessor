from dataFunc import *

def averageTuples(rule, tuples):
    return (1/len(tuples)*sum([rule(p) for p in tuples]))

def getR2(plot):
    xbar = averageTuples( lambda p: p[0], plot)
    ybar = averageTuples( lambda p: p[1], plot)
    xybar = averageTuples( lambda p: p[0]*p[1], plot)
    x2bar = averageTuples( lambda p: p[0]*p[0], plot)
    y2bar = averageTuples( lambda p: p[1]*p[1], plot)
    r2 = ((xybar - xbar*ybar)*(xybar - xbar*ybar))/((x2bar - xbar*xbar)*(y2bar - ybar*ybar))
    return r2

def gradient(plot):
    xbar = averageTuples( lambda p: p[0], plot)
    ybar = averageTuples( lambda p: p[1], plot)
    xybar = averageTuples( lambda p: p[0]*p[1], plot)
    x2bar = averageTuples( lambda p: p[0]*p[0], plot)
    y2bar = averageTuples( lambda p: p[1]*p[1], plot)
    gradient = (xybar - xbar*ybar)/(x2bar - xbar*xbar)
    return gradient

def intercept(plot):
    xbar = averageTuples( lambda p: p[0], plot)
    ybar = averageTuples( lambda p: p[1], plot)
    return (ybar - gradient(plot)*xbar)

def attachR2(plot):
    newPlot = dataPlot([list(i) for i in plot])    # Weird object referencing makes this odd copy necessary
    try:
        newPlot[0].append(0)
        newPlot[1].append(0)
        for i in range(2, len(newPlot)):
            newPlot[i].append(getR2(dataPlot(plot[0:(i+1)])))
    except:
        print("Error: data set too small")
    return newPlot

def indexOfMaximalR2(plot):
    workingPlot = attachR2(plot)
    R2s = [pt.pop() for pt in workingPlot]
    return R2s.index(max(R2s))
