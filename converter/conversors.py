from converter.models import LengthMeasurements, WeightMeasurements


def to_meters(length: float, unit: LengthMeasurements) -> float:
    conversion_factors = {
        LengthMeasurements.millimeter: 0.001,
        LengthMeasurements.centimeter: 0.01,
        LengthMeasurements.meter: 1,
        LengthMeasurements.kilometer: 1000,
        LengthMeasurements.inch: 0.0254,
        LengthMeasurements.foot: 0.3048,
        LengthMeasurements.yard: 0.9144,
        LengthMeasurements.mile: 1609.34,
    }
    return length * conversion_factors[unit]


def from_meters(length_in_meters: float, unit: LengthMeasurements) -> float:
    conversion_factors = {
        LengthMeasurements.millimeter: 1000,
        LengthMeasurements.centimeter: 100,
        LengthMeasurements.meter: 1,
        LengthMeasurements.kilometer: 0.001,
        LengthMeasurements.inch: 39.3701,
        LengthMeasurements.foot: 3.28084,
        LengthMeasurements.yard: 1.09361,
        LengthMeasurements.mile: 0.000621371,
    }
    return length_in_meters * conversion_factors[unit]


def to_grams(weight: float, unit: WeightMeasurements) -> float:
    conversion_factors = {
        WeightMeasurements.milligram: 0.001,
        WeightMeasurements.gram: 1,
        WeightMeasurements.kilogram: 1000,
        WeightMeasurements.ounce: 28.3495,
        WeightMeasurements.pound: 453.592,
    }
    return weight * conversion_factors[unit]


def from_grams(weight_in_grams: float, unit: WeightMeasurements) -> float:
    conversion_factors = {
        WeightMeasurements.milligram: 1000,
        WeightMeasurements.gram: 1,
        WeightMeasurements.kilogram: 0.001,
        WeightMeasurements.ounce: 0.035274,
        WeightMeasurements.pound: 0.00220462,
    }
    return weight_in_grams * conversion_factors[unit]


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)
