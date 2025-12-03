from app.fourier import Fourier, GraphFrecuency
from app.signal_procesor import Signal

signal = Signal(port="COM15")
datos = signal.read_values()
print(f"Datos leídos: {len(datos)} muestras")
signal.close()

fs = 100.0  # frecuencia de muestreo en Hz (ejemplo)

# Calculamos la FFT
fourier = Fourier(datos, fs)
componentes = fourier.fft_components()  # lista de FourierComponent

# Graficamos el espectro de magnitud
grapher = GraphFrecuency(componentes)
grapher.graph_magnitude_db_spectrum()

