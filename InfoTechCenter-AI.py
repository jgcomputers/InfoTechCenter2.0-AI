# Print header for the Gasoline Branch
print("******************************************")
print("Gasoline Branch\n\n")

# Import necessary libraries
import random
from time import sleep

# Function to simulate the gas level gauge, randomly choosing a level from a predefined list
def gas_level_gauge():
    gas_level_list = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level

# Function to simulate the list of nearby gas stations, randomly choosing one from a predefined list
def list_of_gas_stations():
    gas_stations = ["Shell", "Speedway", "Marathon", "Mobile", "Costco", "Meijer", "7Eleven"]
    gas_station_nearby = random.choice(gas_stations)
    return gas_station_nearby

# Function to simulate gas level alerts and display relevant information based on the gas level
def gas_level_alert():
    # Generate random distances to gas stations for low and quarter tank levels
    miles_to_gas_stations_low = round(random.uniform(1, 25), 1)
    miles_to_gas_stations_quarter_tank = round(random.uniform(25.1, 50), 1)
    # Get the current gas level
    gas_level_indicator = gas_level_gauge()

    # Check the gas level and display appropriate messages
    if gas_level_indicator == "Empty":
        print("***Warning - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("\n     ***Call Triple AAA***")
    elif gas_level_indicator == "Low" or gas_level_indicator == "Quarter Tank":
        print(f"Your gas tank is {gas_level_indicator.lower()}, checking Google Maps for the closest gas station")
        sleep(2.5)
        if gas_level_indicator == "Low":
            print(f"The closest gas station is {list_of_gas_stations()}, which is {miles_to_gas_stations_low} miles away.")
        else:
            print(f"The closest gas station is {list_of_gas_stations()}, which is {miles_to_gas_stations_quarter_tank} miles away.")
    elif gas_level_indicator == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination.")
    elif gas_level_indicator == "Three Quarter Tank":
        print("Your gas tank is three quarters full.")
    else:
        print("Your gas tank is full.")

# Call the gas level alert function to simulate a gas level check
gas_level_alert()