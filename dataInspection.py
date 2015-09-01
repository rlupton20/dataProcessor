from tkinter import *

from dataFunc import *
from analysis import *
from linRegression import gradient, intercept

class DataInspectionWindow:
    def __init__(self, parent, dataset):
        self.data = dataset

        self.windowParent = parent
        self.mainContainer = Frame(parent)
        self.mainContainer.grid()

        self.settingsArea = Frame(self.mainContainer)
        self.settingsArea.grid(column = 0, row = 0, sticky=N)

        Label(self.settingsArea, text="List of Data Sets").grid()

        self.dataSelect = Listbox(self.settingsArea, width=30)
        self.dataSelect["selectmode"] = EXTENDED
        self.dataSelect.grid(row=1, stick=N)
        self.dataSelect.bind("<<ListboxSelect>>", self.displayPlot)

        [self.dataSelect.insert(END, name) for name in self.data.getSetNames()]

        self.plotArea = Frame(self.mainContainer)
        self.plotArea.grid(column=2, row = 0)

        self.plotInfoV = StringVar()
        self.plotInfo = Label(self.plotArea, textvariable=self.plotInfoV)
        self.plotInfo.grid(row=0, column=0)

        self.p_width = 400
        self.p_height = 400
        self.plot = Canvas(self.plotArea, width=self.p_width, height=self.p_height)
        self.plot.grid()        

    def displayPlot(self, event):
        [self.plot.delete(item) for item in self.plot.find_all()]	# Clear the plot
        for i in self.dataSelect.curselection():
            self.plotData(colourFirstFew(self.data.makePlot(i)))
            self.plotInitialLine(self.data.makePlot(i))
            self.plotInfoV.set( self.data.getSetNames()[i] + ": " + "{:.1e}".format(dataAndrea(self.data.makePlot(i))))

    def plotData(self, plot):
        xses = lambda p: [point[0] for point in p]
        yses = lambda p: [point[1] for point in p]
        widthPlotX = dimPlot(plot, 0)
        heightPlotY = dimPlot(plot, 1)
        scaledPoint = lambda p: [10+((p[0] - min(xses(plot)))*((self.p_width - 20)/widthPlotX)), self.p_height-((p[1] - min(yses(plot)))*((self.p_height - 20)/heightPlotY))-10]
        for point in plot:
            try: colour = point[2]	# If colour data is provided use it - else default to black
            except: colour="black"
            self.plot.create_text(scaledPoint(point)[0], scaledPoint(point)[1], text="x", fill=colour)

    def plotInitialLine(self, plot):
        xses = lambda p: [point[0] for point in p]
        yses = lambda p: [point[1] for point in p]
        widthPlotX = dimPlot(plot, 0)
        heightPlotY = dimPlot(plot, 1)
        scaledPoint = lambda p: [10+((p[0] - min(xses(plot)))*((self.p_width - 20)/widthPlotX)), self.p_height-((p[1] - min(yses(plot)))*((self.p_height - 20)/heightPlotY))-10]
        m = gradient(getInitialLine(plot))
        c = intercept(getInitialLine(plot))
        line = lambda x: scaledPoint([x, m*x + c])
        start = plot[0][0]
        end = plot[len(getInitialLine(plot))-1][0]
        self.plot.create_line(line(start)[0], line(start)[1], line(end)[0], line(end)[1], fill="blue")   
