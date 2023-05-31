import paho.mqtt.client as mqtt
import time
broker_address = "192.168.0.39"

#subscriber callback function
def on_message(client, userdata, message):
    print("message received : ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    
def main():
    client1 = mqtt.Client()
    client1.connect(broker_address, 1883)
    client1.on_message = on_message
    client1.subscribe("outTopic")
    print("Topic subscribe")
    
    client1.loop_start()
    time.sleep(30)
    client1.loop_stop()
    
    client1.disconnect()
    
if __name__ == "__main__":
    main()