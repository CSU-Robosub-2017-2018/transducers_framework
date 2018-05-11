# -*- coding: utf-8 -*-
import sys
''' pressure_model_base.py - This file is the child class for pressure transducer model 86 absolute pressure transducer.
'''

from transducers_framwork.transducers.a2d_dependencies.ADS1256_definitions import *
from transducers_framwork.transducers.a2d_dependencies.pipyadc import ADS1256
from .transducer import transducer
import time


class pressure_model_86(transducer):

    ##
    # @brief Base class that reads in voltage from the model 86 pressure transducer
    # @param m Initializes the m component of y = amp*m*x + b for the calibration curve
    # @param b Initializes the b component of y = amp*m*x + b for the calibration curve
    # @param amp Initializes the amp component of y = amp*m*x + b for the calibration curve
    # @param input_port Initializes the port number to the port in which data will be gathered
    def __init__(self, m=0, b=0, amp=1000, input_port=1):
        transducer.__init__(self)

        self.hasVoltageData = True
        self.hasUnitData = True
        self.ads = ADS1256()

        self.m = m
        self.b = b
        self.amp = amp

        if input_port == 1:
            EXT2 = POS_AIN2 | NEG_AINCOM
            EXT3 = POS_AIN3 | NEG_AINCOM
            self.CH_SEQUENCE = (EXT2, EXT3)

        if input_port == 2:
            EXT4 = POS_AIN4 | NEG_AINCOM
            EXT5 = POS_AIN5 | NEG_AINCOM
            self.CH_SEQUENCE = (EXT4, EXT5)

        if input_port == 3:
            EXT6 = POS_AIN6 | NEG_AINCOM
            EXT7 = POS_AIN7 | NEG_AINCOM
            self.CH_SEQUENCE = (EXT6, EXT7)

    ##
    # @brief Sets up a chanel to the a2d converter
    def setUpChanel(self):
        self.ads.cal_self()

    ##
    # @brief This function gathers data from the pressure transducer
    def set_data(self):
        raw_channels = self.ads.read_sequence(self.CH_SEQUENCE)
        self.voltageData = [i * self.ads.v_per_digit for i in raw_channels]
        # print(self.voltageData)

    ##
    # @brief This function returns the calculated pressure data given specific m, b, and amp variables
    # @return pressure Returns the calculated pressure
    def get_pressure(self):

        raw_channels = self.ads.read_sequence(self.CH_SEQUENCE)
        self.voltageData = [i * self.ads.v_per_digit for i in raw_channels]

        diff = (self.voltageData[0] - self.voltageData[1]) * self.amp
        # print(diff)
        pressure = self.m * diff + self.b
        return pressure
