int m11 = 33;
int m12 = 25;
int m21 = 26;
int m22 = 27;

void setup()
{
    pinMode(m11, OUTPUT);
    pinMode(m12, OUTPUT);
    pinMode(m21, OUTPUT);
    pinMode(m22, OUTPUT);
}

void loop()
{
    forward();
    delay(3000);

    right();
    delay(500);

    forward();
    delay(3000);

    right();
    delay(500);

    forward();
    delay(3000);

    right();
    delay(500);

    forward();
    delay(3000);

    right();
    delay(500);

    forward();
    delay(3000);

    right();
    delay(500);

    forward();
    delay(3000);

    right();
    delay(500);

    forward();
    delay(3000);
    motorstop();
    delay(3000);
}

void forward()
{
    digitalWrite(m11, LOW);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, LOW);
    digitalWrite(m22, HIGH);
}

void right()
{
    digitalWrite(m11, LOW);
    digitalWrite(m12, LOW);
    digitalWrite(m21, HIGH);
    digitalWrite(m22, HIGH);
}

void motorstop()
{
    digitalWrite(m11, HIGH);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, HIGH);
    digitalWrite(m22, HIGH);
}



// Python Code: 
// import RPi.GPIO as GPIO 
// importtime 
 
// # Define GPIO pins for motor control 
// m11 = 33 
// m12 = 25 
// m21 = 26 
// m22 = 27 
 
// # Setup GPIO mode 
// GPIO.setmode(GPIO.BCM) 
// GPIO.setup(m11, GPIO.OUT) 
// GPIO.setup(m12, GPIO.OUT) 
// GPIO.setup(m21, GPIO.OUT) 
// GPIO.setup(m22, GPIO.OUT) 
 
 
// def forward(): 
// GPIO.output(m11, GPIO.LOW) 
// GPIO.output(m12, GPIO.HIGH) 
// GPIO.output(m21, GPIO.LOW) 
// GPIO.output(m22, GPIO.HIGH) 
 
 
// def right(): 
// GPIO.output(m11, GPIO.LOW) 
// GPIO.output(m12, GPIO.LOW) 
// GPIO.output(m21, GPIO.HIGH) 
// GPIO.output(m22, GPIO.HIGH) 
 
 
// def motorstop(): 
// GPIO.output(m11, GPIO.HIGH) 
// GPIO.output(m12, GPIO.HIGH) 
// GPIO.output(m21, GPIO.HIGH) 
// GPIO.output(m22, GPIO.HIGH) 
 
// try: 
//     while True: 
//         forward() 
//         time.sleep(3) 
//         right() 
//         time.sleep(0.5) 
        
//         forward() 
//         time.sleep(3) 
//         right() 
//         time.sleep(0.5) 
        
//         forward() 
//         time.sleep(3) 
//         right() 
//         time.sleep(0.5) 
        
//         forward() 
//         time.sleep(3) 
//         right() 
//         time.sleep(0.5) 
        
//         forward() 
//         time.sleep(3) 
//         right() 
//         56 
        
//         time.sleep(0.5) 
        
        
//         forward() 
//         time.sleep(3) 
//         right() 
//         time.sleep(0.5) 
        
//         forward() 
//         time.sleep(3) 
//         motorstop() 
//         time.sleep(3) 
        
 
// except KeyboardInterrupt: 
//     print("Program interrupted, cleaning up GPIO...") 
//     GPIO.cleanup()