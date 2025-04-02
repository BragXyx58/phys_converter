class BaseConverter:
    def __init__(self, converters):
        self.converters = converters

    def convert(self, fromUnit, amount, toUnit, converterName):

        neededConverter = self.converters[converterName]

        value_in_base = amount / neededConverter[fromUnit]

        return {toUnit: value_in_base * neededConverter[toUnit]}
