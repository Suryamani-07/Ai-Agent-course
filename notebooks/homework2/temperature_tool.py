from agents import function_tool

@function_tool
def convert_temperature(celsius: float) -> float:
    """Convert temperature from Celsius to Fahrenheit."""

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit