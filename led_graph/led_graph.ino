/*

*/

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void convertAmplitudeToLight(float amplitude) {
  float MAX_AMPLITUDE = 10;
  int on_time = 1;
  int off_time = MAX_AMPLITUDE / amplitude - 1;
  
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(on_time);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(off_time); 
}

void loop() {
  convertAmplitudeToLight(1);
}

