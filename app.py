from flask import Flask, render_template
from data_source_sim import get_vehicle_data
from logger import log_data


print("Starting Flask app...")
app = Flask(__name__)

@app.route("/")
def dashboard():
    data = get_vehicle_data()
    log_data(data)
    print(f"Logged data: {data}")
    return render_template("index.html", data=data)

if __name__ == "__main__":
    print("Running Flask app...")
    app.run(host="0.0.0.0", port=5050, debug=True)