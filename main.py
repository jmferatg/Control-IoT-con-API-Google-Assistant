from machine import Pin
import dht
import time
import network
import socket
import urequests
##cloud_api="URL THINGSPEAK" 

# Función para conectar a la red wifi
def do_connect():
    
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('RED WIFI', 'CONTRASEÑA')  ### AGREGAR SSID Y CONTRASEÑA WIFI
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
do_connect()   #Invocar a la función wifi

#Configurar los puertos de entrada y salida
p5 = Pin(4, Pin.OUT)   ## SE UTILIZA EL PIN4 DE LA NODEMCU

#Configurar la función socket para enviar y recibir datos
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket creado exitosamente") 
except socket.error as err:
    print ("error al momento de crear el socket" %(err))

direccion = ""
puerto = 8000
s.bind((direccion, puerto))        
s.listen(14)



while True:
    consulta = urequests.get("SERVIDOR THIGNSPEAK URL")   ### AGREGAR URL PRIVADO
    data = consulta.json()
    datoRecibido = data["feeds"][0]["field1"]
    print("Cuarto: ",datoRecibido)
    if datoRecibido == "off":
        p5.on()
        time.sleep(5) 

    elif datoRecibido == "on":
        p5.off()
        time.sleep(5) 



