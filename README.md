# Implementación de Brazo Robótico de 6GDL Controlado por App Móvil
Este proyecto presenta la implementación de un brazo robótico de 6 grados de libertad (6GDL) controlado por una aplicación móvil. El brazo fue programado en Python y se comunica vía Bluetooth con la aplicación, permitiendo al usuario seleccionar entre dos modos de operación: cinemática directa y cinemática inversa. En el modo de cinemática directa, el usuario ingresa un vector de valores para cada GDL y el sistema devuelve un vector de ángulos de Euler. En el modo de cinemática inversa, el usuario ingresa un vector de ángulos de Euler y el sistema devuelve un vector de ángulos para cada GDL.


- **Autor:** Mario Airy Hernandez Osorio
- **Institución:** Universidad Autónoma de Querétaro (UAQ)
- **Curso:** Robótica
- **Instructor:** Dr. Gerardo Pérez Soto
- **Año:** 2024-1
---

\begin{tabular}{cccccc}
\toprule
\textbf{art} & $\boldsymbol{\theta_i}$ & $\boldsymbol{d_i}$ & $\boldsymbol{a_i}$ & $\boldsymbol{\alpha_i}$ \\
\midrule
1 & $\theta_1$ & $l_1$ & 0 & $\frac{\pi}{2}$ \\
2 & $\theta_2$ & 0 & $l_2$ & 0 \\
3 & $\theta_3$ & 0 & 0 & $\frac{\pi}{2}$ \\
4 & $\theta_4$ & $l_3$ & 0 & $-\frac{\pi}{2}$ \\
\bottomrule
\end{tabular}

---
# 2. Descripcion de los codigos

## 2.1 Principal
Nombre del Codigo "main.py"
### Funcionalidad
Este código actúa como el controlador principal para un brazo robótico de 6 grados de libertad (6GDL), permitiendo su operación y control mediante una conexión Bluetooth desde una aplicación móvil. Facilita dos modos de operación clave: cinemática directa y cinemática inversa.

### Características
- Comunicación Bluetooth: Permite la comunicación bidireccional entre la aplicación móvil y el controlador del brazo robótico.
- Modo de Cinemática Directa: Transforma un vector de entrada en ángulos de Euler para posicionar el brazo robótico.
- Modo de Cinemática Inversa: Calcula ángulos de Euler a partir de un vector de entrada para configurar los grados de libertad del brazo.
- Verificación de Ángulos: Asegura que los ángulos calculados estén dentro del rango operativo antes de enviarlos al brazo.
- Integración Serial: Utiliza comunicación serial para enviar comandos de posición al brazo robótico.
- Interfaz con Aplicación Móvil: Gestiona la recepción de datos desde la aplicación móvil y envía los resultados de vuelta según el modo de operación seleccionado.

## 2.2 Gestión de Comunicación Bluetooth 
Nombre del Codigo "BT.py"
### Funcionalidad
Este código proporciona funcionalidades para establecer y gestionar la comunicación Bluetooth entre un controlador y una aplicación móvil para controlar un brazo robótico. Permite actuar tanto como cliente como servidor Bluetooth según las necesidades de conexión.

### Características
- Modo Cliente y Servidor: Puede operar como cliente o servidor Bluetooth dependiendo de la configuración inicial.
- Recepción y Envío de Datos: Capaz de recibir y enviar datos a través de la conexión Bluetooth.
- Notificación de Conexión: Informa sobre cambios en el estado de la conexión Bluetooth.
- Interfaz de Callback: Utiliza una función de callback (onRecive) para manejar los datos recibidos.
- Envío de Datos Recibidos: En modo cliente, automáticamente reenvía los datos recibidos.
- Detención de Servicio: Permite detener el servidor Bluetooth cuando sea necesario.

---
## Clonar repositorio
Para crear una copia del proyecto puedes utilizar:

```
git clone [https://github.com/Airy0sorio/Robotica_2024_1_Airy](https://github.com/Airy0sorio/-Development-of-a-6-DOF-Robot-with-Decoupled-Kinematic-Control-Using-Servomotors-and-Raspberry-Pi)
```
---

## Instrucciones para ejecutar los archivos en Python

Este repositorio contiene archivos Python para ejecutar diversas funciones. Para hacerlo de manera efectiva, se recomienda utilizar el editor de código Visual Studio Code (VSCode).

### Requisitos previos
Antes de ejecutar los programas, sigue estos pasos:

1. **Instalación de Python:**
   Asegúrate de tener Python instalado, se recomienda la versión 3.11.8.

2. **Creación de una carpeta de proyecto:**
   Crea una carpeta donde se guardarán los archivos y recursos del proyecto.

3. **Creación de un entorno virtual:**
   Abre la terminal integrada de VSCode y ejecuta el siguiente comando para crear un entorno virtual:
   ```
   python -m venv ./env
   ```

4. **Activación del entorno virtual:**
Activa el entorno virtual con el siguiente comando:
    ```
   .env\Scripts\activate
    ```

5. **Instalación de las librerías:**
Instala las librerías utilizadas en el proyecto ejecutando el siguiente comando:
    ```
   pip install -r requirements.txt
    ```

6.**Ejecución del programa**
Una vez configurado el entorno, puedes ejecutar el programa escribiendo el siguiente comando en la terminal:    
    
    python Nombre_del_archivo.py
    
    
Para futuras ejecuciones, simplemente activa el entorno virtual y ejecuta el archivo Python que deseas correr. 
Los pasos 4 y 6 son suficientes para ejecutar cualquier código adicional.

---
## Video de demostración

[Ver el video en YouTube](https://youtu.be/IZDzBegQsG4)
