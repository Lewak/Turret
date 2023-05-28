#include <Arduino.h>
#include <vector>
#include <string>
#include "utils.h"
#include "hal.h"
#include "serialCommunication.h"
using namespace std;

#define LED 2
#define STEP_X 32
#define STEP_Y 33
#define DIR_X 25
#define DIR_Y 26
#define M0_Y 12
#define M1_Y 14
#define M2_Y 27
#define MOT_ANG_MIN_DEG 5
#define MOT_ANG_MAX_DEG 175

int motorSpeed = 0;
int desiredAngle = 0;

void setup()
{
    serialInit();
    halInit();
    pinMode(LED, OUTPUT);
    pinMode(M0_Y, OUTPUT);
    pinMode(M1_Y, OUTPUT);
    pinMode(M2_Y, OUTPUT);
    pinMode(STEP_X, OUTPUT);
    pinMode(STEP_Y, OUTPUT);
    pinMode(DIR_X, OUTPUT);
    pinMode(DIR_Y, OUTPUT);

    digitalWrite(DIR_X, HIGH);
    digitalWrite(DIR_Y, HIGH);
    digitalWrite(M0_Y, HIGH);
    digitalWrite(M1_Y, HIGH);
    digitalWrite(M2_Y, HIGH);
}

void loop()
{
    double angle = readAngle();
    serialRead([](string code, vector<int> parameters){

        if (code == "AIM")
        {
            motorSpeed = parameters[0];
        }
        else if (code == "SET")
        {
            desiredAngle = clampValue(parameters[0], MOT_ANG_MIN_DEG, MOT_ANG_MAX_DEG);
            Serial.print("New Angle: ");                                                                                                    
            Serial.println(desiredAngle);

        }});
       
    if ((desiredAngle < angle - 0.2) || (desiredAngle > angle + 0.2))
    {
        if (desiredAngle - angle > 0)
            digitalWrite(DIR_Y, LOW);
        else
            digitalWrite(DIR_Y, HIGH);
        digitalWrite(STEP_X, HIGH);
        digitalWrite(STEP_Y, HIGH);
        delayMicroseconds(motorSpeed);
        digitalWrite(STEP_X, LOW);
        digitalWrite(STEP_Y, LOW);
        delayMicroseconds(motorSpeed);
    }
}

