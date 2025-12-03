import cmath
from pydantic import BaseModel

class FourierResponse(BaseModel):
    """
    Respuesta de la Transformada Rápida de Fourier para un componente específico.

    Attributes:
        k (int): índice discreto
        frequency (float): frecuencia asociada (Hz)
        value (complex): coeficiente complejo
        magnitude (float): módulo del coeficiente
        phase (float): fase del coeficiente (radianes)
    """
    k: int
    frequency: float
    value: complex
    magnitude: float
    phase: float