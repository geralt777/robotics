#include <Servo.h> 
Servo myservo;  // create servo object to control a servo 
                // a maximum of eight servo objects can be created 
int pos = 0;    // variable to store the servo position 
byte incomingByte;  
void setup() 
{ 
  myservo.attach(3);  // attaches the servo on pin 9 to the servo object 
  Serial.begin(9600);
  //Initial setup ---- setting up the angle to zero.
  myservo.write(0); 

} 
//I have verified whether the angle is properly transmitted or not.---------------?

//Hand shake communication --------------------------------------------------------?


void loop() 
{ 
  
  if(Serial.available()){
    incomingByte = Serial.read();
    int old_pos = int(incomingByte);
    incomingByte = Serial.read();
    int pos = int(incomingByte);
    incomingByte = Serial.read();
    int vel = int(incomingByte) - 100;
    //Serial.print("received");
    Serial.println(incomingByte, DEC);
    Serial.println(incomingByte, DEC);
    int new_position = old_pos+vel;
    if(new_position<15){
      new_position=15;
    }
    else if(new_position>150){
      new_position=150;
    }
    myservo.write(new_position);
    delay(75);
    Serial.println(incomingByte, DEC);
    /*
    if(old_pos>pos)
    {
      for(int i=old_pos;i>=pos;i--)
      {
        myservo.write(i);
        delay(75);
      }
    }
    else
    {
      for(int i=old_pos;i<=pos;i++)
      {
        myservo.write(i);
        delay(75);
      }      
    }*/
  }
  delay(100);
}





