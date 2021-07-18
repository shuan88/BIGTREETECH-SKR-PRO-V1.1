#include "MPU9250.h"
//https://reurl.cc/xGXQe4https://reurl.cc/xGXQe4
// an MPU9250 object with the MPU-9250 sensor on SPI bus 0 and chip select pin 10
MPU9250FIFO IMU(SPI,10);
//MPU9250FIFO IMU(Wire,0x68);
int status;
// variables to hold FIFO data, these need to be large enough to hold the data
float ax[100], ay[100], az[100];
size_t fifoSize;
const int buttonPin = 9;     // the number of the pushbutton pin
const int VoutPin = 8 ;      // the number of the Vout pin

int buttonState = 0;         // variable for reading the pushbutton status


void setup() {
  // serial to display data
//  Serial.begin(115200);
  Serial.begin(500000);
  pinMode(buttonPin, INPUT);
  pinMode(VoutPin, OUTPUT);
  digitalWrite(VoutPin, HIGH);
  
  while(!Serial) {}

  // start communication with IMU 
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    Serial.println(status);
    while(1) {}
  }
  
//     setting the accelerometer full scale range to +/-8G 
  IMU.setAccelRange(MPU9250::ACCEL_RANGE_8G);
//   setting the gyroscope full scale range to +/-500 deg/s
  IMU.setGyroRange(MPU9250::GYRO_RANGE_500DPS);
//   setting DLPF bandwidth to 184 Hz
  IMU.setDlpfBandwidth(MPU9250::DLPF_BANDWIDTH_20HZ);
//   setting SRD to 19 for a 50 Hz update rate
  IMU.setSrd(0);

}

void loop() {
  buttonState = digitalRead(buttonPin);
  if (buttonState == 0) {
    Serial.print("enabling the FIFO to record just the GYRO");
  ////   enabling the FIFO to record just the GYRO
    IMU.enableFifo(false,true,false,false);
    delay(10);
    while(1){
  //  read the fifo buffer from the IMU
      IMU.readFifo();
      //  getFifoGyroX_rads
      IMU.getFifoGyroX_rads(&fifoSize,ax);
      IMU.getFifoGyroY_rads(&fifoSize,ay);
      IMU.getFifoGyroZ_rads(&fifoSize,az);
      //  print the data
      for (size_t i=0; i < fifoSize; i++) {
          Serial.print(String(String(ax[i],6)+"," + String(ay[i],6) +","  + String(az[i],6) +"\n"));
      }
//      delay(5);    
    }
  }

  else{
    Serial.print("enabling the FIFO to record just the accelerometers");
  //  enabling the FIFO to record just the accelerometers
    IMU.enableFifo(true,false,false,false);
    delay(10);
    while(1){
  //  read the fifo buffer from the IMU
      IMU.readFifo();
  //    get the X, Y, and Z accelerometer data and their size
      IMU.getFifoAccelX_mss(&fifoSize,ax);
      IMU.getFifoAccelY_mss(&fifoSize,ay);
      IMU.getFifoAccelZ_mss(&fifoSize,az);
      //  print the data
      for (size_t i=0; i < fifoSize; i++) {
          Serial.print(String(String(ax[i],6)+"," + String(ay[i],6) +","  + String(az[i],6) +"\n"));
      }
//      delay(5);    
    }
  }
  
}

//    getFifoMagX_uT 
//    IMU.getFifoMagX_uT(&fifoSize,ax);
//    IMU.getFifoMagY_uT(&fifoSize,ay);
//    IMU.getFifoMagZ_uT(&fifoSize,az);
