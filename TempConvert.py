print("Would you like to convert \n 1) C to F \n 2) F to C")
userChoice = input('Select 1 or 2: ')

if userChoice == '1':
    tempC = input('Tempature in C: ')
    tempC_int = int(tempC)
    convertedC = tempC_int / 5 * 9 + 32

    print(convertedC)
    
if userChoice == '2':
    tempF = input('Tempature in F: ')
    tempF_int = int(tempF)
    convertedF = (5/9) * (tempF_int - 32)

    print(convertedF)

input('Press ENTER to exit')