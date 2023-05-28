#include <Arduino.h>
#include <vector>
#include <string>
#include "utils.h"
#include <functional>
void serialInit();
void serialRead(function<void(string, vector<int> )>callback);
