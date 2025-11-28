from app.signal_procesor import PortsAnalyzer

analyzer = PortsAnalyzer()
available_ports = analyzer.list_ports()

if available_ports:
    print("Puertos disponibles:")
    for port in available_ports:
        print(f"- {port}")
        info = analyzer.port_info(port)
        if info:
            print(f"  Información del puerto: {info}")
        else:
            print("  No se encontró información para este puerto.")
else:
    print("No se encontraron puertos disponibles.")