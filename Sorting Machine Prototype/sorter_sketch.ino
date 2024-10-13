#include <Servo.h>
#include <string.h>


// Pin assignments and variables/object declarations. 

int servoPin = 9;
int digit1 = 1;
int digit2 = 1;
String receivedString;
Servo servo1; 

// Functions Declarations.





int movementDecision(int digit1, int digit2);

void setup() {

  servo1.attach(9);
  Serial.begin(115200);
  
}

void loop() {

  
 // this while loop will run until something appears at the Serial communication channel

  while(Serial.available() == 0) {

    movementDecision(0, 0);

    // Debugging print statements. 
    Serial.println(Serial.available());
    Serial.print(digit1);
    Serial.print(" - ");
    Serial.print(digit2);
    Serial.println("");

    }

  // read the string from the communication channel
  receivedString=Serial.readString();
  Serial.print("Outside ");


  // Assign digit1 and digit2 to the digits of the signal. 
  digit1 = receivedString.substring(0, 1).toInt(); // Extract the first digit and convert to integer
  digit2 = receivedString.substring(1, 2).toInt(); // Extract the second digit and convert to integer

  movementDecision(digit1, digit2);

  // Printing Lines for debugging and displaying the digit combinations: 00, 01, 10, and 11. 
  Serial.print(digit1);
  Serial.print(" - ");
  Serial.print(digit2);
  Serial.println("");

  
  
}



int movementDecision(int digit1, int digit2) {

  if ((digit1 == 0 && digit2 == 0)) {

  // Default Movement, back and forth. 

      for (int pos = 90; pos <= 120; pos += 1) { 
          servo1.write(pos);              
          delay(3);                       
      }
      for (int pos = 120; pos >= 90; pos -= 1) { 
           servo1.write(pos);              
          delay(3);                       
      }
     
  }

  else if (digit1 == 1 && digit2 == 0) {

    // Drop the object to the left. 
    servo1.write(180);
    delay(500);
    servo1.write(105);
    
  }

  else if (digit1 == 0 && digit2 == 1) {

    // Drop the object to the right.
    servo1.write(30);
    delay(500);
    servo1.write(105);
    
    
  }

  else {
    
    return -1; // Invalid Reading, return -1. Also, can be a used as a way to stop servo movement by entering 11 as the signal.
  }

  return 1; // Successfull Movement, return 1.
}





/* MRAA STUFF WE ARE NOT USING ANYMORE 

int pin1 = A0;
int pin2 = A1;
int analogValue1 = 0;
int analogValue2 = 0;

pinMode(pin1, INPUT);
pinMode(pin2, INPUT);

int assignDigit(int analogValue) {

  if (analogValue > 50) {
    return 1;
  }
  else {
    return 0;
  }
};
analogValue1 = analogRead(pin1);
analogValue2 = analogRead(pin2);
digit1 = assignDigit(analogValue1);
digit2 = assignDigit(analogValue2);

*/



