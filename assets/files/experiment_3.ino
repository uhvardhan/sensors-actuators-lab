// Distance Measurement 
#define trigPin 9 
#define echoPin 10 
#define irPin A0 
long duration; 
float distanceUS; 

void setup() 
{ 
  Serial.begin(9600); 
  pinMode(trigPin,OUTPUT); 
  pinMode(echoPin,INPUT);
 } 

void loop()
{ 
  digitalWrite(trigPin,LOW); 
  delayMicroseconds(2); 
  digitalWrite(trigPin,HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  duration=pulseIn(echoPin,HIGH);
  distanceUS=duration*0.0343/2;
  Serial.print("Ultrasonic(cm): "); 
  Serial.print(distanceUS); 
  delay(500); 
}
