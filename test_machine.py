"""
Script de prueba automatica para la Maquina de Turing de Fibonacci.
Prueba casos base sin interaccion del usuario.
"""

from src.loader import load_machine


def test_fibonacci():
    """Prueba varios casos de Fibonacci."""
    
    print("=" * 70)
    print("PRUEBAS AUTOMATICAS - MAQUINA DE TURING FIBONACCI")
    print("=" * 70)
    print()
    
    # Cargar la maquina
    machine = load_machine("machines/fibonacci.yaml")
    print()
    
    # Casos de prueba: (n, entrada, F(n) esperado)
    test_cases = [
        (0, "", 0, "Caso base: F(0) = 0"),
        (1, "1", 1, "Caso base: F(1) = 1"),
        (2, "11", 1, "Caso base: F(2) = 1"),
        (3, "111", 2, "F(3) = 2"),
        (4, "1111", 3, "F(4) = 3"),
        (5, "11111", 5, "F(5) = 5"),
        (6, "111111", 8, "F(6) = 8"),
        (7, "1111111", 13, "F(7) = 13"),
        (8, "11111111", 21, "F(8) = 21"),
        (9, "111111111", 34, "F(9) = 34"),
        (10, "1111111111", 55, "F(10) = 55"),
    ]
    
    results = []
    
    for n, entrada, expected, description in test_cases:
        print(f"Test: {description}")
        print(f"  Entrada: '{entrada}' (n={n})")
        
        result = machine.run(entrada, verbose=False)
        
        output = result["tape"]
        # Limpiar separadores - contar solo hasta el primer '0'
        if '0' in output:
            output_clean = output.split('0')[0]
        else:
            output_clean = output
        fib_result = output_clean.count("1")
        pasos = result["steps"]
        aceptada = result["accepted"]
        
        status = "✓ PASS" if fib_result == expected and aceptada else "✗ FAIL"
        
        print(f"  Salida: '{output}' (conteo={fib_result})")
        print(f"  Esperado: F({n}) = {expected}")
        print(f"  Pasos: {pasos}")
        print(f"  Estado: {'Aceptada' if aceptada else 'Rechazada'}")
        print(f"  {status}")
        print()
        
        results.append({
            "n": n,
            "expected": expected,
            "result": fib_result,
            "steps": pasos,
            "passed": fib_result == expected and aceptada
        })
    
    # Resumen
    print("=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    
    print(f"\nPruebas pasadas: {passed}/{total}")
    
    if passed == total:
        print("✓ TODAS LAS PRUEBAS PASARON")
    else:
        print("✗ ALGUNAS PRUEBAS FALLARON")
        for r in results:
            if not r["passed"]:
                print(f"  - F({r['n']}): esperado {r['expected']}, obtenido {r['result']}")
    
    print("\n" + "=" * 70)
    
    # Tabla de complejidad
    print("\nTABLA DE COMPLEJIDAD")
    print("-" * 70)
    print(f"{'n':>5} | {'F(n)':>8} | {'Pasos':>10} | {'Estado':>10}")
    print("-" * 70)
    
    for r in results:
        estado = "✓ OK" if r["passed"] else "✗ ERROR"
        print(f"{r['n']:>5} | {r['expected']:>8} | {r['steps']:>10} | {estado:>10}")
    
    print("=" * 70)
    
    return passed == total


if __name__ == "__main__":
    success = test_fibonacci()
    exit(0 if success else 1)
