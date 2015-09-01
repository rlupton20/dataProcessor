from pluginArch import *
from dataFunc import *
from tkinter import filedialog

class OpenCSVDatabase(MenuItem):
    name = "Open CSV"
    docString = "Opens a dataset from a CSV file"
    menuSlot = "File"

    def process(window, program):
        dataFilename = filedialog.askopenfilename()
        data = dataSet()
        data.openCSV(dataFilename)
        data.minToSec()
        program.dataSets += [data]
