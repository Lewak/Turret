#include <Arduino.h>

#define LED 2
#define STEP_X 32 
#define STEP_Y 33 
#define DIR_X 25 
#define DIR_Y 26 

void setup() {
  Serial.begin(115200);
  pinMode(LED, OUTPUT);
  pinMode(STEP_X, OUTPUT);
  pinMode(STEP_Y, OUTPUT);
  pinMode(DIR_X, OUTPUT);
  pinMode(DIR_Y, OUTPUT);
  digitalWrite(DIR_X, HIGH);
  digitalWrite(DIR_Y, HIGH);
}

void loop() {
  digitalWrite(STEP_X, HIGH);
  digitalWrite(STEP_Y, HIGH);
  Serial.println("step on");
  delay(1);
  digitalWrite(STEP_X, LOW);
  digitalWrite(STEP_Y, LOW);
  Serial.println("step off");
  delay(1);
}
