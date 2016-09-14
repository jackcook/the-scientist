from aenum import Enum

class Distance:
    def __init__(self, length, unit):
        self.original_value = float(length)
        self.original_unit = unit

        self.value = float(length) * unit.value[0]

        self.kilometers = self.value * DistanceUnit.kilometer.value[0]
        self.meters = self.value
        self.centimeters = self.value * DistanceUnit.centimeter.value[0]
        self.millimeters = self.value * DistanceUnit.millimeter.value[0]
        self.micrometers = self.value * DistanceUnit.micrometer.value[0]
        self.nanometers = self.value * DistanceUnit.nanometer.value[0]
        self.miles = self.value * DistanceUnit.mile.value[0]
        self.yards = self.value * DistanceUnit.yard.value[0]
        self.feet = self.value / DistanceUnit.foot.value[0]
        self.inches = self.value * DistanceUnit.inch.value[0]

    def __str__(self):
        return "%.2f %s%s" % (self.original_value, self.original_unit.value[1],
            " (%.2f m)" % self.value if self.original_unit.name != "meter" else "")

    def __repr__(self):
        return self.__str__()

class DistanceUnit(Enum):
    kilometer = (1000.0, "km", "kilometers")
    meter = (1.0, "m", "meters")
    centimeter = (0.01, "cm", "centimeters")
    millimeter = (0.001, "mm", "millimeters")
    micrometer = (0.000001, "um", "micrometers")
    nanometer = (0.000000001, "nm", "nanometers")
    mile = (1609.34, "mi", "miles")
    yard = (0.9144, "yd", "yards")
    foot = (0.3048, "ft", "feet")
    inch = (0.0254, "in", "inches")
