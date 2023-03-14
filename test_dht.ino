#include <SimpleDHT.h> //โหลดไลบารี่ DHT11
SimpleDHT11 dht11; //ระบุรุ่นเซ็นเซอร์รุ่น DHT11

byte temperature = 0; //กําหนดตัวแปรเก็บค่าอุณหภูมิ
byte humidity = 0; //กําหนดตัวแปรเก็บค่าความชื้นสัมสัทธ์
void setup() {
Serial.begin(115200); //ตั้งค่าคอนโซล
}

void loop() {
dht11.read(4, &temperature, &humidity, NULL); //อ่านค่าจากเซ็นเซอร์
delay(1500); //รอ 1.5 วินาที
Serial.print(temperature); //แสดงค่าอุณหภูมิที่ได้ลงบนคอนโซล
Serial.print("C : ");
Serial.print(humidity); //แสดงค่าความชื้นสัมพัทธ์ที่ได้ลงบนคอนโซล
Serial.println("%");
}
