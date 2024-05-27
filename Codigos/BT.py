from bluedot.btcomm import BluetoothServer, BluetoothClient

class BT:
    __isClient = False
    __deviceName = ""
    __connection = None
    __onRecive = None
    def __init__(self, deviceName,onRecive = None, serverName = None):
        self.__deviceName = deviceName
        self.__onRecive = onRecive
        if serverName != None:
            self.__connection = BluetoothClient(serverName, self.__receive)
            self.__isClient = True
        else :
            self.__connection = BluetoothServer(self.__receive, power_up_device=True, when_client_connects=self.notify_connection, when_client_disconnects=self.notify_connection)
            self.__isClient = False

    def __receive(self, data):
        print(f'Receiving data in {self.__deviceName}: {data}')
        if self.__onRecive != None:
            self.__onRecive(data)
        if self.__isClient:
            self.__connection.send(data)

    def notify_connection(self):
        print("Connection status changed")
    
    
    def send(self, data):
        print(f'Sending data from {self.__deviceName}')
        self.__connection.send(data)

    def stop(self):
        if isinstance(self.__connection, BluetoothServer):
            self.__connection.stop()
        return

# # from serial import Serial
# # import time

# # class BT:
# #     __serial: Serial

# #     def __init__(self, puerto: str, tasa_tranferencia: int):
# #         self.__serial = Serial(puerto, tasa_tranferencia)
# #         time.sleep(2)  # Esperar a que se establezca la conexión

# #     def send(self, message: str):  # Mensaje en formato de envío
# #         self.__serial.write(message.encode())
# #         time.sleep(0.2)

# #     def read(self) -> str:
# #         response = self.__serial.readline().decode().strip()
# #         if response:
# #             return response
# #         else:
# #             raise Exception("Error de datos")

# #region bt
# from bluedot.btcomm import BluetoothClient
# from desacoplo import RoboticArm

# # Variable global para almacenar el valor recibido y el valor a enviar
# Vec_pos_euler = None
# Angulos = None

# def dato_recibido(data):
#     global Vec_pos_euler
#     Vec_pos_euler = data.strip()
#     print(f"Mensaje recibido: {Vec_pos_euler}")
#     if Vec_pos_euler:
#         rm = RoboticArm(Vec_pos_euler)
#         angulos = rm.getAngulos()
#         print(f"Ángulos calculados: {angulos}")
#         global Angulos
#         Angulos = " ".join(map(str, angulos))

# def main():
#     # Crear el servidor Bluetooth
#     server = BluetoothClient._read(dato_recibido)
#     print("Servidor Bluetooth iniciado. Esperando mensajes...")
#     input("Presiona Enter para detener el servidor...\n")

#     # Procesar el mensaje recibido si hay alguno
#     if Vec_pos_euler and Angulos:
#         server.send(Angulos)

# if __name__ == "__main__":
#     main()
