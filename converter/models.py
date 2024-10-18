from enum import Enum


class LengthMeasurements(str, Enum):
    millimeter = "millimeter"
    centimeter = "centimeter"
    meter = "meter"
    kilometer = "kilometer"
    inch = "inch"
    foot = "foot"
    yard = "yard"
    mile = "mile"


class WeightMeasurements(str, Enum):
    milligram = "milligram"
    gram = "gram"
    kilogram = "kilogram"
    ounce = "ounce"
    pound = "pound"


class TemperatureMeasurements(str, Enum):
    celsius = "celsius"
    fahrenheit = "fahrenheit"
    kelvin = "kelvin"
