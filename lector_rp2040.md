# Código para RP2040

Este código se guardará en la memoria interna del RP2040, con el nombre de `main.py`, para asegurar que se ejecute apenas se encienda.

```python
from machine import ADC, Pin
import time

class Lector:
   def __init__(self, pin:int):
       # Inicializa el ADC en el pin indicado
       self.adc = ADC(Pin(pin))

   def tomar_lectura(self) -> float:
       # Lectura cruda (0–65535) convertida a voltaje (0–3.3 V)
       valor = self.adc.read_u16()
       voltaje = (valor / 65535) * 3.3
       return voltaje

   def muestrear(self, n:int, intervalo:float=0.1) -> list[float]:
       # Toma n muestras con un intervalo en segundos
       muestra = []
       for _ in range(n):
           l = self.tomar_lectura()
           muestra.append(l)
           time.sleep(intervalo)
       return muestra

    def muestrear_freq(self, n:int, frecuencia:float=50.0) -> list[float]:
        """
        Toma n muestras a una frecuencia dada (Hz).
        Ejemplo: frecuencia=50 → intervalo=0.02 s
        """
        intervalo = 1.0 / frecuencia
        muestra = []
        for _ in range(n):
            l = self.tomar_lectura()
            muestra.append(l)
            time.sleep(intervalo)
        return muestra



# -------------------------------
# Uso en un bucle infinito
# -------------------------------

lector = Lector(26)  # GP26 → ADC0

while True:
   # Bloque de muestreo (ejemplo: 5 muestras cada ciclo)
   datos = lector.muestrear(256, intervalo=0.02)
   print(datos)

   # Pausa entre ciclos
   time.sleep(2)

```