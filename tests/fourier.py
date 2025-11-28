from app.fourier.fourier import Fourier

# Señal de ejemplo
datos = [0.323, 0.961, 0.990, 1.010, 1.010, 0.874, 0.879, 0.883]
fs = 5  # Hz

f = Fourier(datos, fs)

# DFT
print("DFT:")
for comp in f.dft():
    print(comp)

# FFT
print("\nFFT:")
for comp in f.fft_components():
    print(comp)
