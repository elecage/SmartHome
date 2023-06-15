from flask import Flask, request, render_template
import paho.mqtt.client as mqtt

broker_address = "192.168.0.39"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/led/on")
def led_on():
    client1 = mqtt.Client()
    client1.connect(broker_address, 1883)
    client1.publish("IND/LED5", 'ON')
    client1.disconnect()
    return 'ok'
    
    
@app.route("/led/off")
def led_off():
    client1 = mqtt.Client()
    client1.connect(broker_address, 1883)
    client1.publish("IND/LED5", 'OFF')
    client1.disconnect()
    return 'ok'
    
if __name__ == "__main__":
    app.run()