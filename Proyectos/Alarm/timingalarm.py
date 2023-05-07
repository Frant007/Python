import time, winsound
from playsound import playsound
from plyer import notification
# Pedimos al usuario que ingrese una hora en la que suene la alarma
hora = int(input('Ingrese la hora en formato 24h (0-23): '))
minutos = int(input("Ingresa los minutos (0-59): "))

# En este while, el codigo se va a ejecutar hasta que ññegue el momento en que suene
while True:
    hora_actual = time.localtime().tm_hour
    minuto_actual = time.localtime().tm_min
    
    if hora_actual == hora and minuto_actual == minutos:
        notification.notify(title='Hey!', message='Take a break!', timeout=10)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        winsound.PlaySound(None, winsound.SND_ASYNC)
        break
    else:
        time.sleep(10)   
