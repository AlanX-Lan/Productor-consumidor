# Elaborado por Trinidad González Alan Isaac
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-2s) %(message)s'
                    )

BUFFER_SIZE = 10  # Buffer de 10 elementos
buffer = []  # Buffer para almacenar los recursos generados/consumidos

def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Iniciando hilo consumidor')
    with cond:
        while True:
            while len(buffer) == 0:  # Si el buffer está vacío
                logging.debug('El buffer está vacío. Esperando recursos...')
                cond.wait()  # Espera a que haya recursos disponibles en el buffer
            resource = buffer.pop(0)
            logging.debug('El consumidor ha utilizado el recurso: %s', resource)
            if len(buffer) == 0:
                logging.debug('El buffer está vacío. Notificando a los productores.')
                cond.notify_all()
            time.sleep(1)  # Tiempo para simular el procesamiento del recurso

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Iniciando el hilo productor')
    with cond:
        while True:
            while len(buffer) >= BUFFER_SIZE:
                logging.debug('El buffer está lleno. Esperando espacio...')
                cond.wait()  # Esperar a que haya espacio disponible en el buffer
            for i in range(1, 11):  # Generar 10 recursos
                resource = f'Recurso {i}'
                buffer.append(resource)
                logging.debug('El productor ha generado el recurso: %s', resource)
            logging.debug('Notificando a los consumidores que los recursos están disponibles.')
            cond.notify_all()
            cond.wait()  # Esperar a que los consumidores utilicen los recursos

condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='p', target=producer, args=(condition,))

c1.start()  # Iniciamos el hilo consumidor 1
time.sleep(2)
c2.start()  # Iniciamos el hilo consumidor 2
time.sleep(2)
p.start()  # Iniciamos el hilo productor