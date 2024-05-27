import numpy as np
from scipy.spatial.transform import Rotation as R
class Cinematica_directa:
    __data : str
    __vec_pos_euler : list[float]

    def __init__(self,data : str, ):
        self.l1 = 20
        self.l2 = 20
        self.l3 = 15
        self.l4 = 10
        self.DH_d = [self.l1, 0, 0, self.l3, 0, self.l4]
        self.DH_a = [0, self.l2, 0, 0, 0, 0]
        self.DH_alfa = [np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0]
        self.__data = data
        self.__vec_pos_euler = [0 , 0 , 0 , 0 , 0 , 0]
        np.set_printoptions(suppress=True, precision=4)
        self.main()

        
    def getV_euler(self):
        return self.__vec_pos_euler
    
    def matriz_tranformacion_homogenea(self,data):
        As = []
        for i, t in enumerate(data):
            dh_d, dh_a, dh_alfa = self.DH_d[i], self.DH_a[i], self.DH_alfa[i]
            A = np.array([
                [np.cos(t), -np.sin(t) * np.cos(dh_alfa), np.sin(t) * np.sin(dh_alfa), dh_a * np.cos(t)],
                [np.sin(t), np.cos(t) * np.cos(dh_alfa), -np.cos(t) * np.sin(dh_alfa), dh_a * np.sin(t)],
                [0, np.sin(dh_alfa), np.cos(dh_alfa), dh_d],
                [0, 0, 0, 1]
            ])
            As.append(A)
        MTH0_6 = np.linalg.multi_dot(As)
        #print(MTH0_6)
        return MTH0_6
    
    def calculo_euler(self, MTH):
        #Vector posicion 
        Vec_pos = MTH[:3, 3]
        #Matriz de rotacion de la MTH0_6
        MTH_R = MTH[:3, :3]
        # Crear un objeto de rotación a partir de la matriz de rotación
        r = R.from_matrix(MTH_R)
        # Obtener los ángulos de Euler
        angles = r.as_euler('ZXZ', degrees=True)  # 'ZXZ' representa la secuencia de los ángulos de Euler
        return Vec_pos,angles
    
    def main(self):
        try:
            data = list(map(float, self.__data.split()))
            # Convertir los ángulos de grados a radianes
            data = np.radians(data)
            MTH0_6_calculada = self.matriz_tranformacion_homogenea(data)
            Vec_pos, angles = self.calculo_euler(MTH0_6_calculada)
            self.__vec_pos_euler = list(Vec_pos) + list(angles)
        except Exception as e:
            print(f"Error: {e}. Por favor, asegúrese de que los datos estén correctamente formateados y sean números válidos.")