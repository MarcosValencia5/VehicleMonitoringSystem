import obd

connection = obd.OBD("/dev/ttyUSB0")

def safe_query(cmd):
    try:
        response = connection.query(cmd)
        if response.is_null():
            return 0
        return response.value.magnitude
    except:
        return 0

def get_vehicle_data():
    return {
        "speed": safe_query(obd.commands.SPEED),
        "rpm": safe_query(obd.commands.RPM),
        "coolant_temp": safe_query(obd.commands.COOLANT_TEMP)
    }