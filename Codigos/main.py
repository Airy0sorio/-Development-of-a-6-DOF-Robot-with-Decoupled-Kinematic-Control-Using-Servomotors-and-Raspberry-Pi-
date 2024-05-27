# #region codigo con bluetooth
from BT import BT
from serial import Connection_Serial
from desacoplo import RoboticArm as RM
#from Servo import Servo
#from ServoSignaler import ServoSignaler
from Cinematica_directa import Cinematica_directa as CD
#GDL1 = Servo(17)
port = '/dev/ttyUSB0'
serial = Connection_Serial(port)
def verificar_angulos(angulos):
    # Verificar si algún ángulo está fuera del rango de 0 a 180 grados
    for angle in angulos:
        if angle < 0 or angle > 180:
            return False
    return True
def main():
    bluetoothClient = None
    def reciveData(data):
        #Data recive puede ser:
        #	Ve # # # # # # #
        #	Sr # # # # # # #
        recive = data.split()
        key = recive.pop(0)
        vec =  " ".join(str(i) for i in recive)        
        print(key)
        print(recive)
        if key == "Ve":    
            roboticArm =  RM(vec)
            angulos = roboticArm.getAngulos()
            dataSend = angulos
            print (angulos)
            if not verificar_angulos(angulos):
                print("Alerta: Al menos uno de los ángulos está fuera del rango permitido (0-180 grados)")
            else:
                print("Todos los ángulos están dentro del rango permitido (0-180 grados)")
                #----------------------------------------------------
                serial.send(angulos)
                #   Aqui van servos.py

                #----------------------------------------------------
            
        elif key == "Sr":
            cd = CD(vec)
            ang = vec.split()
            vec_euler_obtenido = cd.getV_euler()
            dataSend = vec_euler_obtenido
            
            print(vec_euler_obtenido)
            #print(ang[0])
            #---------------------------------------- #
            #GDL1.move(float(ang[0]))
            serial.send(vec)
            #-----------------------------------------#
            
        else:
            print("Accion no valida")
            
        if bluetoothClient != None:
            bluetoothClient.send(" ".join(str(i) for i in dataSend) )
            
    bluetoothClient  = BT("Raspberry PI",reciveData)
    
if __name__ == "__main__":
    main()
