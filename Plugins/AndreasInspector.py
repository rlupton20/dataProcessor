from pluginArch import *
from tkinter import *
from dataInspection import *

class AndreasAnalysisPlus(DataSetProcessor):
    name = "Andrea's Inspection Tool"
    docString = "View the gradients of the initial growth lines for each bit of the dataset"
    signature = [True, False]

    def process(dataset):
        inspectionWindow = Toplevel()
        inspectionWindow.title("Inspection window for " + dataset.name)
        inspectionTools = DataInspectionWindow(inspectionWindow, dataset)
        return
