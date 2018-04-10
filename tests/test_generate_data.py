from context import pressure_base
from context import transducer_tools

pressTools = transducer_tools()
pressureCSV = pressure_base(0.042389869, -0.124235215, 100)


# press86_front = pressure_model_86(1, 0.0547, 0.261)
# press86_back = pressure_model_86(1, 0.0547, 0.261)
# press86_front.setUpChanel()
# press86_back.setUpChanel()

pressureCSV.setUpChanel(fileName='pressure_base_data_2.csv')
endOfFile = pressureCSV.getLenOfFile()-3


i = 0
print('start')

while i<=endOfFile:

    pressureCSV.set_data()
    voltageData = pressureCSV.getAllVoltageData()
    pressureData = pressureCSV.get_pressure()

    data = [voltageData[0], voltageData[1], pressureData[0],
            voltageData[2], voltageData[3], pressureData[1],
            ]

    pressTools.twoPressurTransducers(data,i, 'test_generate_')


    i += 1

print('done')