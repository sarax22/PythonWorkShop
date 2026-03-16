# Goal -> Use a list of sensor readings and decide when lights should turn on.
# Example Scenario -> "A corridor light system checks motion readings over time. For each reading, decide whether the light should be ON or OFF."

motion_readings = [False, False, True, True, False]

def light_status(motion):
    # return "Light ON" or "Light OFF"
    pass

for reading in motion_readings:
    print(light_status(reading))
