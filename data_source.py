import obd

connection = obd.OBD()

def safe_query(command):
    response = connection.query(command)

    if response.is_null():
        return 0

    return response.value.magnitude

def get_vehicle_data():
    return {
        "speed": safe_query(obd.commands.SPEED),
        "rpm": safe_query(obd.commands.RPM),
        "coolant_temp": safe_query(obd.commands.COOLANT_TEMP)
    }