# -*- coding: utf-8 -*-
import sys
from transducers_framework.transducers_framework.transducers.a2d_dependencies.ADS1256_definitions import *
from transducers_framework.transducers_framework.transducers.a2d_dependencies.pipyadc import ADS1256
from .transducer import transducer
import time

class pressure_model_86(transducer):

    def __init__(self):
        transducer.__init__(self)

        self.hasVoltageData = True
        self.hasUnitData = True
        self.ads = ADS1256()

        self.EXT1 = POS_AIN1 | NEG_AINCOM
        self.EXT2 = POS_AIN2 | NEG_AINCOM
        self.EXT3 = POS_AIN3 | NEG_AINCOM
        self.EXT4 = POS_AIN4 | NEG_AINCOM
        self.EXT5 = POS_AIN5 | NEG_AINCOM
        self.EXT6 = POS_AIN6 | NEG_AINCOM
        self.EXT7 = POS_AIN7 | NEG_AINCOM

        self.CH_SEQUENCE = (self.EXT1, self.EXT2)

    def setUpChanel(self):
        self.ads.cal_self()

    def set_data(self):
        raw_channels = self.ads.read_sequence(self.CH_SEQUENCE)
        self.voltageData = [i * self.ads.v_per_digit for i in raw_channels]
        # print(self.voltageData)
