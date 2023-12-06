import threading
import time

def subproceso(condicion):
    while not condicion.is_set():
        time.sleep(2)
        print("\nProceso en segundo plano...")  # en un proceso en segundo plano, 
                                                #lo ideal es que no muestre un mensaje

condicion = threading.Event()

while True:
    print("""
1) Iniciar proceso en segundo plano
2) Salir\n
          """)
    entrada = input("->")
    if entrada == "1":
        hilo = threading.Thread(target=subproceso, args=(condicion,))
        hilo.start()
    if entrada == "2":
        condicion.set()
        hilo.join()
        break