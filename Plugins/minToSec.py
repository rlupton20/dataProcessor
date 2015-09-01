from pluginArch import *
from dataFunc import *

class minToSec(DataSetProcessor):
    name = "Header: Minutes to Seconds"
    docString = "Changes the data header from minutes to seconds"
    signature = [True, False]

    def process(dataset):
        dataset.minToSec()

