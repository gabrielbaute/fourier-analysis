from app.signal_procesor import Signal

signal = Signal(port="COM15")

while True:
    valores = signal.read_values()
    if valores:
        print(valores)  # lista de floats lista para graficar