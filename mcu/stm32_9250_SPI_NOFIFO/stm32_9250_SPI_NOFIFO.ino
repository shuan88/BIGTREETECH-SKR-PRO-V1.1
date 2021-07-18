#include "MPU9250.h"

// an MPU9250 object with the MPU-9250 sensor on I2C bus 0 with address 0x68
//MPU9250 IMU(Wire,0x68);
MPU9250 IMU(SPI,10);

int status;

void setup() {
  // serial to display data
  Serial.begin(500000);
  while(!Serial) {}

  // start communication with IMU 
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    while(1) {}
  }
  // setting the accelerometer full scale range to +/-8G 
  IMU.setAccelRange(MPU9250::ACCEL_RANGE_8G);
  // setting the gyroscope full scale range to +/-500 deg/s
  IMU.setGyroRange(MPU9250::GYRO_RANGE_500DPS);
  // setting DLPF bandwidth to 20 Hz
  IMU.setDlpfBandwidth(MPU9250::DLPF_BANDWIDTH_184HZ);
  // setting SRD to 19 for a 50 Hz update rate 
  IMU.setSrd(0); // (1000 / frequency) -1
}

void loop() {
  // read the sensor
  IMU.readSensor();
  // display the data
  Serial.print(String(String(IMU.getAccelX_mss(),6)+"," + String(IMU.getAccelY_mss(),6) +","  + String(IMU.getAccelZ_mss(),6) +"\n"));
//delayMicroseconds(1);
}
