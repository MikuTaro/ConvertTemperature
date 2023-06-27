class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """

        self.kelvin = celsius + 273.15
        self.fahrenheit = celsius * 1.80 + 32.00
        return [self.kelvin, self.fahrenheit]

