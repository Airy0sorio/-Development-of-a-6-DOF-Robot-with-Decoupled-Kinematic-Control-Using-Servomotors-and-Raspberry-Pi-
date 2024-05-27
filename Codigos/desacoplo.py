import numpy as np
from scipy.spatial.transform import Rotation as R

class RoboticArm:
    __data : str
    __angulos : list[float]

    def __init__(self,data : str, ):
        self.l1 = 20
        self.l2 = 20
        self.l3 = 15
        self.l4 = 10
        self.DH_d = [self.l1, 0, 0, self.l3, 0, self.l4]
        self.DH_a = [0, self.l2, 0, 0, 0, 0]
        self.DH_alfa = [np.pi/2, 0, np.pi/2, -np.pi/2, np.pi/2, 0]
        self.__data = data
        self.__angulos = [0 , 0 , 0 , 0 , 0 , 0]
        np.set_printoptions(suppress=True, precision=4)
        self.main()

    def getAngulos(self):
        return self.__angulos
    def round_to_significant(self, value, threshold=1e-5, significants=[90]):
        degrees = float(np.degrees(value))
        return "{:.3f}".format(degrees)
    
    #region calcular matriz trandormacion 
    def calcular_matriz_transformacion0_6(self):
        Px, Py, Pz, alfa, beta, gamma = map(float, self.__data.split())
        angles_degrees = [alfa, beta, gamma]
        rotation = R.from_euler('ZXZ', angles_degrees, degrees=True)
        R_total = rotation.as_matrix()
        T = np.array([Px, Py, Pz])
        H = np.eye(4)
        H[:3, :3] = R_total
        H[:3, 3] = T
        Va = H[:3, 2] 
        Vs = self.l4 * Va
        return H, T, Vs

    # region angulos articulaciones 1 a 3
    def angulos_articulacion1_3(self, Vpos_0_6, Vs):
        Px, Py, Pz = (Vpos_0_6[0] - Vs[0]), (Vpos_0_6[1] - Vs[1]), (Vpos_0_6[2] - Vs[2])
        th1 = np.arctan2(Py, Px)
        u = Py / np.cos(th1)
        v = self.l1 - Pz
        m = u**2 + v**2 + self.l2**2 - self.l3**2 
        n = 2 * self.l2 * v
        p = -2 * self.l2 * u
        a = m - p
        b = 2 * n
        c = m + p
        th2_1 = 2 * np.arctan2(-b + np.sqrt(b**2 - 4 * a * c), (2 * a)) 
        th2_2 = 2 * np.arctan2(-b - np.sqrt(b**2 - 4 * a * c), (2 * a))
        th3yth2_1 = np.arctan2(u - self.l2 * np.cos(th2_1), v + self.l2 * np.sin(th2_1))
        th3_1 = th3yth2_1 - th2_1
        th3yth2_2 = np.arctan2(u - self.l2 * np.cos(th2_2), v + self.l2 * np.sin(th2_2))
        th3_2 = th3yth2_2 - th2_2
        return [th1, th2_1, th3_1], [th1, th2_2, th3_2]

    def calcular_matriz_tranformacion0_3(self, MTH0_6, ths1_3):
        As = []
        for i, t in enumerate(ths1_3):
            dh_d, dh_a, dh_alfa = self.DH_d[i], self.DH_a[i], self.DH_alfa[i]
            A = np.array([
                [np.cos(t), -np.sin(t) * np.cos(dh_alfa), np.sin(t) * np.sin(dh_alfa), dh_a * np.cos(t)],
                [np.sin(t), np.cos(t) * np.cos(dh_alfa), -np.cos(t) * np.sin(dh_alfa), dh_a * np.sin(t)],
                [0, np.sin(dh_alfa), np.cos(dh_alfa), dh_d],
                [0, 0, 0, 1]
            ])
            As.append(A)
        MTH0_3 = np.linalg.multi_dot(As)
        R0_3 = MTH0_3[:3, :3]
        R0_6 = MTH0_6[:3, :3]
        R4_6 = np.transpose(R0_3) @ R0_6
        return MTH0_3, R4_6

    def angulos_articulacion4_6(self, R3_6):
        th4 = np.arctan2(R3_6[1, 2], R3_6[0, 2])
        th5 = np.arccos(R3_6[2, 2])
        th6 = np.arctan2(R3_6[2, 1], -R3_6[2, 0])

        return self.round_to_significant(th4), self.round_to_significant(th5), self.round_to_significant(th6)

    def main(self):
        try:
            MTH0_6, Vpos_0_6, Vs = self.calcular_matriz_transformacion0_6()
            ths1_3_1, ths1_3_2 = self.angulos_articulacion1_3(Vpos_0_6, Vs)
            # print("\nAngulos th1, th2 y th3 para la primera solucion:")
            # print("th1:", np.degrees(ths1_3_1[0]))
            # print("th2:", np.degrees(ths1_3_1[1]))
            # print("th3:", np.degrees(ths1_3_1[2]))

            # print("\nAngulos th1, th2 y th3 para la segunda solucion:")
            # print("th1:", np.degrees(ths1_3_2[0]))
            # print("th2:", np.degrees(ths1_3_2[1]))
            # print("th3:", np.degrees(ths1_3_2[2]))

            MTH0_3, R4_6 = self.calcular_matriz_tranformacion0_3(MTH0_6, ths1_3_1)
            ths4_6 = self.angulos_articulacion4_6(R4_6)
            # print("\nAngulo th4:", ths4_6[0])
            # print("Angulo th5:", ths4_6[1])
            # print("Angulo th6:", ths4_6[2])
            self.__angulos = [np.degrees(ths1_3_1[0]),np.degrees(ths1_3_1[1]),np.degrees(ths1_3_1[2]),float(ths4_6[0]),float(ths4_6[1]),float(ths4_6[2])]
        except Exception as e:
            print(f"Error: {e}. Por favor, asegúrese de que los datos estén correctamente formateados y sean números válidos.")

