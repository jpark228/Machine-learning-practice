"""이 스크립트에는 몇 가지 PEP 8 규칙이 들어 있습니다.
"""

import datetime as dt


TEMPERATURE_SCALES = ("fahrenheit", "kelvin",
                      "celsius")


class TemperatureConverter:
    pass  # Doesn't do anything at the moment


def convert_to_celsius(degrees, source="fahrenheit"):
    """이 함수는 화씨나 켈빈을 섭씨로 바꿉니다.
    """
    if source.lower() == "fahrenheit":
        return (degrees-32) * (5/9)
    elif source.lower() == "kelvin":
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"


celsius = convert_to_celsius(44, source="fahrenheit")
non_celsius_scales = TEMPERATURE_SCALES[:-1]

print("Current time: " + dt.datetime.now().isoformat())
print(f"The temperature in Celsius is: {celsius}")