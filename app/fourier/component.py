import cmath

class FourierComponent:
    def __init__(self, k: int, frequency: float, value: complex):
        self.k = k                # índice discreto
        self.frequency = frequency # frecuencia asociada (Hz)
        self.value = value         # coeficiente complejo

    @property
    def magnitude(self) -> float:
        return abs(self.value)

    @property
    def phase(self) -> float:
        return cmath.phase(self.value)

    def __repr__(self):
        return (f"FourierComponent(k={self.k}, f={self.frequency:.2f} Hz, "
                f"mag={self.magnitude:.3f}, phase={self.phase:.3f})")

    def __to_dict__(self):
        return {
            "index[k]": self.k,
            "frecuency": self.frequency,
            "value": self.value,
            "magnitude": self.magnitude,
            "phase": self.phase
        }