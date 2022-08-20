# Conversions program
# IS-280 Summer 2022
# Victoria Shearing

from Converter import Converter

def main():
    print("Wecome to English/Metric Converter.")
    #need to get 'show K temps' answer
    doK = False
    choice = getChoice()
    while choice !=0:
        #bubble up exception handling: Converer will throw errors back here
        try: 
            if choice == 1:
                #Miles to Kilometers
                mi = input("Enter your miles to be converted: ")
                km = Converter.MilesToKm(mi)  #mi variable will be a string
                print("A distance of " +str(mi) + " mile(s) = " + str(km) + " kilometers \n")
            elif choice == 2:
                #Ounces to Grams
                oz = input("Enter your ounces to be converted: ")
                grams = Converter.OzToGrams(oz)  
                print("The weight of " +str(oz) + " ounce(s) = " + str(grams) + " grams \n")
            elif choice == 3:
                #Fahrenheit to Celsius
                far = input("Enter temperature in Fahrenheit: ")
                celsius = Converter.FarToCel(far)
                print("The temperature of " +str(far) + " Fahrenheit = " + str(celsius) + " Celsius \n")
                kelvin = input("Would you like an additional conversion to Kelvin? (y/n) ")
                if kelvin.lower() == "y":
                    doK == True
                    kelvin = Converter.FarToKel(far)
                    print("The temperature of " +str(far) + " Fahrenheit = " + str(kelvin) + " Kelvin \n")
            elif choice == 4:
                #Celsius to Fahrenheit
                cel = input("Enter temperature in Celsius: ")
                far = Converter.CelToFar(cel)  
                print("The temperature of " +str(cel) + " Celsius = " + str(far) + " Fahrenheit \n")

                kelvin = input("Would you like an additional conversion to Kelvin? (y/n) ")
                if kelvin.lower() == "y":
                    doK == True
                    kelvin = Converter.CelToKel(cel)
                    print("The temperature of " +str(cel) + " Celsius = " + str(kelvin) + " Kelvin \n")
            elif choice == 5:
                #Meters to Feet
                m = input("Enter your meters to be converted: ")
                feet = Converter.MetersToFeet(m)  
                print("The distance " +str(m) + " meter(s) = " + str(feet) + " feet \n")
            elif choice == 6:
                #Liters to Gallons
                lit = input("Enter your liters to be converted: ")
                gal = Converter.LitToGal(lit)  
                print("The volume of " +str(lit) + " liter(s) = " + str(gal) + " gallons \n")
            else:
                print("This conversion is not yet implemented. \n")
        except ValueError as e:
            print("Data Error: " + str(e))
        except Exception as e:
            print("General Error: "+ str(e))
            
        choice = getChoice()
    print("Thank you for using the converter.")

def getChoice():
    choice = -1
    while choice < 0 or choice > 6:
        try:
            choice = int(input("Please select your conversion option: \n 1. Miles to Kilometers \n" +
                               " 2. Ounces to Grams \n 3. Fahrenheit to Celsius \n 4. Celsius to Fahrenheit \n" +
                               " 5. Meters to Feet \n 6. Liters to Gallons \n 0. End the Program. \n Your choice: "
                               ))
            print()
            if choice < 0 or choice > 6:
                print("Unknown choice, please select from available options only.\n")
        except ValueError:
            print("Illegal input: integers from 1 - 6 and 0 only. \n")
    return choice     


if __name__ == "__main__":
    main()
