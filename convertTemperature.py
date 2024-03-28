class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        kelvin =celsius + 273.15
        fah = celsius * 1.80 + 32
        li=[kelvin , fah]
        return li
