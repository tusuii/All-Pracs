// Define motor control pins
int m11 = 13;
int m12 = 12;
int m21 = 14;
int m22 = 27;

// Define IR sensor pins
int ir_1 = 26;
int ir_2 = 25;

// Variables to store sensor readings
int obsense1;
int obsense2;

void setup()
{
    // Set motor control pins as outputs
    pinMode(m11, OUTPUT);
    pinMode(m12, OUTPUT);
    pinMode(m21, OUTPUT);
    pinMode(m22, OUTPUT);

    // Set IR sensor pins as inputs
    pinMode(ir_1, INPUT);
    pinMode(ir_2, INPUT);
}

void loop()
{
    // Read sensor values
    obsense1 = digitalRead(ir_1);
    obsense2 = digitalRead(ir_2);

    // Decision making based on sensor readings
    if (obsense1 == HIGH && obsense2 == LOW)
    {
        // Turn right to adjust position
        digitalWrite(m11, HIGH);
        digitalWrite(m12, LOW);
        digitalWrite(m21, LOW);
        digitalWrite(m22, HIGH);
    }
    else if (obsense1 == LOW && obsense2 == HIGH)
    {
        // Turn left to adjust position
        digitalWrite(m11, LOW);
        digitalWrite(m12, HIGH);
        digitalWrite(m21, HIGH);
        digitalWrite(m22, LOW);
    }
    else if (obsense1 == LOW && obsense2 == LOW)
    {
        // Move forward if both sensors are off the edge
        digitalWrite(m11, HIGH);
        digitalWrite(m12, LOW);
        digitalWrite(m21, HIGH);
        digitalWrite(m22, LOW);
    }
    else
    {
        // Stop if both sensors detect the edge or are off
        digitalWrite(m11, LOW);
        digitalWrite(m12, LOW);
        digitalWrite(m21, LOW);
        digitalWrite(m22, LOW);
    }
}

// PYTHON CODE 
// import RPi.GPIO as GPIO 
// import time 
 
// # Define motor control pins (GPIO numbering) 
// m11 = 17 
// m12 = 18 
// m21 = 27 
// m22 = 22 
 
// # Define IR sensor pins (GPIO numbering) 
// ir_1 = 26 
// ir_2 = 25 
 
// # Initialize GPIO settings 
// GPIO.setmode(GPIO.BCM) 
// GPIO.setup(m11, GPIO.OUT) 
// GPIO.setup(m12, GPIO.OUT) 
// GPIO.setup(m21, GPIO.OUT) 
// GPIO.setup(m22, GPIO.OUT) 
// GPIO.setup(ir_1, GPIO.IN) 
// GPIO.setup(ir_2, GPIO.IN) 
 
// def stop_motors(): 
//     GPIO.output(m11, GPIO.LOW) 
//     GPIO.output(m12, GPIO.LOW) 
//     GPIO.output(m21, GPIO.LOW) 
//     GPIO.output(m22, GPIO.LOW) 
 
// try: 
//     while True: 
//         # Read sensor values 
//         obsense1 = GPIO.input(ir_1) 
//         obsense2 = GPIO.input(ir_2) 
 
//         # Decision making based on sensor readings 
//         if obsense1 == GPIO.HIGH and obsense2 == GPIO.LOW: 
//             # Turn right to adjust position 
//             GPIO.output(m11, GPIO.HIGH) 
//             GPIO.output(m12, GPIO.LOW) 
//             GPIO.output(m21, GPIO.LOW) 
//             GPIO.output(m22, GPIO.HIGH) 
//         elif obsense1 == GPIO.LOW and obsense2 == GPIO.HIGH: 
//             # Turn left to adjust position 
//             GPIO.output(m11, GPIO.LOW) 
//             GPIO.output(m12, GPIO.HIGH) 
//             GPIO.output(m21, GPIO.HIGH) 
//             GPIO.output(m22, GPIO.LOW) 
//         elif obsense1 == GPIO.LOW and obsense2 == GPIO.LOW: 
//             # Move forward if both sensors are off the edge 
//             GPIO.output(m11, GPIO.HIGH) 
//             GPIO.output(m12, GPIO.LOW) 
//             GPIO.output(m21, GPIO.HIGH) 
//             GPIO.output(m22, GPIO.LOW) 
//         else: 
//             # Stop if both sensors detect the edge or are off 
//             stop_motors() 
 
//             time.sleep(0.1)  # Adjust delay as needed for your application 
 
// except KeyboardInterrupt: 
//     print("Stopping the program...") 
// finally: 
//     GPIO.cleanup() 
