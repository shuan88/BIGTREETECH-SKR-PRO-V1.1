#include "MPU9250.h"

// an MPU9250 object with the MPU-9250 sensor on SPI bus 0 and chip select pin 10
MPU9250FIFO IMU(SPI,10);
//MPU9250FIFO IMU(Wire,0x68);

int status;

// variables to hold FIFO data, these need to be large enough to hold the data
float ax[100], ay[100], az[100];
size_t fifoSize;

void setup() {
  // serial to display data
//  Serial.begin(115200);
  Serial.begin(500000);
  while(!Serial) {}

  // start communication with IMU 
  status = IMU.begin();
  if (status < 0) {
    Serial.println("IMU initialization unsuccessful");
    Serial.println(status);
    while(1) {}
  }
  // setting DLPF bandwidth to 184 Hz
  IMU.setDlpfBandwidth(MPU9250::DLPF_BANDWIDTH_184HZ);
  // setting SRD to 19 for a 50 Hz update rate
  IMU.setSrd(1);
  // enabling the FIFO to record just the accelerometers
  //IMU.enableFifo(true,false,false,false);
  
  IMU.enableFifo(false,true,false,false);
  
  // enabling the FIFO to record just the accelerometers  
//  IMU.enableFifo(false,false,true,false);
  // gather 50 samples of data
  delay(10);
  // read the fifo buffer from the IMU
  while(1){
    IMU.readFifo();
    
//    get the X, Y, and Z accelerometer data and their size
//    IMU.getFifoAccelX_mss(&fifoSize,ax);
//    IMU.getFifoAccelY_mss(&fifoSize,ay);
//    IMU.getFifoAccelZ_mss(&fifoSize,az);


//    getFifoGyroX_rads
    IMU.getFifoGyroX_rads(&fifoSize,ax);
    IMU.getFifoGyroX_rads(&fifoSize,ay);
    IMU.getFifoGyroX_rads(&fifoSize,az);

//    getFifoMagX_uT 
//    IMU.getFifoMagX_uT(&fifoSize,ax);
//    IMU.getFifoMagY_uT(&fifoSize,ay);
//    IMU.getFifoMagY_uT(&fifoSize,az);
    
    // print the data
    for (size_t i=0; i < fifoSize; i++) {
        Serial.print(String(String(ax[i],6)+"," + String(ay[i],6) +","  + String(az[i],6) +"\n"));
    }
    delay(5);

  }
}

void loop() {}
