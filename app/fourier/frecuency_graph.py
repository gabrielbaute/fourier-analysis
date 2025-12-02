import math
import numpy as np
import matplotlib.pyplot as plt
from app.fourier.component import FourierComponent

class GraphFrecuency:
    def __init__(self, componentes: list[FourierComponent]):
        self.frequencies = [c.frequency for c in componentes]
        self.values = [c.value for c in componentes]
        self.magnitudes = [c.magnitude for c in componentes]
        self.phases = [c.phase for c in componentes]
        self.N = len(self.frequencies)

    def print_magnitude_spectrum(self):
        """Imprime el espectro de magnitud"""
        print("Frecuencia (Hz) | Magnitud")
        print("----------------|---------")
        for f, m in zip(self.frequencies, self.magnitudes):
            print(f"{f:15.2f} | {m:.4f}")
    
    def print_phase_spectrum(self):
        """Imprime el espectro de fase"""
        print("Frecuencia (Hz) | Fase (radianes)")
        print("----------------|-----------------")
        for f, p in zip(self.frequencies, self.phases):
            print(f"{f:15.2f} | {p:.4f}")
    
    def print_complex_spectrum(self):
        """Imprime el espectro complejo"""
        print("Frecuencia (Hz) | Coeficiente complejo")
        print("----------------|-----------------")
        for f, c in zip(self.frequencies, self.values):
            print(f"{f:15.2f} | {c:.4f}")

    def graph_magnitude_spectrum(self):
        """Grafica el espectro de magnitud"""
        plt.figure(figsize=(10,5))
        plt.plot(self.frequencies, self.magnitudes, marker="o")
        plt.title("Espectro de la señal (FFT)")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud")
        plt.grid(True)
        plt.show()

    def graph_phase_spectrum(self):
        """Grafica el espectro de fase"""
        frequencies = self.frequencies[:self.N//2]
        phases = np.unwrap(self.phases[:self.N//2])  # suaviza saltos

        plt.figure(figsize=(10,5))
        plt.plot(frequencies, phases, marker="o", color="orange")
        plt.title("Espectro de fase (unwrapped)")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Fase (rad)")
        plt.grid(True)
        plt.show()

    def graph_complex_spectrum(self):
        """Grafica el espectro complejo (parte real e imaginaria)"""
        real_parts = [c.real for c in self.values[:self.N//2]]
        imag_parts = [c.imag for c in self.values[:self.N//2]]

        plt.figure(figsize=(6,6))
        plt.scatter(real_parts, imag_parts, marker="o")
        plt.title("Coeficientes FFT en plano complejo")
        plt.xlabel("Parte real")
        plt.ylabel("Parte imaginaria")
        plt.grid(True)
        plt.axis("equal")
        plt.show()
    
    def graph_magnitude_db_spectrum(self):
        """Grafica el espectro de magnitud en dB"""
        magnitudes_db = [20*math.log10(m) if m > 0 else -float("inf") for m in self.magnitudes]

        plt.figure(figsize=(10,5))
        plt.plot(self.frequencies, magnitudes_db, marker="o")
        plt.title("Espectro unilateral en dB")
        plt.xlabel("Frecuencia (Hz)")
        plt.ylabel("Magnitud (dB)")
        plt.grid(True)
        plt.show()