from pluginArch import *
from dataFunc import *
from analysis import *
from tkinter import filedialog

class AndreasAnalysisPlus(DataSetProcessor):
    name = "Andrea's Analysis tool"
    docString = "Gets the gradients of the initial growth lines, and lets you save these to a file"
    signature = [True, False]

    def process(dataset):
        datafile = filedialog.asksaveasfile(mode="w", defaultextension=".csv")
        datacsv = "Value, Name \n"
        for i, name in enumerate(dataset.getSetNames()):
            try: datacsv += "{:.1e}".format(dataAndrea(dataset.makePlot(i)))+ ", " + name + "\n"
            except: datacsv += "ERROR, " + name + "\n"
        datafile.write(datacsv)
        datafile.close()

