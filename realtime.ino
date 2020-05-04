#include <Servo.h>
char data;
Servo myservo1;
Servo myservo2;

void setup() {
  
  
  // initialize serial communication at 9600 bits per second:
  Serial.begin(57600);
  //pinMode(13, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  Serial.println(analogRead(A0));
  
  while (Serial.available()){
  data = Serial.read();
//  Serial.print(data);
  
  if (data == '0'){
    myservo1.attach(5);
  myservo1.write(0);
  
  }
  else if(data=='1') {
    myservo1.attach(5);
    myservo1.write(30);
  }
  else if(data=='2') {
    myservo1.attach(5);
    myservo1.write(60);
  }
  else if(data=='3') {
    myservo1.attach(5);
  myservo1.write(90);
  }
  else if(data=='4') {
    myservo2.attach(6);
  myservo2.write(0);
  }
  else if(data=='5') {
    myservo2.attach(6);
  myservo2.write(45);
  }
  else if(data=='6') {
    myservo2.attach(6);
  myservo2.write(90);
  }
  else if(data=='7') {
    myservo2.attach(6);
  myservo2.write(135);
  }
  else if(data=='8') {
    myservo2.attach(6);
  myservo2.write(360);
  }
 }
}
