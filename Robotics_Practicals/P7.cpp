#include "BluetoothSerial.h"
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run make menuconfig to and enable it
#endif
int m11 = 13;
int m12 = 12;
int m21 = 14;
int m22 = 27;
BluetoothSerial SerialBT;

void forward()
{
    digitalWrite(m11, LOW);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, LOW);
    digitalWrite(m22, HIGH);
    // delay(3000);
}

void stops()
{
    // stop
    digitalWrite(m11, LOW);
    digitalWrite(m12, LOW);
    digitalWrite(m21, LOW);
    digitalWrite(m22, LOW);
    // delay(1300);
}

void left()
{
    // LEFT
    digitalWrite(m11, LOW);
    digitalWrite(m12, LOW);
    digitalWrite(m21, LOW);
    digitalWrite(m22, HIGH);
    delay(200);
}

void right()
{
    // rIGHT
    digitalWrite(m11, LOW);
    digitalWrite(m12, HIGH);
    digitalWrite(m21, LOW);
    digitalWrite(m22, LOW);
    delay(200);
}
void reverse()
{
    digitalWrite(m11, HIGH);
    digitalWrite(m12, LOW);
    digitalWrite(m21, HIGH);
    digitalWrite(m22, LOW);
    delay(300);
}
void setup()
{
    pinMode(m11, OUTPUT);
    pinMode(m12, OUTPUT);
    pinMode(m21, OUTPUT);
    pinMode(m22, OUTPUT);
    Serial.begin(115200);
    SerialBT.begin("ESP32test"); // Bluetooth device name
    Serial.println("The device started, now you can pair it with bluetooth!");
    // pinMode(LED_BUILTIN, OUTPUT);
}
char keyvalue;
void loop()
{
    if (SerialBT.available())
    {
        keyvalue = SerialBT.read();
        // SerialBT.write(keyvalue.toString);
        Serial.println(keyvalue);
        if (keyvalue == 'F' || keyvalue == 'f' || keyvalue == 'U')
        {
            Serial.println("Foward Movement.....");
            digitalWrite(m11, LOW);
            digitalWrite(m12, HIGH);
            digitalWrite(m21, LOW);
            digitalWrite(m22, HIGH);
        }
        if (keyvalue == 'L' || keyvalue == 'l')
        {
            Serial.println("Left Movement.....");
            left();
        }
        if (keyvalue == 'R' || keyvalue == 'r')
        {
            Serial.println("right Movement.....");
            right();
        }
        if (keyvalue == 'B' || keyvalue == 'b' || keyvalue == 'D')
        {
            Serial.println("Backward Movement.....");
            reverse();
        }
        if (keyvalue == 'S' || keyvalue == 's')
        {
            Serial.println("Stop Movement.....");
                stops();
        }
    }
    // delay(20);
}

// Python Code: 
// import bluetooth 
// import RPi.GPIO as GPIO 
// import time 
 
 
// # Define GPIO pins for motor control 
// m11 = 13 
// m12 = 12 
// m21 = 14 
// m22 = 27 
 
 
// # Setup GPIO mode 
// GPIO.setmode(GPIO.BCM) 
// GPIO.setup(m11, GPIO.OUT) 
// GPIO.setup(m12, GPIO.OUT) 
// GPIO.setup(m21, GPIO.OUT) 
// GPIO.setup(m22, GPIO.OUT) 
 
// # Bluetooth setup 
// server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM) 
// port = 1 
// server_socket.bind(("", port)) 
// server_socket.listen(1) 
 
// print("Waiting for Bluetooth connection on RFCOMM channel", port) 
 
// client_socket, address = server_socket.accept() 
// print("Accepted connection from", address) 
 
// def forward(): 
//     GPIO.output(m11, GPIO.LOW) 
//     GPIO.output(m12, GPIO.HIGH) 
//     GPIO.output(m21, GPIO.LOW) 
//     GPIO.output(m22, GPIO.HIGH) 
 
// def stops(): 
//     GPIO.output(m11, GPIO.LOW) 
//     GPIO.output(m12, GPIO.LOW) 
//     GPIO.output(m21, GPIO.LOW) 
//     GPIO.output(m22, GPIO.LOW) 
 
// def left(): 
//     GPIO.output(m11, GPIO.LOW) 
//     GPIO.output(m12, GPIO.LOW) 
//     GPIO.output(m21, GPIO.LOW) 
//     GPIO.output(m22, GPIO.HIGH) 
//     time.sleep(0.2) 
//     stops() 
 
 
// def right(): 
//     GPIO.output(m11, GPIO.LOW) 
//     GPIO.output(m12, GPIO.HIGH) 
//     GPIO.output(m21, GPIO.LOW) 
//     GPIO.output(m22, GPIO.LOW) 
//     time.sleep(0.2) 
//     stops() 
 
// def reverse(): 
//     GPIO.output(m11, GPIO.HIGH) 
//     GPIO.output(m12, GPIO.LOW) 
//     GPIO.output(m21, GPIO.HIGH) 
//     GPIO.output(m22, GPIO.LOW) 
//     time.sleep(0.3) 
//     stops() 
 
 
// try: 
//     while True: 
//         data = client_socket.recv(1024).decode().strip() 
//         print("Received:", data) 
        
//         if data == 'F' or data == 'f' or data == 'U': 
//         print("Forward Movement...") 
//         forward() 
//         elif data == 'L' or data == 'l': 
//         print("Left Movement...") 
//         left() 
//         elif data == 'R' or data == 'r': 
//         print("Right Movement...") 
//         right() 
//         elif data == 'B' or data == 'b' or data == 'D': 
//         print("Backward Movement...") 
//         reverse() 
//         elif data == 'S' or data == 's': 
//         print("Stop Movement...") 
        
//         stops() 
    
// except KeyboardInterrupt: 
//     print("Keyboard interrupt detected, closing connections...") 
//     client_socket.close() 
//     server_socket.close() 
//     GPIO.cleanup()