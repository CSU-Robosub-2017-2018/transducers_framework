import numpy as np
import csv

class transducer_tools():


    def twoPressurTransducers(self, data, iteration, fileName='youForgotToNameYourFile',
                           save_path='C:/Users/bob/Desktop/transducers_framework/tests/test_files/'):

        fileName = fileName + '.csv'
        nameOfFile = save_path + fileName

        if iteration == 0:
            with open(nameOfFile, "w") as csvfile:
                fieldnames = ['Voltage_P0', 'Voltage_N0', 'Pressure0',
                              'Voltage_P1', 'Voltage_N1', 'Pressure1']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'Voltage_P0': data[0], 'Voltage_N0': data[1], 'Pressure0': data[2],
                                 'Voltage_P1': data[3], 'Voltage_N1': data[4], 'Pressure1': data[5]})

        if iteration != 0:
            with open(nameOfFile, "a") as csvfile:
                fieldnames = ['Voltage_P0', 'Voltage_N0', 'Pressure0',
                              'Voltage_P1', 'Voltage_N1', 'Pressure1']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'Voltage_P0': data[0], 'Voltage_N0': data[1], 'Pressure0': data[2],
                                 'Voltage_P1': data[3], 'Voltage_N1': data[4], 'Pressure1': data[5]})
