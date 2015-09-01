#!/usr/bin/python

from tkinter import *
from tkinter import filedialog
from dataInspection import *   
from pluginArch import *

findPlugins()

class ProgramStructure:
    def __init__(self):
        self.dataSets = []
        self.dataSetPlugins = DataSetProcessor.plugins

    def addDataSet(self, dataset):
        self.dataSets += [dataset]

    def applyDataSetPlugin(self, plugin, dataset):
        plugin.apply(self, dataset)

class MainWindow:
    def __init__(self, parent):
        self.windowParent = parent

        self.program = ProgramStructure()

        # Construct menus - menus and items are specified by plugins
        self.menubar = Menu(parent)
        # Get menu headers (Should only be a short list)
        headers = []
        for h in MenuItem.plugins:
            if h.menuSlot not in headers:
                headers += [h.menuSlot]
        # Build menus
        menuStructure = [[h, Menu(self.menubar)] for h in headers]
        [self.menubar.add_cascade(label=m[0], menu=m[1]) for m in menuStructure]
        for h in menuStructure:
            [h[1].add_command(label=p.name, command=lambda: [p.process(self, self.program), self.update()]) for p in MenuItem.plugins if p.menuSlot == h[0]]


        Label(parent, text="Data Sets").grid()
        self.dataSetsBox = Listbox(parent, width=60, exportselection=0)
        #self.dataSetsBox["selectmode"] = EXTENDED
        self.dataSetsBox.grid()

        Label(parent, text="Tasks").grid()
        self.pluginList = Listbox(parent, width = 60, exportselection=0)
        self.pluginList["selectmode"] = EXTENDED
        self.pluginList.grid()

        [self.pluginList.insert(END, p.name) for p in self.program.dataSetPlugins]

        self.runButton = Button(parent, text="Run", background="white")
        self.runButton.grid()
        self.runButton.bind("<Button-1>", self.runPluginOnDataset)

        self.update()    # Take program data and update lists
        
    def runPluginOnDataset(self, event):
        selectedPlugins = [self.program.dataSetPlugins[i] for i in self.pluginList.curselection()]
        selectedDataSets = [self.program.dataSets[i] for i in self.dataSetsBox.curselection()]
        [p.apply(self.program, d) for p in selectedPlugins for d in selectedDataSets]
        self.update()

    def update(self):
        self.dataSetsBox.delete(0, self.dataSetsBox.size())
        [self.dataSetsBox.insert(END, p.name) for p in self.program.dataSets]
    


root = Tk()
root.title("Data Analysis")
baseMenu = MainWindow(root)
root.config(menu = baseMenu.menubar)
root.mainloop()
