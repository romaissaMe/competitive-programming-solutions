class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        if not 0 <= celsius <= 1000:
            print('The temperature is negative or exceeds 999 degrees Celsius.')
            return
        kelvin= float(format(celsius+273.15,'.5f'))
        fahrenheit = float(format(celsius*1.80+32,'.5f'))
        return [kelvin,fahrenheit]