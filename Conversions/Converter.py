# Converter file for Conversions program
# IS-280 Summer 2022
# Victoria Shearing

class Converter:

    """Convert metric to colonial system using conversion algorithms"""
    @staticmethod
    def MilesToKm(mi):
        if not isinstance(mi, (int, float)):
            try:
                mi = float(mi)
            except ValueError:
                raise Exception("Illegal miles value: not a numeric.")
        if mi <= 0 :
            #error: not a legal value for conversion
            raise ValueError("Miles must be a positive value.")
            
        else:
            km = mi * 1.60934
            return round(km, 3)

    @staticmethod
    def OzToGrams(oz):
        if not isinstance(oz, (int, float)):
            try:
                oz = float(oz)
            except ValueError:
                raise Exception("Illegal ounces value: not a numeric.")
        if oz <= 0 :
            #error: not a legal value for conversion
            raise ValueError("Ounces must be a positive value.")
            
        else:
            grams = oz * 28.3495
            return round(grams, 3)

    @staticmethod
    def FarToCel(far):
        if not isinstance(far, (int, float)):
            try:
                far = float(far)
            except ValueError:
                raise Exception("Illegal temperature value: not a numeric.")    
        if far <= -459.67:
            #error, not a legal value for conversion
            raise ValueError("This temperature is not possible, as it is below 0K")
        else:
            celsius = (far - 32)*5.0/9.0
            return round(celsius, 3)

    @staticmethod
    def CelToFar(cel):
        if not isinstance(cel, (int, float)):
            try:
                cel = float(cel)
            except ValueError:
                raise Exception("Illegal ounces value: not a numeric.")
        if cel <= -273.15:
            #error, not a legal value for conversion
            raise ValueError("This temperature is not possible, as it is below 0K")
        else:
            far = 9.0/5.0*cel + 32
            return round(far, 3)

    @staticmethod
    def MetersToFeet(m):
        if not isinstance(m, (int, float)):
            try:
                m = float(m)
            except ValueError:
                raise Exception("Illegal ounces value: not a numeric.")
        if m <= 0 :
            #error: not a legal value for conversion
            raise ValueError("Ounces must be a positive value.")
            
        else:
            feet = m * 3.2808
            return round(feet, 3)

    @staticmethod
    def LitToGal(lit):
        if not isinstance(lit, (int, float)):
            try:
                lit = float(lit)
            except ValueError:
                raise Exception("Illegal ounces value: not a numeric.")
        if lit <= 0 :
            #error: not a legal value for conversion
            raise ValueError("Ounces must be a positive value.")
            
        else:
            gal = 0.26417*lit
            return round(gal, 3)

    @staticmethod
    def FarToKel(far):
        if not isinstance(far, (int, float)):
            try:
                far = float(far)
            except ValueError:
                raise Exception("Illegal temperature value: not a numeric.")
        if far <= -459.67 :
            #error: not a legal value for conversion
            raise ValueError("This temperature is not possible, as it is below 0 K.\n")
            
        else:
            kelvin = (far - 32)*5.0/9.0 + 273.15
            return round(kelvin, 3)
    @staticmethod
    def CelToKel(cel):
        if not isinstance(cel, (int, float)):
            try:
                cel = float(cel)
            except ValueError:
                raise Exception("Illegal temperature value: not a numeric. \n")
        if cel <= -273.15:
            #error: not a legal value for conversion
            raise ValueError("This temperature is not possible, as it is below 0 K. \n")
            
        else:
            kelvin = cel + 273.15
            return round(kelvin, 3)

