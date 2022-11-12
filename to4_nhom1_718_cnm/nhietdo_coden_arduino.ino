#include <dht.h>
#define dht_apin A0 // Analog Pin sensor is connected to
 
dht DHT;
int red = 10;
int green = 12;
int yellow = 11;

void setup(){
  pinMode(A0, INPUT);
  Serial.begin(9600);
  delay(500);//Delay to let system boot
  Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000);//Wait before accessing Sensor
  pinMode(red, OUTPUT);
  pinMode(green, OUTPUT);
  pinMode(yellow, OUTPUT);
}//end "setup()"
 
void loop(){
  //Start of Program 
 
    DHT.read11(dht_apin);
    
    Serial.print("Current humidity = ");
    Serial.print(DHT.humidity);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(DHT.temperature); 
    Serial.println("C  ");
    digitalWrite(green, LOW);
    digitalWrite(red, LOW);
    digitalWrite(yellow, LOW);

    if (DHT.temperature < 20) { //cold
      digitalWrite(green, HIGH);
      // Serial.println(" It's Cold.");
    }
    else if (DHT.temperature >= 20 && DHT.temperature <= 27) { //hot
      digitalWrite(green, LOW);
      digitalWrite(yellow, HIGH);
      // Serial.println(" It's Hot.");
    }
    else { //fine
      digitalWrite(yellow, LOW);
      digitalWrite(red, HIGH);
    }

    delay(2000);//Wait 5 seconds before accessing sensor again.
 
  //Fastest should be once every two seconds.
 
}// end loop(