#define BLYNK_TEMPLATE_ID "TMPL3eppMxIZ"
#define BLYNK_TEMPLATE_NAME "LAB10"
#define BLYNK_AUTH_TOKEN "vW5YNQc0uBAh75r5HncPrQVnB8_M--W3"
#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <HTTPClient.h>
#include <BlynkSimpleEsp32.h>
#include <SimpleDHT.h>
int pinDHT11 = 4;
SimpleDHT11 dht11(pinDHT11);
char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "TO_EL";
char pass[] = "123456789";
BlynkTimer timer;
#define PIN1 2
BLYNK_WRITE(V3)
{
  int value = param.asInt();
  Serial.println(value);
  if (value == 1){
  digitalWrite(PIN1,HIGH);
}else if (value == 0){
  digitalWrite(PIN1,LOW);
}
}
void myTimerEvent()
{
  byte temperature = 0;
  byte humidity = 0;
  dht11.read(&temperature, &humidity, NULL);
  int t = (int)temperature;
  int h = (int)humidity;
  if (isnan(h) || isnan(t)) {
  Serial.println(F("Failed to read from DHT sensor!"));
  delay(1000);
  return;
}
  Serial.println(t);
  Serial.println(h);
  delay(100);
  Blynk.virtualWrite(V0, t);
  Blynk.virtualWrite(V1, h);
}
  void setup() {
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  pinMode(PIN1,OUTPUT);
  digitalWrite(PIN1,LOW);
  timer.setInterval(1000L, myTimerEvent);
}
  void loop() {
  Blynk.run();
  timer.run();
}
