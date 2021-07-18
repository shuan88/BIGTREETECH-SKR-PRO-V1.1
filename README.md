# MPU 9250數據擷取

###### tags: `TE`

---

* [雲端資料夾](https://drive.google.com/drive/folders/1gK3bhSXd41HmCHAkCUYq4XbA05TIExSr)
* [Grove-IMU 10DOF v2.0](https://wiki.seeedstudio.com/cn/Grove-IMU_10DOF_v2.0/)
* [MPU-9250 datasheet](https://files.seeedstudio.com/wiki/Grove-IMU_10DOF/res/MPU-9250A_Product_Specification.pdf)
* [ESP32-Arduino-MPU9250](https://github.com/yelvlab/ESP32-Arduino-MPU9250)
* [9250API 說明](https://github.com/introlab/OpenIMU-MiniLogger/blob/master/Firmware-Arduino/lib/MPU9250/src/MPU9250.h)
* [OpenIMU-MiniLogger](https://github.com/introlab/OpenIMU-MiniLogger/blob/master/Firmware-Arduino/lib/MPU9250/src/MPU9250.h)
* [STM32 Arduino IDE](https://github.com/stm32duino/Arduino_Core_STM32#nucleo-144-boards)
* [Linkit COM消失](https://oranwind.org/-linkit-smart-7688-com-port-xiao-shi/)
* [Serial reconnect](https://stackoverflow.com/questions/32071581/serial-com-port-reconnect-on-windows)
* [孟軒報告](https://hackmd.io/YB9GOCShQ-2sNFaGiWxI8A)
* [How to find all serial devices](https://stackoverflow.com/questions/2530096/how-to-find-all-serial-devices-ttys-ttyusb-on-linux-without-opening-them)
* [ESP32 pin](https://i.imgur.com/RhIS8LC.png)
* [Jetson pin](https://www.rs-online.com/designspark/jetson-nano-40-pin-gpio-cn)
* [inux平台串口调试工具](https://www.waveshare.net/study/article-888-1.html)
* [ESP32 TX2 RX2](https://www.chosemaker.com/board/esp32/lesson-12/)

---

# 買Sensor
* [维特智能三轴加速度计ADXL357传感器模块串口输出原装进口ADXL355
](https://detail.tmall.com/item.htm?id=622930184269&spm=a1z0k.7385961.1997985097.d4918997.7f084771uKKKjB&_u=t2dmg8j26111)
* [维特智能ADXL375三轴加速度计ADXL345模块姿态传感器高量程200g
](https://detail.tmall.com/item.htm?spm=a220o.1000855.0.0.31926e96yttHrH&id=620796197088&scm=1007.12776.82642.100200300000000&pvid=b7d63994-5d0e-402f-929e-7309990e4e72&skuId=4413150513898)
* [ADXL375 蝦皮](https://shopee.tw/%E2%99%97%E7%B6%AD%E7%89%B9%E6%99%BA%E8%83%BDADXL375%E4%B8%89%E8%BB%B8%E5%8A%A0%E9%80%9F%E5%BA%A6%E8%A8%88ADXL345%E6%A8%A1%E5%A1%8A%E5%A7%BF%E6%85%8B%E5%82%B3%E6%84%9F%E5%99%A8%E9%AB%98%E9%87%8F%E7%A8%8B200g-i.428438781.11112204807)
* [Mega 腳位](https://i.imgur.com/JfFu178.png)


---

# Websocket

* [API Reference AsyncWebSocket](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/protocols/esp_websocket_client.html#esp-websocket-client)
* [linkit ws](https://oranwind.org/-linkit-smart-7688-tou-guo-websocket-chuan-song-sensing-data-dao-iot-studio/)
* [ArduinoWebsockets](https://github.com/gilmaimon/ArduinoWebsockets)
* [esp32 ws](https://blog.csdn.net/Naisu_kun/article/details/107164844)

----


error messages 
``` log
21:01:10.547 -> ERROR: Too many messages queued
21:01:10.580 -> ERROR: Too many messages queued
21:02:44.028 -> ws[/][1] error(1007): ⸮?⸮?
21:02:44.028 -> ws[/][1] disconnect: 150994941
```

----

# Muti Data Read SPI 

``` c
#include "MPU9250.h"
//https://reurl.cc/xGXQe4https://reurl.cc/xGXQe4
// an MPU9250 object with the MPU-9250 sensor on SPI bus 0 and chip select pin 10
MPU9250FIFO IMU(SPI,5);
//MPU9250FIFO IMU(Wire,0x68);
int status;
// variables to hold FIFO data, these need to be large enough to hold the data
float ax[100], ay[100], az[100];
size_t fifoSize;
const int buttonPin = 17;     // the number of the pushbutton pin
const int VoutPin = 16 ;      // the number of the Vout pin

int buttonState = 0;         // variable for reading the pushbutton status


void setup() {
  // serial to display data
//  Serial.begin(250000);
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
  IMU.setAccelRange(MPU9250::ACCEL_RANGE_8G); //2,4,8,16
//   setting the gyroscope full scale range to +/-500 deg/s
  IMU.setGyroRange(MPU9250::GYRO_RANGE_500DPS); //250,500,1000,2000
//   setting DLPF bandwidth to 184 Hz
  IMU.setDlpfBandwidth(MPU9250::DLPF_BANDWIDTH_184HZ); //184,92,41,20,10,5
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
      delay(5);    
    }
  }
  
}

//    getFifoMagX_uT 
//    IMU.getFifoMagX_uT(&fifoSize,ax);
//    IMU.getFifoMagY_uT(&fifoSize,ay);
//    IMU.getFifoMagZ_uT(&fifoSize,az);
```




