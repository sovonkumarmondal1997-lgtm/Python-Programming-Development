def traffic_light_message(color):
    if color == "red":
        return "Stop"
    elif color == "yellow":
        return "Prepare to stop"
    elif color == "green":
        return "Go"
    else:
        return "Invalid traffic light color"


traffic_lights = ["green", "yellow", "red", "green"]

for color in traffic_lights:
    message = traffic_light_message(color)
    print(message)