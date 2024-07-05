// Write a suitable program to show working of motors in Tinkercad
    // Code :
    // C++ code
    //
int m11 = 11;
int m12 = 10;
int m21 = 7;
int m22 = 6;
int led1 = 8;
int led2 = 9;

void setup()
{
    pinMode(m11, OUTPUT);
    pinMode(m12, OUTPUT);
    pinMode(m21, OUTPUT);
    pinMode(m22, OUTPUT);
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
}

void loop()
{
    // Forward
    digitalWrite(m11, HIGH);
    digitalWrite(m12, LOW);
    digitalWrite(m21, HIGH);
    digitalWrite(m22, LOW);
    digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    delay(5000);

    // Backward
    digitalWrite(m11, LOW);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, LOW);
    digitalWrite(m22, HIGH);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    delay(5000);

    // Left
    digitalWrite(m11, LOW);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, HIGH);
    digitalWrite(m22, LOW);
    digitalWrite(led1, HIGH);
    digitalWrite(led2, LOW);
    delay(5000);

    // Right
    digitalWrite(m11, HIGH);
    digitalWrite(m12, LOW);
    digitalWrite(m21, LOW);
    digitalWrite(m22, HIGH);
    digitalWrite(led1, LOW);
    digitalWrite(led2, HIGH);
    delay(5000);

    // Stop
    digitalWrite(m11, HIGH);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, HIGH);
    digitalWrite(m22, HIGH);
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    delay(5000);
}