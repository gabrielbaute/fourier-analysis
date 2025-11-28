import serial
import serial.tools.list_ports

class PortsAnalyzer:
    def __init__(self):
        pass

    def list_ports(self) -> list[str]:
        """Devuelve una lista de puertos disponibles en el sistema"""
        puertos = serial.tools.list_ports.comports()
        return [p.device for p in puertos]
    
    def port_info(self, port: str) -> dict | None:
        """
        Devuelve información sobre el puerto especificado.

        Args:
            port (str): El nombre del puerto a analizar.

        Returns:
            dict: Un diccionario con la información del puerto. Si el puerto no existe, devuelve None.
        """
        puertos = serial.tools.list_ports.comports()
        for p in puertos:
            if p.device == port:
                return {
                    "device": p.device,
                    "name": p.name,
                    "description": p.description,
                    "hwid": p.hwid,
                    "vid": p.vid,
                    "pid": p.pid,
                    "serial_number": p.serial_number,
                    "location": p.location,
                    "manufacturer": p.manufacturer,
                    "product": p.product,
                    "interface": p.interface
                }
        return None