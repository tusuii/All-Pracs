// Define motor pins
int motorPin1 = 32;
int motorPin2 = 33;
int motorPin3 = 25;
int motorPin4 = 26;

// Define IR sensor pins
int irSensorPinLeft = 37;
int irSensorPinRight = 14;

void setup()
{
    Serial.begin(9600);

    // Motor pins setup
    pinMode(motorPin1, OUTPUT);
    pinMode(motorPin2, OUTPUT);
    pinMode(motorPin3, OUTPUT);
    pinMode(motorPin4, OUTPUT);

    // IR sensor pins setup
    pinMode(irSensorPinLeft, INPUT);
    pinMode(irSensorPinRight, INPUT);
}

void loop()
{

    int sensorValueLeft = digitalRead(irSensorPinLeft);
    int sensorValueRight = digitalRead(irSensorPinRight);

    Serial.print("Left Sensor: ");
    Serial.print(sensorValueLeft);
    Serial.print(" | Right Sensor: ");
    Serial.println(sensorValueRight);

    // Determine line-following behavior based on sensor readings
    if (sensorValueLeft == LOW && sensorValueRight == LOW)
    {
        // Neither sensor detects the line, stop or take corrective action

        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, LOW);
    }
    else if (sensorValueLeft == LOW && sensorValueRight == HIGH)
    {

        // Only right sensor detects the line, adjust left to turn left
        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, LOW);
        digitalWrite(motorPin4, HIGH);
    }
    else if (sensorValueLeft == HIGH && sensorValueRight == LOW)
    {

        // Only left sensor detects the line, adjust right to turn right
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin2, HIGH);
        digitalWrite(motorPin3, HIGH);
        digitalWrite(motorPin4, LOW);
    }
    else if (sensorValueLeft == HIGH && sensorValueRight == HIGH)
    {

        // Both sensors detect the line, move forward
        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin2, LOW);
        digitalWrite(motorPin3, HIGH);
        digitalWrite(motorPin4, LOW);
    }
    delay(100);
}


// Python Code: 
// import RPi.GPIO as GPIO 
// import time 
 
// # Define GPIO pins 
// motorPin1 = 17  # Example GPIO pin numbers; adjust as per your wiring 
// motorPin2 = 18 
// motorPin3 = 27 
// motorPin4 = 22 
// irSensorPinLeft = 37 
// irSensorPinRight = 14 
 
// # Setup GPIO mode and pins 
// GPIO.setmode(GPIO.BCM) 
// GPIO.setup(motorPin1, GPIO.OUT) 
// GPIO.setup(motorPin2, GPIO.OUT) 
// GPIO.setup(motorPin3, GPIO.OUT) 
// GPIO.setup(motorPin4, GPIO.OUT) 
// GPIO.setup(irSensorPinLeft, GPIO.IN) 
// GPIO.setup(irSensorPinRight, GPIO.IN) 
 
// try: 
//     while True: 
//         # Read sensor values 
 
//         sensorValueLeft = GPIO.input(irSensorPinLeft) 
//         sensorValueRight = GPIO.input(irSensorPinRight) 
         
//         # Print sensor readings (optional) 
//         print(f"Left Sensor: {sensorValueLeft} | Right Sensor: {sensorValueRight}") 
 
//         # Determine line-following behavior based on sensor readings 
//         if sensorValueLeft == GPIO.LOW and sensorValueRight == GPIO.LOW: 
//             # Neither sensor detects the line, stop or take corrective action 
//             GPIO.output(motorPin1, GPIO.LOW) 
//             GPIO.output(motorPin2, GPIO.LOW) 
//             GPIO.output(motorPin3, GPIO.LOW) 
//             GPIO.output(motorPin4, GPIO.LOW) 
 
//         elif sensorValueLeft == GPIO.LOW and sensorValueRight == GPIO.HIGH: 
//             # Only right sensor detects the line, adjust left to turn left 
//             GPIO.output(motorPin1, GPIO.HIGH) 
//             GPIO.output(motorPin2, GPIO.LOW) 
//             GPIO.output(motorPin3, GPIO.LOW) 
//             GPIO.output(motorPin4, GPIO.HIGH) 
 
//         elif sensorValueLeft == GPIO.HIGH and sensorValueRight == GPIO.LOW: 
//             # Only left sensor detects the line, adjust right to turn right 
//             GPIO.output(motorPin1, GPIO.LOW) 
//             GPIO.output(motorPin2, GPIO.HIGH) 
//             GPIO.output(motorPin3, GPIO.HIGH) 
//             GPIO.output(motorPin4, GPIO.LOW) 
 
//         elif sensorValueLeft == GPIO.HIGH and sensorValueRight == GPIO.HIGH: 
//             # Both sensors detect the line, move forward 
//             GPIO.output(motorPin1, GPIO.HIGH) 
//             GPIO.output(motorPin2, GPIO.LOW) 
//             GPIO.output(motorPin3, GPIO.HIGH) 
//             GPIO.output(motorPin4, GPIO.LOW) 
 
//         time.sleep(0.1)  # Adjust delay as needed 
 
// except KeyboardInterrupt: 
//     print("Program stopped by user") 
// finally: 
//     GPIO.cleanup() 
