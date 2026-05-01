import obd

connection = None

def connect_obd():
    global connection
    if connection is None or not connection.is_connected():
        try:
            print("Connecting to OBD...")
            connection = obd.OBD("/dev/ttyUSB0")
        except Exception as e:
            print("Connection failed:", e)
            connection = None

def safe_query(cmd):
    if connection is None:
        return 0

    try:
        response = connection.query(cmd)
        if response.is_null():
            return 0
        return response.value.magnitude
    except:
        return 0

def get_vehicle_data():
    connect_obd()

    return {
        "speed": safe_query(obd.commands.SPEED),
        "rpm": safe_query(obd.commands.RPM),
        "coolant_temp": safe_query(obd.commands.COOLANT_TEMP)
    }