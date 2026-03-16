#example answer to environment_monitor.py

temperature = 31
humidity = 28
light_level = 180

if temperature > 30:
    print("Fan ON")

if humidity < 30:
    print("Low humidity warning")

if light_level < 200:
    print("Lights ON")

if temperature <= 30 and humidity >= 30 and light_level >= 200:
    print("Room conditions normal")



"""
More neat:

temperature = 31
humidity = 28
light_level = 180

message_printed = False

if temperature > 30:
    print("Fan ON")
    message_printed = True

if humidity < 30:
    print("Low humidity warning")
    message_printed = True

if light_level < 200:
    print("Lights ON")
    message_printed = True

if not message_printed:
    print("Room conditions normal")
    
"""
