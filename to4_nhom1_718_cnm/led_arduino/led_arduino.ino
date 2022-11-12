// C++ code
//
int  green = 2;
int yellow = 3;
int red = 4;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(green,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(red,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(green, HIGH);
  Serial.println("ON");
  delay(3000);
  digitalWrite(green, LOW);
  Serial.println("OFF");
  delay(3000);
  digitalWrite(yellow, HIGH);
  delay(5000);
  digitalWrite(yellow, LOW);
  delay(5000);
  digitalWrite(red, HIGH);
  delay(9000);
  digitalWrite(red, LOW);
  delay(9000);
}