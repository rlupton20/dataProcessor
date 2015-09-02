import re
import itertools

class dataSet:
    def __init__(self):
        self.name = "Dataset"
        self.raw_dataLines = []

    def openCSV(self, filename):
        dataFile = open(filename, 'r')
        self.raw_dataLines = self.__CSVcreateNiceDataList(self.__CSVremoveEmptyDatasets([lines for lines in dataFile]))
        dataFile.close()
        self.name = filename

    def getSetNames(self):
        return [entry[0] for entry in self.__getDataList()]

    def minToSec(self):
        newdataset = [([self.raw_dataLines[0][0]] +  [[times*60 for times in self.__getTimes()]])] + self.__getDataList()
        self.raw_dataLines = [a for a in newdataset]

    def makePlot(self, n):
        "Build plottable tuples from line n of the data"
        plot = []
        for i, time in enumerate(self.__getTimes()):
            plot = plot + [[time, self.__getDataList()[n][1][i]]]
        return dataPlot(plot)

    def __CSVremoveEmptyDatasets(self, lst):
        "If a data entry begins comma then no data - remove!"
        return [item for item in lst if not item[0]==',']      

    def __CSVcreateNiceDataList(self, lst):
        "Turns a raw list from the file into a nicely formatted list"
        a = [re.split('[,]', dataLine) for dataLine in lst]    # Splits the list by commas
        b = [self.__CSVdF_removeNewLine(item) for item in a]
        return [ ([item.pop()]) + [dF_makeFloats(item)] for item in b]    # Puts name as first item of the list, then data set as second

    def __CSVdF_removeNewLine(self, listItem):
        listItem.pop()
        return listItem

    def __getTimes(self):
        return self.raw_dataLines[0][1]

    def __getDataList(self):
        return self.raw_dataLines[1:]

class dataPlot(list):		# Want this to behave like a list with extra properties
    def fromList(self, lst):    # Should now be redundant
        self.clear()
        [self.append(i) for i in lst]

    def listOfTuples(self):     # Should now be redundant
        return [a for a in self]


def dF_makeFloats(list):
    return [dF_float(i) for i in list]

def dF_float(i):
    try: return float(i)
    except ValueError:
        try: return float(i[1:-1])    # Try getting rid of mysterious parenthesese
        except ValueError: return 0

def extractValues(dataplot, par):
    return [point[par] for point in dataplot]

def dimPlot(dataplot, par):
    values = extractValues(dataplot, par)
    return (max(values) - min(values))

def takeInitial(dataplot, cond):
    return list(itertools.takewhile(cond, dataplot))
