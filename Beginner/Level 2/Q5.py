'''
5. You are developing a program that analyzes weather data.
Write a Python function that takes a list of temperature readings for a specific location and determines the average temperature, highest temperature, and lowest temperature.
Input: temperature_readings = [25, 28, 21, 24, 27]
Output: Average Temperature: 25.0 Highest Temperature: 28 Lowest Temperature: 21
'''

def weather_forcast(temperature_readings):
    avg_temp = sum(temperature_readings)/ len(temperature_readings)

    highest = max(temperature_readings)
    lowest = min(temperature_readings)

    print("Average Temperature:", avg_temp, "\nHighest Temperature:", highest, "\nLowest Temperature:", lowest)

weather_forcast([25, 28, 21, 24, 27])