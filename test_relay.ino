#define led 14
#define relay 26

void setup() {
  // put your setup code here, to run once:
  pinMode(relay, OUTPUT); // RElay
  pinMode(led, OUTPUT); // LED
  Serial.begin(9600);

}

void loop() {
  
  digitalWrite(led, HIGH);
  delay(1500);
  digitalWrite(led, LOW);
  delay(1500);
  
  // put your main code here, to run repeatedly:
  if(led == LOW){
    Serial.println("Success");
  }else{
    Serial.println("Failed");
  }
  
}
