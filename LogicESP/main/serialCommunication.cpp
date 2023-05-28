#include <Arduino.h>
#include <vector>
#include <string>
#include "utils.h"
#include <functional>
using namespace std;
void serialInit() 
{
    Serial.begin(115200);
}
void serialRead(function<void(string, vector<int> )>callback)  
{
    if (Serial.available() > 0)
    {
        String result = Serial.readStringUntil('\n');
        vector<string> inputString = split(string(result.c_str()), ' ');
        vector<string> subvector(inputString.begin() + 1, inputString.end());
        vector<int> intSubvector;
        for (string &i:subvector)
        {
            intSubvector.push_back(atoi(i.c_str()));
        }
        callback (inputString[0], intSubvector);
    }
}

