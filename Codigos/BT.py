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
