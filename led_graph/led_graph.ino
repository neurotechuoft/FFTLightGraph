/*

*/

void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
}

void convertAmplitudeToLight(int amplitude) {
//  int MAX_AMPLITUDE = 10;
//  int on_time = 1;
//  int off_time = MAX_AMPLITUDE / amplitude - 1;

//  for (int i = 0; i < 1000; i++) {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(amplitude);                       // wait for a second
//    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
//    delay(off_time);
//  }
}

void loop() {
//  Serial.write(Serial.read());
  if (Serial.available()) {
    int amplitude = Serial.parseInt();
    convertAmplitudeToLight(amplitude);
//    Serial.read();
//    digitalWrite(LED_BUILTIN, HIGH);
//    delay(50);
  }
  else {
    digitalWrite(LED_BUILTIN, LOW);
    delay(50);
  }
}

