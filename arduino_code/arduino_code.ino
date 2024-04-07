#include <Servo.h>

// Create a servo object for each ESC
Servo esc1;
Servo esc2;
Servo esc3;
Servo esc4;

// Define ESC control pins
int escPins[] = {8, 9, 10, 11}; // Example pins, adjust as needed

// Variables for serial communication
String inputString = "";         // A String to hold incoming data
boolean stringComplete = false;  // Whether the string is complete

void setup() {
  Serial.begin(9600);

  // Attach each ESC to its respective pin
  esc1.attach(escPins[0]);
  esc2.attach(escPins[1]);
  esc3.attach(escPins[2]);
  esc4.attach(escPins[3]);

  // Initialize all ESCs to neutral (1500 microseconds)
  esc1.writeMicroseconds(1490);
  delay(5000); // Wait a bit after sending the arm signal
  esc2.writeMicroseconds(1500);
  delay(5000); // Wait a bit after sending the arm signal
  esc3.writeMicroseconds(1500);
  delay(5000); // Wait a bit after sending the arm signal
  esc4.writeMicroseconds(1500);
  delay(5000); // Wait a bit after sending the arm signal
}

void loop() {
  if (stringComplete) {
    if (inputString.startsWith("<[") && inputString.endsWith("]>")) {
      // Extract and parse the integers
      int pwmValues[4]; // Array to hold the parsed PWM values
      int startIdx = 2; // Start after "<["
      for (int i = 0; i < 4; i++) {
        int endIdx = inputString.indexOf("]", startIdx);
        if (endIdx != -1) {
          pwmValues[i] = inputString.substring(startIdx, endIdx).toInt();
          startIdx = endIdx + 2; // Move past the "]" and to the start of the next number
        }
      }

      // Update ESCs with the new PWM values
      esc1.writeMicroseconds(pwmValues[0]);
      esc2.writeMicroseconds(pwmValues[1]);
      esc3.writeMicroseconds(pwmValues[2]);
      esc4.writeMicroseconds(pwmValues[3]);

      // Echo the PWM values back for confirmation
      Serial.print("<[");
      for (int i = 0; i < 4; i++) {
        Serial.print(pwmValues[i]);
        if (i < 3) Serial.print("][");
      }
      Serial.println("]>");

      // Reset the input string and the complete flag
      inputString = "";
      stringComplete = false;
    }
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputString += inChar;
    if (inChar == '>') {
      stringComplete = true;
    }
  }
}
