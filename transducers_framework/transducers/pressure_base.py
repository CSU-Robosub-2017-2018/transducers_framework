''' pressure_base.py - This is the base transducer that takes in csv files and outputs data like a normal
pressure transducer. This class should be used for and preliminary testing or
for comparing two different algorithms.
'''

from transducers_framwork.transducers.transducer import transducer
import numpy as np


class pressure_base(transducer):

    ##
    # @brief Base class that reads in a csv file and behaves like a live pressure transducer
    # @param m Initializes the m component of y = amp*m*x + b for the calibration curve
    # @param b Initializes the b component of y = amp*m*x + b for the calibration curve
    # @param amp Initializes the amp component of y = amp*m*x + b for the calibration curve
    def __init__(self, m=0, b=0, amp=1000):
        transducer.__init__(self)

        self.hasVoltageData = True
        self.hasUnitData = True

        self.m = m
        self.b = b
        self.amp = amp

        self.counter = 0
        self.lengthOfFile = 0

        self.voltagePositive = None
        self.voltageNegetive = None

        self.numOfPressTrasnducers = 0


    ##
    # @brief Reads in the desired csv file, stores the values, updates self.numOfPressTrasnducers
    # and updates self.lengthOfFile to the length of the data
    # @param fileName  The name of the csv file that will be used
    def setUpChanel(self, fileName='pressure_base_data_1.csv'):
        pathAndFileName = 'C:/Users/bob/Desktop/transducers_framework/tests/test_files/' + fileName  # Fix me remove hardcode path

        csv = np.genfromtxt(pathAndFileName, delimiter=",")

        [numRows, numCollumns] = csv.shape

        if numCollumns == 2:
            print('one pressure transducer')
            self.numOfPressTrasnducers = 1

            self.voltagePositive = np.zeros([numRows - 1, self.numOfPressTrasnducers])
            self.voltageNegetive = np.zeros([numRows - 1, self.numOfPressTrasnducers])

            self.voltagePositive = csv[1:-1, 0]
            self.voltageNegetive = csv[1:-1, 1]

        if numCollumns == 4:
            print('two pressure transducers')
            self.numOfPressTrasnducers = 2

            self.voltagePositive = np.zeros([numRows - 1, self.numOfPressTrasnducers])
            self.voltageNegetive = np.zeros([numRows - 1, self.numOfPressTrasnducers])

            self.voltagePositive[0:-1, 0] = csv[1:-1, 0]
            self.voltageNegetive[0:-1, 0] = csv[1:-1, 1]

            self.voltagePositive[0:-1, 1] = csv[1:-1, 2]
            self.voltageNegetive[0:-1, 1] = csv[1:-1, 3]

        if numCollumns == 6:
            print('three pressure transducers')
            self.numOfPressTrasnducers = 3

            self.voltagePositive = np.zeros([numRows - 1, self.numOfPressTrasnducers])
            self.voltageNegetive = np.zeros([numRows - 1, self.numOfPressTrasnducers])

            self.voltagePositive[0:-1, 0] = csv[1:-1, 0]
            self.voltageNegetive[0:-1, 0] = csv[1:-1, 1]

            self.voltagePositive[0:-1, 1] = csv[1:-1, 2]
            self.voltageNegetive[0:-1, 1] = csv[1:-1, 3]

            self.voltagePositive[0:-1, 2] = csv[1:-1, 4]
            self.voltageNegetive[0:-1, 2] = csv[1:-1, 5]

        self.lengthOfFile = numRows
        print(self.lengthOfFile)

    ##
    # @brief This function updates the list voltagePositive and voltage Negetive global
    # variables one row at a time to simulate live data
    def set_data(self):
        # print('set data')

        if self.numOfPressTrasnducers == 1:
            self.voltageData = [self.voltagePositive[self.counter],
                                self.voltageNegetive[self.counter]]

        if self.numOfPressTrasnducers == 2:
            self.voltageData = [self.voltagePositive[self.counter, 0],
                                self.voltageNegetive[self.counter, 0],
                                self.voltagePositive[self.counter, 1],
                                self.voltageNegetive[self.counter, 1]]

        if self.numOfPressTrasnducers == 3:
            self.voltageData = [self.voltagePositive[self.counter, 0],
                                self.voltageNegetive[self.counter, 0],
                                self.voltagePositive[self.counter, 1],
                                self.voltageNegetive[self.counter, 1],
                                self.voltagePositive[self.counter, 2],
                                self.voltageNegetive[self.counter, 2]]


        self.counter = self.counter + 1


    ##
    # @brief This function returns the calculated pressure data given specific m, b, and amp variables
    # @return pressure Returns the calculated pressure
    def get_pressure(self):
        # print('get pressure')

        diff = np.zeros(self.numOfPressTrasnducers)
        iterr = 0
        while iterr <= self.numOfPressTrasnducers-1:
            diff[iterr] = (self.voltageData[iterr*2] - self.voltageData[iterr*2+1]) * self.amp
            iterr = iterr+1
        # print(diff)
        pressure = self.m * diff + self.b
        return pressure

    ##
    # @brief This function returns the number of pressure transducers
    # @return numOfPressTrasnducers Returns the number of pressure transducers described in the csv file
    def get_numOfPressTrasnducers(self):
        return self.numOfPressTrasnducers
