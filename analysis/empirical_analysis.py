"""
Analisis empirico de la Maquina de Turing de Fibonacci.

Genera:
- Listado de entradas de prueba y tiempos de ejecucion
- Diagrama de dispersion (tiempo vs tamano de entrada)
- Regresion polinomial ajustada a los datos
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from src.loader import load_machine


def measure_execution(machine, n):
    """
    Mide el tiempo de ejecucion de la MT para una entrada de tamano n.

    Args:
        machine: Instancia de TuringMachine.
        n: Tamano de la entrada (numero en unario).

    Returns:
        Tupla (tiempo_segundos, pasos, resultado).
    """
    input_string = "1" * n

    start_time = time.perf_counter()
    result = machine.run(input_string, verbose=False)
    end_time = time.perf_counter()

    elapsed = end_time - start_time
    return elapsed, result["steps"], result


def run_analysis(machine_path, test_inputs=None):
    """
    Ejecuta el analisis empirico completo.

    Args:
        machine_path: Ruta al archivo YAML de la MT.
        test_inputs: Lista de valores n para probar. Si es None, usa valores por defecto.
    """
    machine = load_machine(machine_path)

    if test_inputs is None:
        test_inputs = list(range(0, 16))

    # --- Entregable 5a: Listado de entradas y tiempos ---
    print("\n" + "=" * 70)
    print("ANALISIS EMPIRICO - MAQUINA DE TURING FIBONACCI")
    print("=" * 70)
    print(f"{'n':>5} | {'Entrada':>15} | {'Pasos':>10} | {'Tiempo (s)':>12} | {'F(n)':>8}")
    print("-" * 70)

    sizes = []
    times = []
    steps_list = []

    for n in test_inputs:
        elapsed, steps, result = measure_execution(machine, n)
        fib_result = result["tape"].count("1") if result["accepted"] else "ERROR"

        input_repr = "1" * n if n <= 10 else f"1x{n}"
        print(f"{n:>5} | {input_repr:>15} | {steps:>10} | {elapsed:>12.6f} | {fib_result:>8}")

        sizes.append(n)
        times.append(elapsed)
        steps_list.append(steps)

    # --- Entregable 5b: Diagrama de dispersion ---
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Tiempo vs entrada
    axes[0].scatter(sizes, times, color="blue", zorder=5)
    axes[0].set_xlabel("Tamano de entrada (n)")
    axes[0].set_ylabel("Tiempo de ejecucion (segundos)")
    axes[0].set_title("Tiempo de ejecucion vs Tamano de entrada")
    axes[0].grid(True, alpha=0.3)

    # Pasos vs entrada
    axes[1].scatter(sizes, steps_list, color="red", zorder=5)
    axes[1].set_xlabel("Tamano de entrada (n)")
    axes[1].set_ylabel("Numero de pasos")
    axes[1].set_title("Pasos de la MT vs Tamano de entrada")
    axes[1].grid(True, alpha=0.3)

    # --- Entregable 5c: Regresion polinomial ---
    sizes_arr = np.array(sizes, dtype=float)
    times_arr = np.array(times, dtype=float)
    steps_arr = np.array(steps_list, dtype=float)

    # Probar grados 1 a 4 y elegir el mejor ajuste
    best_degree = 1
    best_r2 = -1

    for degree in range(1, 5):
        if len(sizes) > degree:
            coeffs = np.polyfit(sizes_arr, steps_arr, degree)
            poly = np.poly1d(coeffs)
            y_pred = poly(sizes_arr)

            ss_res = np.sum((steps_arr - y_pred) ** 2)
            ss_tot = np.sum((steps_arr - np.mean(steps_arr)) ** 2)
            r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0

            if r2 > best_r2:
                best_r2 = r2
                best_degree = degree

    # Ajustar con el mejor grado
    coeffs_best = np.polyfit(sizes_arr, steps_arr, best_degree)
    poly_best = np.poly1d(coeffs_best)

    x_smooth = np.linspace(min(sizes), max(sizes), 200)
    y_smooth = poly_best(x_smooth)

    axes[1].plot(x_smooth, y_smooth, color="darkred", linewidth=2,
                 label=f"Regresion grado {best_degree} (R²={best_r2:.4f})")
    axes[1].legend()

    # Regresion para tiempos tambien
    coeffs_time = np.polyfit(sizes_arr, times_arr, best_degree)
    poly_time = np.poly1d(coeffs_time)
    y_time_smooth = poly_time(x_smooth)

    axes[0].plot(x_smooth, y_time_smooth, color="darkblue", linewidth=2,
                 label=f"Regresion grado {best_degree}")
    axes[0].legend()

    plt.tight_layout()
    plt.savefig("analysis/fibonacci_analysis.png", dpi=150)
    plt.show()

    print(f"\nMejor ajuste: polinomio de grado {best_degree}")
    print(f"R² = {best_r2:.6f}")
    print(f"Coeficientes: {coeffs_best}")
    print(f"\nGrafica guardada en: analysis/fibonacci_analysis.png")


if __name__ == "__main__":
    run_analysis("machines/fibonacci.yaml")
