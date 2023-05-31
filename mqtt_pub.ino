#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid     = "bioElectronics";
const char* password = "tlsfkd1004";

const char* mqtt_server = "192.168.0.39";
int smartConfigCount = 0;
unsigned long lastMsg = 0;

#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;


WiFiClient espClient;
PubSubClient client(espClient);

void setup_wifi() {
    WiFi.begin();
    for (int i = 0; ; i++) {
    Serial.println("Connecting to WiFi...");
    delay(1000);
      if (WiFi.status() == WL_CONNECTED) {
        break;
      }
    }
    if(WiFi.status() != WL_CONNECTED)
    {
      WiFi.mode(WIFI_AP_STA);
      WiFi.beginSmartConfig();
      Serial.println("Waiting for smartConfig.");
      while(!WiFi.smartConfigDone()){
         Serial.print(".");
          smartConfigCount++ ;
          if(smartConfigCount > 600)
          {
            ESP.restart();
          }
          delay(1000);
      }
    }

    Serial.println("Waiting for WiFi");
    while (WiFi.status() != WL_CONNECTED) {
      delay(1000);
      Serial.print(",");
    }
    randomSeed(micros());
    
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());
    Serial.print("IP Address: ");
    Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for(int i = 0 ; i < length ; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}
void reconnect()
{
  while(!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);

    if(client.connect(clientId.c_str())) {
      Serial.println("connected");
      client.publish("outTopic", "hello world");
      client.subscribe("inTopic");
    } else 
    {
      Serial.print("failed, rc = ");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void setup(){
    // put your setup code here, to run once:
    Serial.begin(115200);
    delay(10);  
    setup_wifi();
    client.setServer(mqtt_server, 1883);
    client.setCallback(callback);
}
void loop() {
  // put your main code here, to run repeatedly:
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastMsg > 2000) {
    lastMsg = now;
    ++value;
    snprintf (msg, MSG_BUFFER_SIZE, "hello world #%ld", value);
    Serial.print("Publish message: ");
    Serial.println(msg);
    client.publish("outTopic", msg);
  }
  
}
