#example answer to smart_lighting.py

motion_readings = [False, False, True, True, False]

def light_status(motion):
    if motion:
        return "Light ON"
    else:
        return "Light OFF"

for reading in motion_readings:
    print(light_status(reading))


"""
Neat Version:

motion_readings = [False, False, True, True, False]

def light_status(motion):
    if motion:
        return "Light ON"
    else:
        return "Light OFF"

for reading in motion_readings:
    print("Motion:", reading, "->", light_status(reading))
    
"""