void setup() 
{
   Serial.begin(9600);
   pinMode(14, OUTPUT);
   pinMode(21, OUTPUT);
   pinMode(15, OUTPUT);

   digitalWrite(14, LOW);   
   digitalWrite(21, LOW);
   digitalWrite(15, HIGH);
}

void loop() 
{
    delayMicroseconds(50);
    digitalWrite(15, LOW);
    delayMicroseconds(50);
    digitalWrite(15, HIGH);
}
