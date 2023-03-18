#include <Arduino.h>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

#define LED 2
#define STEP_X 32 
#define STEP_Y 33 
#define DIR_X 25 
#define DIR_Y 26 
#define M0_Y 12 
#define M1_Y 14
#define M2_Y 27

int silnikSpeed = 0;

std::vector<string> split(const string &s, char delim) 
{
    vector<string> tokens;
    stringstream ss(s);
    string item;
    while (std::getline(ss, item, delim)) 
    {
        tokens.push_back(item);
    }
    return tokens;
}

void setup() 
{
  Serial.begin(115200);
  Serial.setTimeout(1000); //to do fucking remove this
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
  String result = " ";
  if (Serial.available() > 0) 
  {
    result =  Serial.readStringUntil('\n');
    vector<string> chuj = split(string(result.c_str()), ' ');
    if(!chuj[0].compare("AIM"))
    { 
      silnikSpeed = atoi(chuj[1].c_str());
    }
  }
  
  if(silnikSpeed)
  {
    digitalWrite(STEP_X, HIGH);
    digitalWrite(STEP_Y, HIGH);
    delayMicroseconds(silnikSpeed);
    digitalWrite(STEP_X, LOW);
    digitalWrite(STEP_Y, LOW);
    delayMicroseconds(silnikSpeed);
  }
}
