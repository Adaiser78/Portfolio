// Define study time, break time, and the start time, pushbuttons and switch states, and the restart variable.  
 unsigned long studyTime = 15000; // 100 seconds of studying. 
 unsigned long breakTime = 20000; // 10 seconds break time. 
 unsigned long startTime = 0;
 int switchState, overridePushbuttonState, distancePushbuttonState; 
 bool restart = false;

// Define the pins. 
 const int switchPin = 9;
 const int redPin = 3;
 const int bluePin = 5;
 const int greenPin = 6;
 const int overridePushbuttonPin = 8;
 const int distancePushbuttonPin = 11;
 const int sensitivityPotentiometerPin = A5;



// Define the threshold distance in centimeters, and other distance tracking variables.  
 int setDistance = 50; 
 int closeThreshold = 20;
 int sensorValue;
 const int triggerPin = 13;
 const int echoPin = 12;
 unsigned long duration;
 unsigned int distance;
 unsigned int averageDistance;
 unsigned int sumDistances = 0;
 const int minValue = 5;
 const int maxValue = 40;
 const int AverageDistanceAccuracy = 20; // How many distances are taken into an average, which also means the time it takes.  

//Declare functions. 
 unsigned int measureDistance();
 void greenLed();
 void whiteLed();
 void redLed();
 void yellowLed();
 void offLed();
 int customAbs(int difference);
 void PrintGeneralInformation();
 unsigned int AverageDistance();
 void ReadValues();


void setup() {
  
  // Set up all the pinModes and the Serial Monitor. 
  Serial.begin(9600);
  pinMode(switchPin, INPUT);
  pinMode(overridePushbuttonPin, INPUT);
  pinMode(distancePushbuttonPin, INPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(sensitivityPotentiometerPin, INPUT);
   
}

void loop() {
  
  ReadValues();

  if (switchState) {

    PrintGeneralInformation();
    ReadValues();

    // If restart is true. That means we switched the device off. The new startTime should be the current time, and change reset back to false. 
    if (restart) {
      startTime = millis();
      restart = false;
    }

    whiteLed();

    if (distancePushbuttonState) {

      // If distancePushbutton is pressed, make the LED yellow, set restart to true, and save the distance they're at into averageDistance. 
      yellowLed();
      restart = true;
      setDistance = AverageDistance();

      // Error Checking. 
    Serial.print("DISTANCE RESET.  ");
    Serial.print("New Set Distance: ");
    Serial.print(setDistance);
    Serial.println(""); 

    distancePushbuttonState = 0; // Resets the distancePushbuttonState to 0. DO NOT DELETE THIS LINE. 

    }
    

    // If time passed is more than the study time.
    if (millis() - startTime >= studyTime) {
      
      // While time passed has not exceeded the break time. 
      while (millis() - startTime <= studyTime + breakTime) {  
         
        greenLed();
        ReadValues();

        // If pushbutton has been pressed or the switch is off, exit out of the break loop. 
        if (overridePushbuttonState || !switchState) { 
          Serial.println("Override Break PRESSED. ");
          break;
        }
        // End of break loop. 
      }
      // Set the start time to current time after we exit break loop. 
      startTime = millis(); 
    }

    AverageDistance();
    ReadValues();
    

  // If the distance is close or equal to the threshold, and it isn't a break, and switch is on. 

   while (customAbs(averageDistance - setDistance) >= closeThreshold && switchState && !(millis() - startTime >= studyTime) && !distancePushbuttonState) {

    // Make the LED red, remeasure distance, and check states. 
     redLed();
     AverageDistance();
     ReadValues(); 

    PrintGeneralInformation();
     
  }

  
// End of if switch is open. 
  }

// If the switch isn't open. 
  else {
    offLed();
    restart = true;
  }



}
  
  
// Function Definitions: 



unsigned int measureDistance() {

  digitalWrite(triggerPin, LOW);
  delay(2);
  digitalWrite(triggerPin, HIGH);
  delay(10);
  digitalWrite(triggerPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  return distance;
  
}

unsigned int AverageDistance() {

  for (int i = 0; i < AverageDistanceAccuracy; i += 1) {sumDistances += measureDistance(); ReadValues();}  // Measure distance x times. 

    averageDistance = sumDistances / AverageDistanceAccuracy; // Average distance is the sum of those distances / x. 
    sumDistances = 0;
    return averageDistance;
    
}


void ReadValues() {
  // Read Switch State and Override Pushbutton State. 
  switchState = digitalRead(switchPin);
  overridePushbuttonState = digitalRead(overridePushbuttonPin);

  // Set the distancePushbuttonState to 1 if it was pressed, which will stay 1 until we reset it again to 0. 
  if (digitalRead(distancePushbuttonPin)) {distancePushbuttonState = 1;}

  // Read analog value from potentiometer, and then map it to a threshold between min and max.  
  sensorValue = analogRead(sensitivityPotentiometerPin);
  closeThreshold = map(sensorValue, 0, 1023, minValue, maxValue);


}

void redLed() {

  analogWrite(redPin, 255);
  analogWrite(greenPin, 0);
  analogWrite(bluePin, 0);
}

  
void whiteLed() {

  analogWrite(redPin, 255);
  analogWrite(greenPin, 255);
  analogWrite(bluePin, 255);
}
    

void greenLed() {

  analogWrite(redPin, 0);
  analogWrite(greenPin, 255);
  analogWrite(bluePin, 0);
}

void offLed() {

  analogWrite(redPin, 0);
  analogWrite(greenPin, 0);
  analogWrite(bluePin, 0);
}


void yellowLed() {

  analogWrite(redPin, 255);
  analogWrite(greenPin, 200);
  analogWrite(bluePin, 0);
}

int customAbs(int difference) {

  if (difference < 0) {
    difference = -difference;
  }
  return difference;
}

void PrintGeneralInformation () {

  Serial.print("Current Distance: ");
  Serial.print(averageDistance);
  Serial.print("  Sensitivity: ");
  Serial.print(closeThreshold);
  Serial.print("  Time Elapsed: ");
  Serial.print(millis());
  Serial.print("  Start Time: ");
  Serial.print(startTime);
  Serial.print("  Distance Pushbutton: ");
  Serial.print(distancePushbuttonState);
  Serial.println("");

}






/* 

Test Cases:

Override Break Works. 
Reset distance works while Led is White and Red. 
Sensitivity Works while Led is White and Red. 
Time Tracking works fine. 

*/




