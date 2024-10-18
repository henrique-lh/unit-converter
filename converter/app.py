from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from converter.models import (
    LengthMeasurements,
    WeightMeasurements,
    TemperatureMeasurements,
)
from converter.conversors import (
    to_meters,
    from_meters,
    to_grams,
    from_grams,
    celsius_to_kelvin,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
)

app = FastAPI()


@app.get("/length/", status_code=HTTPStatus.OK)
def convert_length(
    length: float, unit_from: LengthMeasurements, unit_to: LengthMeasurements
):
    if length < 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Length is not valid"
        )

    length_in_meters = to_meters(length, unit_from)
    converted_length = from_meters(length_in_meters, unit_to)

    return {"length": length, "converted_length": converted_length}


@app.get("/weight/", status_code=HTTPStatus.OK)
def convert_weight(
    weight: float, unit_from: WeightMeasurements, unit_to: WeightMeasurements
):
    if weight < 0:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST, detail="Weight is not valid"
        )

    weight_in_grams = to_grams(weight, unit_from)
    converted_weight = from_grams(weight_in_grams, unit_to)

    return {"weight": weight, "converted_weight": converted_weight}


@app.get("/temperature/", status_code=HTTPStatus.OK)
def convert_temperature(
    temperature: float,
    unit_from: TemperatureMeasurements,
    unit_to: TemperatureMeasurements,
):
    if unit_from == TemperatureMeasurements.celsius:
        if unit_to == TemperatureMeasurements.fahrenheit:
            converted_temp = celsius_to_fahrenheit(temperature)
        elif unit_to == TemperatureMeasurements.kelvin:
            converted_temp = celsius_to_kelvin(temperature)
    elif unit_from == TemperatureMeasurements.fahrenheit:
        if unit_to == TemperatureMeasurements.celsius:
            converted_temp = fahrenheit_to_celsius(temperature)
        elif unit_to == TemperatureMeasurements.kelvin:
            converted_temp = fahrenheit_to_kelvin(temperature)
    elif unit_from == TemperatureMeasurements.kelvin:
        if unit_to == TemperatureMeasurements.celsius:
            converted_temp = kelvin_to_celsius(temperature)
        elif unit_to == TemperatureMeasurements.fahrenheit:
            converted_temp = kelvin_to_fahrenheit(temperature)
    else:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="Temperature unit is not valid",
        )

    return {"temperature": temperature, "converted_temperature": converted_temp}
