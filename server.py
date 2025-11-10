from fastmcp import FastMCP

# Initialize MCP server
mcp = FastMCP("Weather MCP Server")

@mcp.tool()
def get_temperature(city: str, unit: str = "celsius") -> dict:
    """Get the current temperature for a city"""
    # Mock data for testing
    temps = {
        "celsius": {"london": 15, "paris": 18, "tokyo": 22, "new york": 20},
        "fahrenheit": {"london": 59, "paris": 64, "tokyo": 72, "new york": 68}
    }
    
    city_lower = city.lower()
    if city_lower in temps.get(unit, {}):
        return {
            "city": city,
            "temperature": temps[unit][city_lower],
            "unit": unit
        }
    else:
        return {
            "error": f"City {city} not found",
            "available_cities": list(temps["celsius"].keys())
        }

@mcp.tool()
def convert_temperature(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert temperature between Celsius and Fahrenheit"""
    if from_unit.lower() == "celsius" and to_unit.lower() == "fahrenheit":
        converted = (value * 9/5) + 32
    elif from_unit.lower() == "fahrenheit" and to_unit.lower() == "celsius":
        converted = (value - 32) * 5/9
    else:
        return {"error": "Invalid units. Use 'celsius' or 'fahrenheit'"}
    
    return {
        "original_value": value,
        "original_unit": from_unit,
        "converted_value": round(converted, 2),
        "converted_unit": to_unit
    }

@mcp.resource("weather://cities")
def get_available_cities():
    """Get list of available cities"""
    return {
        "cities": ["London", "Paris", "Tokyo", "New York"],
        "total": 4
    }
