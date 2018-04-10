from transducers_framwork.transducers.transducer import transducer
import numpy as np


class pressure_base(transducer):
    def __init__(self, m=0, b=0, amp=1000, input_port=1):
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

    def getLenOfFile(self):
        return self.lengthOfFile

    def get_numOfPressTrasnducers(self):
        return self.numOfPressTrasnducers
