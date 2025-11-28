import serial
import logging
import matplotlib.pyplot as plt

class Signal:
    def __init__(self, baudrate: int = 115200, port: str = "COM15"):
        self.port = port
        self.baudrate = baudrate
        self.logger = logging.getLogger(f"{self.__class__.__name__}")
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)

    def read_line(self) -> str:
        """Lee una línea cruda desde el puerto serial y la devuelve como string"""
        raw = self.ser.readline()
        return raw.decode("utf-8").strip()

    def read_values(self) -> list[float]:
        """Convierte la línea recibida en lista de floats"""
        linea = self.read_line()
        if linea.startswith("[") and linea.endswith("]"):
            # elimina corchetes y separa por coma
            valores = linea[1:-1].split(",")
            response = [float(v.strip()) for v in valores]
            self.logger.info(f"Valores obtenidos: {len(response)} muestras")
            return response
        return []

    def write_command(self, cmd: str):
        """Envía un comando al Pico"""
        self.ser.write((cmd + "\n").encode("utf-8"))

    def available(self) -> int:
        """Devuelve cuántos bytes hay en el buffer"""
        return self.ser.in_waiting

    def stream(self):
        """Modo streaming: lee continuamente y grafica en tiempo real"""
        plt.ion()
        fig, ax = plt.subplots()

        while True:
            valores = self.read_values()
            if valores:
                ax.clear()
                ax.plot(valores, marker="o")
                ax.set_ylim(0, 3.3)
                ax.set_title("Streaming ADC RP2040")
                ax.set_xlabel("Muestra")
                ax.set_ylabel("Voltaje (V)")
                plt.pause(0.01)

    def close(self) -> bool:
        try:
            self.ser.close()
            return True
        except Exception as e:
            print(f"Error al cerrar el puerto serial: {e}")
            return False