from datetime import datetime
from plyer import notification
import time

# Pedimos al usuario que ingrese su fecha de cumpleaños
while True:
    cumpleaños = input('Ingrese su fecha de cumpleaños en el formato: dd/mm/yyyy: ')
    if not cumpleaños:
        continue    # Si el usuario colocó bien la fecha, se continua con el código
    try:
        fecha_cumpleaños = datetime.strptime(cumpleaños, '%d/%m/%Y')
        fecha_str = input("Ingresa la fecha y hora del recordatorio (formato: dd/mm/yyyy HH:MM): ")
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
        break
    except ValueError:
        print('La fecha ingresada no es válida.')
# Se resta la fecha que indicó el usuario con la fecha actual
segundos_hasta_recordatorio = (fecha - datetime.now()).total_seconds()

if segundos_hasta_recordatorio < 0:
    print('La fecha ya pasó')
else:
    # Configuración del recordatorio
    titulo = 'Recordatorio'
    mensaje = '¡Felíz cumpleaños! ❤️'
    tiempo = 10
    time.sleep(segundos_hasta_recordatorio) # El código entra en reposo hasta que se cumpla el horario del recordatorio
    notification.notify(title=titulo,message=mensaje,timeout=tiempo)
    