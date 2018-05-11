''' transducer.py -- Is the parent class for all of the transducers and contains all of the
information that is common between them all.
'''


class transducer:
    # Veriables

    ##
    # @brief Base class that reads in a csv file and behaves like a live imu
    # @param self.hasVoltageData Initializes hasVoltageData to False, used for malfunction check
    # @param self.hasUnitData Initializes hasUnitData to False, used for malfunction check
    # @param self.voltageData Initializes voltageData to 0, used for raw voltage data
    # @param self.unitData Initializes unitData to 0, used for raw data that has be converted to data with a untit i.e. pressure
    # @param self.timeStamp Initializes timeStamp to 0, used for sample time

    def __init__(self):
        # does it have accelerometers, groscopes, magnometers
        self.hasVoltageData = False
        self.hasUnitData = False

        self.voltageData = 0
        self.unitData = 0

        self.timeStamp = 0

    # Returns all data available
    def getDescriptionData(self):  # all data
        allDataAvalable = (self.hasVoltageData, self.hasUnitData, self.unitData, self.timeStamp)
        return allDataAvalable

    def getAllVoltageData(self):
        return self.voltageData
