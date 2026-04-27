import random

# Starting simulated values
speed = 0
rpm = 800
coolant_temp = 170

def get_vehicle_data():
    global speed, rpm, coolant_temp

    # Simulate speed changes
    speed += random.randint(-4, 6)
    speed = max(0, min(speed, 80))

    # Simulate RPM based on speed
    if speed == 0:
        rpm = random.randint(700, 1000)
    else:
        rpm = int(800 + speed * random.randint(25, 45) + random.randint(-150, 150))

    rpm = max(700, min(rpm, 4500))

    # Simulate coolant temperature slowly warming up
    if coolant_temp < 195:
        coolant_temp += random.randint(0, 2)
    else:
        coolant_temp += random.choice([-1, 0, 0, 1])

    coolant_temp = max(170, min(coolant_temp, 220))

    return {
        "speed": speed,
        "rpm": rpm,
        "coolant_temp": coolant_temp
    }