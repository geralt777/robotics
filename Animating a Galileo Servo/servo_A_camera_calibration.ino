// Sweep
// by BARRAGAN <http://barraganstudio.com> 
// This example code is in the public domain.


#include <Servo.h> 
 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
 
int pos = 0;    // variable to store the servo position 
 
void setup() 
{ 
  myservo.attach(3);
  myservo.write(0); 
  
  
  // attaches the servo on pin 9 to the servo object 
} 


void loop() {
Serial.print("sensor"); 
myservo.write(0);
 delay(2500);
 myservo.write(45);
 delay(2500);
 
myservo.write(90);
 delay(2500);

 
  // put your main code here, to run repeatedly:

}


