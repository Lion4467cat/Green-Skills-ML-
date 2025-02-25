# LIST COMPREHENSION
climate_data=[
    {"city":"City A","temperature":25,"carbon_footprint":500},
    {"city":"City B","temperature":30,"carbon_footprint":350},
    {"city":"City C","temperature":22,"carbon_footprint":600},
    {"city":"City D","temperature":15,"carbon_footprint":200},
    {"city":"City E","temperature":28,"carbon_footprint":450},
]
high_temp_threshold=26

high_temp_cities=[city for city in climate_data if city["temperature"]>high_temp_threshold]
for city in high_temp_cities:
    print(f"{city["city"]} -{city["temperature"]}°C")
total_carbon=0
for city in climate_data:
    total_carbon+=city["carbon_footprint"]
average_carbon_footprint=total_carbon/len(climate_data)
print(f"Average:{average_carbon_footprint:.2f}kg CO2 ")

sustainability_thresh=400
sustainable_cities=list(filter(lambda city :city["carbon_footprint"]<sustainability_thresh,climate_data))
for city in sustainable_cities:
    print(f"{city["city"]}-{city["carbon_footprint"]} kg CO2")
highest_footprint_city=max(climate_data,key=lambda city: city["carbon_footprint"])
print(f"City with the highest carbon footprint:")
print(f"{highest_footprint_city["city"]}-{highest_footprint_city["carbon_footprint"]}kg CO2")

#User defined,built-in & lambda functions
def calculate_carbon_footprint(energy_consumption,emission_factor):
    return energy_consumption*emission_factor
check1=calculate_carbon_footprint(100,2.0)
print(check1)
