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
 //myservo.write(60);
 
  for(pos = 40; pos <= 120; pos += 20)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(5000);                       // waits 15ms for the servo to reach the position 
  } 
  for(pos = 120; pos>=40; pos-=20)     // goes from 180 degrees to 0 degrees 
  {                                
    myservo.write(pos);              // tell servo to go to position in variable 'pos' 
    delay(5000);                       // waits 15ms for the servo to reach the position 
  } 

 
  // put your main code here, to run repeatedly:

}
