@function_tool
def get_weather(city:str):           #city:str --> type annotation
    print("Tool called...")
    """
        Returns the current weather from the city.
    """
    return datetime.now().strftime("%d %B %Y, %I:%M:%S %p")

#just a ex if func is taking parameters then using type annotation ai will understand