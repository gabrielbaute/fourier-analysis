import serial

class Signal:
    def __init__(self, baudrate: int = 115200, port: str = "COM3"):
        self.port = port
        self.baudrate = baudrate
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
            return [float(v.strip()) for v in valores]
        return []

    def write_command(self, cmd: str):
        """Envía un comando al Pico"""
        self.ser.write((cmd + "\n").encode("utf-8"))

    def available(self) -> int:
        """Devuelve cuántos bytes hay en el buffer"""
        return self.ser.in_waiting

    def close(self) -> bool:
        try:
            self.ser.close()
            return True
        except Exception as e:
            print(f"Error al cerrar el puerto serial: {e}")
            return False