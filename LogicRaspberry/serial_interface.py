import serial


class Serial:
    serial0: serial.Serial = None

    @staticmethod
    def initialise():
        uartPort = '/dev/serial0'
        baudRate = 115200  # Set your baud rate
        Serial.serial0 = serial.Serial(uartPort, baudRate)

    @staticmethod
    def sendMessage(message: str):
        Serial.serial0.write(message.encode('utf-8'))

    @staticmethod
    def destroy():
        Serial.serial0.close()

