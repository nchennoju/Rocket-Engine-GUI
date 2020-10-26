// Read Pot Adjustable Analog Voltage
// Use External voltage source
// Wire Potentiomenter to potPin

const int potPin = A0;

void setup() {

  // Initiate serial Communications
  Serial.begin(9600);

}

// Code Start
void loop() {

  // Read Pot Value and Change from Integer to Volt Measurement
  int val = map(analogRead(potPin),0,1023,0,5);
  
  // Display Voltage in serial monitor
  Serial.println(val);

  // Delay for stability
  delay(1);

}
