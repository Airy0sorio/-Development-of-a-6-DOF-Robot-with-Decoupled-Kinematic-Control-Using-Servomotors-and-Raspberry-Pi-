import serial

class Connection_Serial:
    __isConnected = False
    __port = ""
    __baudrate = 9600
    __connection = None
    __onReceive = None

    def __init__(self, port, baudrate=9600):
        self.__port = port
        self.__baudrate = baudrate
        try:
            self.__connection = serial.Serial(port, baudrate)
            self.__isConnected = True
            print(f'Conectando al puerto: {port} con un baudrate de {baudrate}.')
        except serial.SerialException as e:
            print(f'Conectando al puerto: {port} con un baudrate de {baudrate}: {e}')
    
    def send(self, data):
        if self.__validate_data(data):
            print(f'Enviando datos por serial: {data}')
            self.__connection.write((data + '\n').encode())
        else:
            print('Formato invalido')

    def __validate_data(self, data):
        parts = data.split(',')
        return len(parts) == 6

    def stop(self):
        if self.__isConnected:
            self.__connection.close()
            self.__isConnected = False
            print(f'Desconectando del puerto: {self.__port}')
