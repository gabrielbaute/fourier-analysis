# Guía base de análisis de fourier

Mediante este repositorio, tendrán acceso a algunas funciones básicas de análisis de fourier, servirán como guía para elaborar sus propias funciones y clases.

## Instrucciones

1. Clona aste repositorio:
```bash
git clone https://github.com/gabrielbaute/fourier-analysis.git
```

2. Crea un entorno virtual:
```bash
cd fourier-analysis
python -m venv ven
venv\Scripts\activate
```

3. Instala las dependencias:
```bash
pip install -r requirements.txt
```

4. Abre el proyecto:
```bash
code .
```

## ¿Cómo emplear el proyecto?
Este repositorio asume que estás leyendo datos desde un raspberry pi. En caso de no tener uno a la mano, podrías simular las entradas muestreadas, colocando a la entrada de los módulos listas de floats (64, 128, 256 muestras, etc)