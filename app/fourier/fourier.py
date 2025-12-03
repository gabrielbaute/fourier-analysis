import cmath
from app.fourier.component import FourierComponent

class Fourier:
    def __init__(self, x: list[float], fs: float = 1.0):
        """
        x: señal en el tiempo (lista de floats)
        fs: frecuencia de muestreo en Hz
        """
        self.x = x
        self.N = len(x)
        self.fs = fs

    def get_transform_kernel(self, k: int, N: int) -> complex:
        """Kernel de la transformada: W_N^k = exp(-j*2πk/N)"""
        return cmath.exp(-2j * cmath.pi * k / N)

    def dft(self) -> list[FourierComponent]:
        """Transformada discreta de Fourier (O(N^2))"""
        resultado = []
        for k in range(self.N):
            suma = 0j
            for n in range(self.N):
                suma += self.x[n] * self.get_transform_kernel(k * n, self.N)
            freq = self.fs * k / self.N
            resultado.append(FourierComponent(k, freq, suma))
        return resultado

    def fft(self, x=None) -> list[complex]:
        """FFT recursiva (Cooley–Tukey). Devuelve coeficientes complejos."""
        if x is None:
            x = self.x
        N = len(x)
        if N <= 1:
            return x
        pares = self.fft(x[0::2])
        impares = self.fft(x[1::2])
        factor = [self.get_transform_kernel(k, N) * impares[k] for k in range(N//2)]
        return [pares[k] + factor[k] for k in range(N//2)] + \
               [pares[k] - factor[k] for k in range(N//2)]

    def fft_components(self) -> list[FourierComponent]:
        """Versión FFT que devuelve FourierComponent para análisis didáctico."""
        coeficientes = self.fft(self.x)
        resultado = []
        for k, val in enumerate(coeficientes):
            freq = self.fs * k / self.N
            resultado.append(FourierComponent(k, freq, val))
        return resultado
 
    def fft_components_explain(self, x=None) -> list[FourierComponent]:
        if x is None:
            x = self.x
        N = len(x)
        if N <= 1:
            return [FourierComponent(0, 0.0, x[0])]

        pares = self.fft_components_explain(x[0::2])
        impares = self.fft_components_explain(x[1::2])

        resultado = []
        for k in range(N//2):
            twiddle = self.get_transform_kernel(k, N) * impares[k].value

            # Parte superior
            val_sup = pares[k].value + twiddle
            freq_sup = self.fs * k / N
            resultado.append(FourierComponent(k, freq_sup, val_sup))

            # Parte inferior
            val_inf = pares[k].value - twiddle
            freq_inf = self.fs * (k + N//2) / N
            resultado.append(FourierComponent(k + N//2, freq_inf, val_inf))

        return resultado


