# Atari 2600 PlusCart-Pico

## Description
Atari 2600 PlusCart-Pico is a porting on Al-Nafuur [PlusCart](https://github.com/Al-Nafuur/United-Carts-of-Atari) to Raspberry Pi Pico platform. 

## Features
- SD card support for ROMs
- on-board flash storage (1MB or 16MB) for ROMs
- Internet access and WiFi connection (with ESP8266)
- [PlusROM](http://pluscart.firmaplus.de/pico/?PlusROM) support
- [PlusStore](https://pcart.firmaplus.de/pico/?PlusStore) support

## Hardware
PlusCart-Pico consists of these modules:
- Raspberry Pi Pico (purple version is recommended due to more pins available)
  
  <img src="https://github.com/gtortone/PlusCart-Pico/blob/main/images/rpi-pico.jpg" height="180" width="200" />
  <img src="https://github.com/gtortone/PlusCart-Pico/blob/main/images/rpi-purple.jpg" height="180" width="200" />

- Atari 2600 cartridge breakout board:

  <img src="https://github.com/gtortone/PlusCart-Pico/blob/main/images/atari.png" height="180" width="200" />

  
- ESP8266-01

  <img src="https://github.com/gtortone/PlusCart-Pico/blob/main/images/esp8266.jpg" width="200" />
  
- SD card breakout board

  <img src="https://github.com/gtortone/PlusCart-Pico/blob/main/images/microsd.jpg" width="200" />
  
- USB UART (optional for debugging purposes)

  <img src="https://github.com/gtortone/PlusCart-Pico/blob/main/images/usb-uart.jpg" width="200" />

### Connections

| RPi Pico pin | module pin |
| ------------- | ------------- |
| GP2...GP14 | cartridge bus ADDR[0...12] |
| GP22...GP29 | cartridge bus DATA[0...7] |
| GP16...GP19 | microSD (MISO, CS, SCK, MOSI) |
| GP0, GP1, GP15 | ESP8266 (TX, RX, RST) |
| GP20, GP21 | USB-UART (RX, TX) |

RPi Pico connections are defined in [board.h](https://github.com/gtortone/PlusCart-Pico/blob/main/include/board.h) 

### Build

Development environment is based on PlatformIO with two board profiles: `pico` and `vccgnd_yd_rp2040`. At first build all dependency library and whole development environment will be automatically installed and configured by PlatformIO.

Start the build:
```
pio run -e vccgnd_yd_rp2040
  or
pio run -e pico
```

Upload firmware on board:
``` 
pio run -e vccgnd_yd_rp2040 -t upload
  or
pio run -e pico -t upload
```


