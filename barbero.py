import threading

# Número máximo de sillas disponibles en la sala de espera
MAX_SILLAS = 5

# Semáforos para coordinar los procesos del barbero y los clientes
clientes_en_sala = threading.Semaphore(0)
cliente_atendido = threading.Semaphore(0)
sillas_disponibles = threading.Semaphore(MAX_SILLAS)

# Función que representa el proceso del barbero
def barbero():
    while True:
        # El barbero espera a que llegue un cliente a la sala de espera
        clientes_en_sala.acquire()
        
        # El barbero toma una silla de la sala de espera
        sillas_disponibles.release()
        
        # El barbero atiende al cliente
        print("El barbero está cortando el pelo a un cliente")
        cliente_atendido.release()

# Función que representa el proceso de los clientes
def cliente(id_cliente):
    while True:
        # El cliente espera a que haya una silla disponible en la sala de espera
        sillas_disponibles.acquire()
        
        # El cliente toma una silla de la sala de espera
        print(f"El cliente {id_cliente} se ha sentado en una silla de la sala de espera")
        clientes_en_sala.release()
        
        # El cliente espera a que el barbero lo atienda
        cliente_atendido.acquire()
        
        # El cliente es atendido por el barbero
        print(f"El cliente {id_cliente} ha sido atendido por el barbero")

# Creamos una instancia del proceso del barbero
threading.Thread(target=barbero).start()

# Creamos varias instancias del proceso de los clientes
for i in range(10):
    threading.Thread(target=cliente, args=(i+1,)).start()
