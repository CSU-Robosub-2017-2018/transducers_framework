''' transducer.py -- Is the parent class for all of the transducers and contains all of the
information that is common between them all.
'''


class transducer:

    #Veriables
    def __init__(self):
        # does it have accelerometers, groscopes, magnometers
        self.hasVoltageData = False
        self.hasUnitData = False

        self.voltageData = 0
        self.unitData = 0

        self.timeStamp = 0

    # Returns all data available
    def getAllAvalableData(self):  # all data
        allDataAvalable = (self.hasVoltageData, self.hasUnitData, self.voltageData, self.unitData, self.timeStamp)
        return allDataAvalable