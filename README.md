# Productor consumidor
### Elaborado por Trinidad González Alan Isaac.
#
## :computer: El codigo primero crea un buffer el cual tiene una capacidad máxima de 10 elementos. El programa crea dos hilos consumidores (c1 y c2) y un hilo productor (p). Los hilos consumidores consumen recursos del buffer y los hilos productores generan recursos y los colocan en el buffer de nuevo, utilizamos un objeto de condición para sincronizar los hilos y asi los consumidores esperan en la condición cuando el buffer está vacío, y el productor espera en la condición cuando el buffer está lleno. Una vez que el productor ha generado todos los recursos le notifica a los consumidores que los recursos están disponibles, mientras que los consumidores consumen los recursos y si el buffer está vacío después del consumo notifican al productor que hay más espacio disponible.
#
## :computer: Al compilar y ejecutar el programa podemos ver como se generan los recursos y como se consumen:
![Captura de pantalla de la compilación y ejecución del archivo servidor.py](https://github.com/AlanX-Lan/Productor-consumidor/blob/main/Screenshots/1.png)
#
![Captura de pantalla de la compilación y ejecución del archivo cliente.py](https://github.com/AlanX-Lan/Productor-consumidor/blob/main/Screenshots/2.png)
#
![Captura de pantalla de la consola del archivo servidor.py](https://github.com/AlanX-Lan/Productor-consumidor/blob/main/Screenshots/3.png)
#
![Captura de pantalla de la consola del archivo servidor.py](https://github.com/AlanX-Lan/Productor-consumidor/blob/main/Screenshots/4.png)
#
![Captura de pantalla de la consola del archivo servidor.py](https://github.com/AlanX-Lan/Productor-consumidor/blob/main/Screenshots/5.png)
