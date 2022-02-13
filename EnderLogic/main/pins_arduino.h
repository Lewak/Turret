// ATMEL ATMEGA644/ATMEGA1284 / SANGUINO
//
//                        +---\/---+
//            (D 0) PB0  1|        |40  PA0 (AI 0 / D31)
//            (D 1) PB1  2|        |39  PA1 (AI 1 / D30)
//       INT2 (D 2) PB2  3|        |38  PA2 (AI 2 / D29)
//        PWM (D 3) PB3  4|        |37  PA3 (AI 3 / D28)
//     SS PWM (D 4) PB4  5|        |36  PA4 (AI 4 / D27)
//       MOSI (D 5) PB5  6|        |35  PA5 (AI 5 / D26)
//       MISO (D 6) PB6  7|        |34  PA6 (AI 6 / D25)
//        SCK (D 7) PB7  8|        |33  PA7 (AI 7 / D24)
//                  RST  9|        |32  AREF
//                  VCC 10|        |31  GND
//                  GND 11|        |30  AVCC
//                XTAL2 12|        |29  PC7 (D 23)
//                XTAL1 13|        |28  PC6 (D 22)
//       RX0 (D 8)  PD0 14|        |27  PC5 (D 21) TDI
//       TX0 (D 9)  PD1 15|        |26  PC4 (D 20) TDO
//  INT0 RX1 (D 10) PD2 16|        |25  PC3 (D 19) TMS
//  INT1 TX1 (D 11) PD3 17|        |24  PC2 (D 18) TCK
//       PWM (D 12) PD4 18|        |23  PC1 (D 17) SDA
//       PWM (D 13) PD5 19|        |22  PC0 (D 16) SCL
//       PWM (D 14) PD6 20|        |21  PD7 (D 15) PWM
//                        +--------+

#ifndef pins_arduino_h
#define pins_arduino_h

#define PA0 (31)
#define PA1 (30)
#define PA2 (29)
#define PA3 (28)
#define PA4 (27)
#define PA5 (26)
#define PA6 (25)
#define PA7 (24)

#define PB0 (0)
#define PB1 (1)
#define PB2 (2)
#define PB3 (3)
#define PB4 (4)
#define PB5 (5)
#define PB6 (6)
#define PB7 (7)

#define PC0 (16)
#define PC1 (17)
#define PC2 (18)
#define PC3 (19)
#define PC4 (20)
#define PC5 (21)
#define PC6 (22)
#define PC7 (23)

#define PD0 (8)
#define PD1 (9)
#define PD2 (10)
#define PD3 (11)
#define PD4 (12)
#define PD5 (13)
#define PD6 (14)
#define PD7 (15)


#define SD_SS (PA0)
#define LCD_SCK (PA1)
#define EXT_A2 (PA2)
#define LCD_CS (PA3)
#define Beeper (PA4)
#define ZENABLE (PA5)
#define BEDTEMP (PA6)
#define ENDTEMP (PA7)

#define E_DIR (PB0)
#define E_STEP (PB1)
#define Z_DIR (PB2)
#define Z_STEP (PB3)
#define FAN (PB4)
#define MOSI (PB5)
#define MISO (PB6)
#define SCLK (PB7)

#define Encoder_Button (PC0)
#define LCD_MOSI (PC1)
#define X_STOP (PC2)
#define Y_STOP (PC3)
#define Z_STOP (PC4)
#define X_DIR (PC5)
#define Y_STEP (PC6)
#define Y_DIR (PC7)

#define AIFO (PD0)
#define AOFI (PD1)
#define Encoder_A (PD2)
#define Encoder_B (PD3)
#define Hotbed (PD4)
#define Hotend (PD5)
#define XYEENABLE (PD6)
#define X_STEP (PD7)

#endif
