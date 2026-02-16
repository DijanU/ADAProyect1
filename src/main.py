"""
Punto de entrada del simulador de Maquina de Turing.

Uso:
    uv run python -m src.main <archivo_maquina.yaml>
"""

import sys
from src.loader import load_machine


def main():
    if len(sys.argv) < 2:
        print("Uso: uv run python -m src.main <archivo_maquina.yaml>")
        print("Ejemplo: uv run python -m src.main machines/fibonacci.yaml")
        sys.exit(1)

    filepath = sys.argv[1]

    # Cargar la maquina desde el archivo
    machine = load_machine(filepath)

    print()
    print("Ingrese la cadena de entrada en representacion unaria.")
    print("Ejemplo: '111' para n=3")
    print("Escriba 'salir' para terminar.")
    print()

    while True:
        entrada = input("Cadena de entrada: ").strip()

        if entrada.lower() == "salir":
            print("Fin de la simulacion.")
            break

        # Validar que la entrada solo contenga simbolos del alfabeto de entrada
        for char in entrada:
            if char not in machine.input_alphabet:
                print(f"Error: simbolo '{char}' no pertenece al alfabeto de entrada {machine.input_alphabet}")
                continue

        print()
        result = machine.run(entrada)

        if result["accepted"]:
            output = result["tape"]
            # Contar los 1s en la salida para mostrar el valor numerico
            count = output.count("1")
            print(f"\nResultado numerico: F({len(entrada)}) = {count}")
        print()


if __name__ == "__main__":
    main()
