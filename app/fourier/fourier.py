import cmath
import logging
from typing import List
from app.fourier.component import FourierComponent
from app.schemas import FourierResponse

class Fourier:
    def __init__(self, x: list[float], fs: float = 1.0):
        """
        x: señal en el tiempo (lista de floats)
        fs: frecuencia de muestreo en Hz
        """
        self.x = x
        self.fs = fs
        self.N = len(x)
        self.logger = logging.getLogger(f"{self.__class__.__name__}")

    def get_magnitude(self, value: complex) -> float:
        """
        Retorna el módulo de un número complejo.

        Args:
            value (complex): número complejo
        
        Returns:
            float: módulo del número complejo
        """
        return abs(value)
    
    def get_phase(self, value: complex) -> float:
        """
        Retorna la fase de un número complejo.
        
        Args:
            value (complex): número complejo
        
        Returns:
            float: fase del número complejo en radianes
        """
        return cmath.phase(value)

    def get_transform_kernel(self, k: int, N: int) -> complex:
        """
        Kernel de la transformada: W_N^k = exp(-j*2πk/N)

        Args:
            k (int): índice discreto
            N (int): número total de muestras
        
        Returns:
            complex: valor del kernel de la transformada
        """
        return cmath.exp(-2j * cmath.pi * k / N)

    def dft(self) -> List[FourierComponent]:
        """
        Transformada discreta de Fourier (O(N^2))
        Devuelve una lista de FourierComponent.
        
        Returns:
            list[FourierComponent]: lista de componentes de Fourier
        """
        self.logger.info("Calculando DFT...")
        resultado = []
        for k in range(self.N):
            suma = 0j
            for n in range(self.N):
                suma += self.x[n] * self.get_transform_kernel(k * n, self.N)
            freq = self.fs * k / self.N
            resultado.append(FourierComponent(k, freq, suma))
        self.logger.info(f"DFT completa. Encontrados {len(resultado)} componentes.")
        return resultado

    def fft(self, x=None) -> List[complex]:
        """
        FFT recursiva (Cooley–Tukey). Devuelve coeficientes complejos.
        
        Args:
            x (list[complex], optional): señal de entrada. Si es None, usa self.x.
        
        Returns:
            list[complex]: lista de coeficientes complejos
        """
        self.logger.info("Calculando FFT...")
        if x is None:
            x = self.x
        N = len(x)
        if N <= 1:
            return x
        pares = self.fft(x[0::2])
        impares = self.fft(x[1::2])
        factor = [self.get_transform_kernel(k, N) * impares[k] for k in range(N//2)]
        self.logger.info("FFT completa.")
        return [pares[k] + factor[k] for k in range(N//2)] + \
               [pares[k] - factor[k] for k in range(N//2)]

    def fft_components(self) -> List[FourierResponse]:
        """
        Versión FFT que devuelve FourierResponse para análisis didáctico.
        
        Returns:
            list[FourierResponse]: lista de respuestas de Fouriers
        """
        coeficientes = self.fft(self.x)
        resultado = []
        for k, val in enumerate(coeficientes):
            freq = self.fs * k / self.N
            response = FourierResponse(
                k=k,
                frequency=freq,
                value=val,
                magnitude=self.get_magnitude(val),
                phase=self.get_phase(val)
            )
            resultado.append(response)
        self.logger.info(f"FFT completa. Encotrados {len(resultado)} componentes.")
        return resultado
 
    def fft_components_explain(self, x=None) -> List[FourierComponent]:
        """
        Deprecated: Versión FFT que devuelve FourierComponent para análisis didáctico.
        """
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


