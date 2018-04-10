from context import pressure_base
from context import transducer_tools

pressTools = transducer_tools()
pressureCSV = pressure_base(0.042389869, -0.124235215, 100)


# press86_front = pressure_model_86(1, 0.0547, 0.261)
# press86_back = pressure_model_86(1, 0.0547, 0.261)
# press86_front.setUpChanel()
# press86_back.setUpChanel()

pressureCSV.setUpChanel(fileName='pressure_base_data_3.csv')

i = 0
endOfFile = pressureCSV.getLenOfFile()-3
# print(endOfFile)
print('start')

while i<=endOfFile:

    pressureCSV.set_data()
    press1 = pressureCSV.get_pressure()

    print(press1)

    i += 1

print('done')