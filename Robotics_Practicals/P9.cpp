#include <Servo.h>
// Define servo objects
Servo panServo;
Servo tiltServo;
// Define servo pin numbers
int panPin = 21;  // Example GPIO pin for pan servo
int tiltPin = 22; // Example GPIO pin for tilt servo

void setup()
{
    // Attach servo objects to respective pins
    panServo.attach(panPin);
    tiltServo.attach(tiltPin);
}

void loop()
{
    // Example usage: move pan servo to 90 degrees
    panServo.write(90);
    delay(1000); // Wait for 1 second

    // Example usage: move tilt servo to 45 degrees
    tiltServo.write(45);
    delay(1000); // Wait for 1 second

    // Add more movements or control logic as needed
    // Loop will repeat continuously
}
