int m1Pin11 = 13;
int m1Pin12 = 12;
int m2Pin21 = 14;
int m2Pin22 = 27;
int ir1 = 19;
int ir2 = 15;
int obstaclesense1;
int obstaclesense2;

void setup()
{
    pinMode(m1Pin11, OUTPUT);
    pinMode(m1Pin12, OUTPUT);
    pinMode(m2Pin21, OUTPUT);
    pinMode(m2Pin22, OUTPUT);
    pinMode(ir1, INPUT);
    pinMode(ir2, INPUT);
}
void loop()
{
    obstaclesense1 = digitalRead(ir1);
    obstaclesense2 = digitalRead(ir2);
    // LEFT WHEEL
    left();
    // right wheel
    right();
    // straight
    straight();
    // backward
    backward();
}
void straight()
{
    // straight
    if (obstaclesense1 == 0 && obstaclesense2 == 0)
    {
        digitalWrite(m1Pin11, LOW);
        digitalWrite(m1Pin12, HIGH);
        digitalWrite(m2Pin21, LOW);
        digitalWrite(m2Pin22, HIGH);
        delay(250);
    }
}

void right()
{
    if (obstaclesense1 == 0 && obstaclesense2 == 1)
    {
        digitalWrite(m1Pin11, HIGH);
        digitalWrite(m1Pin12, LOW);
        digitalWrite(m2Pin21, LOW);
        digitalWrite(m2Pin22, HIGH);
        delay(250);
    }
}

void left()
{
    if (obstaclesense1 == 1 && obstaclesense2 == 0)
    {
        digitalWrite(m1Pin11, LOW);
        digitalWrite(m1Pin12, HIGH);
        digitalWrite(m2Pin21, HIGH);
        digitalWrite(m2Pin22, LOW);
        delay(250);
    }
}

void backward()
{
    // backward
    if (obstaclesense1 == 1 && obstaclesense2 == 1)
    {
        digitalWrite(m1Pin11, HIGH);
        digitalWrite(m1Pin12, LOW);
        digitalWrite(m2Pin21, HIGH);
        digitalWrite(m2Pin22, LOW);
        delay(250);
    }
}


// Python Code: 
// import RPi.GPIO as GPIO 
// import time 
 
// # Define GPIO pins 
// m1Pin11 = 13 
// m1Pin12 = 12 
// m2Pin21 = 14 
// m2Pin22 = 27 
// ir1 = 19 
// ir2 = 15 
 
// # Setup GPIO mode and pins 
// GPIO.setmode(GPIO.BCM) 
 
// GPIO.setup(m1Pin11, GPIO.OUT) 
// GPIO.setup(m1Pin12, GPIO.OUT) 
// GPIO.setup(m2Pin21, GPIO.OUT) 
// GPIO.setup(m2Pin22, GPIO.OUT) 
// GPIO.setup(ir1, GPIO.IN) 
// GPIO.setup(ir2, GPIO.IN) 
 
// try: 
//     while True: 
//         # Read sensor values 
//         obstaclesense1 = GPIO.input(ir1) 
//         obstaclesense2 = GPIO.input(ir2) 
 
//         # Conditionally control the motors 
//         if obstaclesense1 == 0 and obstaclesense2 == 0:  # Both sensors clear 
//             GPIO.output(m1Pin11, GPIO.LOW) 
//             GPIO.output(m1Pin12, GPIO.HIGH) 
//             GPIO.output(m2Pin21, GPIO.LOW) 
//             GPIO.output(m2Pin22, GPIO.HIGH) 
//             time.sleep(0.25) 
 
//         elif  obstaclesense1  ==  0  and  obstaclesense2  ==  1:    #  Only  second sensor detects obstacle 
//             GPIO.output(m1Pin11, GPIO.HIGH) 
//             GPIO.output(m1Pin12, GPIO.LOW) 
//             GPIO.output(m2Pin21, GPIO.LOW) 
//             GPIO.output(m2Pin22, GPIO.HIGH) 
//             time.sleep(0.25) 
 
//         elif obstaclesense1 == 1 and obstaclesense2 == 0:  # Only first sensor detects obstacle 
//             GPIO.output(m1Pin11, GPIO.LOW) 
//             GPIO.output(m1Pin12, GPIO.HIGH) 
//             GPIO.output(m2Pin21, GPIO.HIGH) 
//             GPIO.output(m2Pin22, GPIO.LOW) 
//             time.sleep(0.25) 
 
//         elif  obstaclesense1  ==  1 and obstaclesense2  ==  1:    #  Both  sensors detect obstacle 
//             GPIO.output(m1Pin11, GPIO.HIGH) 
//             GPIO.output(m1Pin12, GPIO.LOW) 
//             GPIO.output(m2Pin21, GPIO.HIGH) 
//             GPIO.output(m2Pin22, GPIO.LOW) 
//             time.sleep(0.25) 
 
// except KeyboardInterrupt: 
//     print("Program stopped by user") 
// finally: 
//     GPIO.cleanup()