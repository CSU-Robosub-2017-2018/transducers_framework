from context import pressure_base
from context import transducer_tools
import numpy as np

pressTools = transducer_tools()
pressureCSV = pressure_base(0.042389869, -0.124235215, 100)


# press86_front = pressure_model_86(1, 0.0547, 0.261)
# press86_back = pressure_model_86(1, 0.0547, 0.261)
# press86_front.setUpChanel()
# press86_back.setUpChanel()

pressureCSV.setUpChanel(fileName='pressure_base_data_3.csv')
endOfFile = pressureCSV.getLenOfFile()-3


i = 0
print('start')

while i<=endOfFile:

    pressureCSV.set_data()
    voltageData = pressureCSV.getAllVoltageData()

    print(voltageData)

    i += 1

print('done')