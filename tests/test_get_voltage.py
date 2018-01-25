from transducers_framework.tests.context import pressure_model_86

press86 = pressure_model_86()

voltageData = 0

press86.setUpChanel()

i = 0
print('start')
while i <= 10:
    press86.set_data()
    rawImuData = press86.getAllAvalableData()

    hasVoltageData = rawImuData[0]
    hasUnitData = rawImuData[1]
    voltageData = rawImuData[2]
    unitData = rawImuData[3]
    timeStamp = rawImuData[4]
    print(voltageData)
    i += 1
print('done')