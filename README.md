# Implementación de Brazo Robótico de 6GDL Controlado por App Móvil
Este proyecto presenta la implementación de un brazo robótico de 6 grados de libertad (6GDL) controlado por una aplicación móvil. El brazo fue programado en Python y se comunica vía Bluetooth con la aplicación, permitiendo al usuario seleccionar entre dos modos de operación: cinemática directa y cinemática inversa. En el modo de cinemática directa, el usuario ingresa un vector de valores para cada GDL y el sistema devuelve un vector de ángulos de Euler. En el modo de cinemática inversa, el usuario ingresa un vector de ángulos de Euler y el sistema devuelve un vector de ángulos para cada GDL.


- **Autor:** Mario Airy Hernandez Osorio
- **Institución:** Universidad Autónoma de Querétaro (UAQ)
- **Curso:** Robótica
- **Instructor:** Dr. Gerardo Pérez Soto
- **Año:** 2024-1

---
# Descripcion de los codigos
## 1.1 Principal
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



---
  
## Video de demostración

[Ver el video en YouTube](https://youtu.be/IZDzBegQsG4)
