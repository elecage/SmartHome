import paho.mqtt.client as mqtt
import time
broker_address = "192.168.0.39"

#publish callback function
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection returned code=", rc)
        
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected ", str(rc))
    
def on_publish(client, userdata, mid):
    print("In on_pub callback mid = ", mid)
    print(userdata)
    
def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish
    
    # address : 192.168.0.39, port : 1883
    client.connect(broker_address, 1883)
    client.loop_start()
    client.publish('testTopic', "Hello Message")
    client.loop_stop()
    #연결 종료
    client.disconnect()
    
if __name__ == "__main__":
    main()
    
