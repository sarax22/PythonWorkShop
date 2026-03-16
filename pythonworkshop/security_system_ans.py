#example answer to security_system.py

system_armed = True
motion_detected = True
door_open = True

if system_armed and motion_detected and door_open:
    print("Intrusion detected at entry point")

elif system_armed and motion_detected:
    print("Alarm triggered")

else:
    print("System safe")



"""
More Neat:

system_armed = True
motion_detected = True
door_open = True
battery_level = 15

if battery_level < 20:
    print("Low battery warning")

if system_armed and motion_detected and door_open:
    print("Intrusion detected at entry point")

elif system_armed and motion_detected:
    print("Alarm triggered")

elif not system_armed and motion_detected:
    print("Motion detected, but system is disarmed")

else:
    print("System safe")

"""

