"""
Simulador de Maquina de Turing Determinista de una cinta.
"""


class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transitions,
                 start_state, accept_state, reject_state, blank_symbol="_"):
        self.states = set(states)
        self.input_alphabet = set(input_alphabet)
        self.tape_alphabet = set(tape_alphabet)
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.blank_symbol = blank_symbol

        # Construir tabla de transiciones: (estado, simbolo) -> (nuevo_estado, nuevo_simbolo, direccion)
        self.transition_table = {}
        for t in transitions:
            state, symbol, new_state, new_symbol, direction = t
            self.transition_table[(state, symbol)] = (new_state, new_symbol, direction)

    def run(self, input_string, max_steps=100000, verbose=True):
        """
        Ejecuta la maquina de Turing con la cadena de entrada dada.

        Args:
            input_string: Cadena de entrada para la cinta.
            max_steps: Numero maximo de pasos antes de abortar.
            verbose: Si True, imprime cada configuracion.

        Returns:
            dict con resultado, pasos ejecutados, y contenido final de la cinta.
        """
        # Inicializar la cinta
        tape = list(input_string) if input_string else [self.blank_symbol]
        head = 0
        state = self.start_state
        steps = 0

        if verbose:
            print("=" * 60)
            print("SIMULACION DE MAQUINA DE TURING")
            print("=" * 60)
            print(f"Entrada: '{input_string}'")
            print(f"Estado inicial: {self.start_state}")
            print("-" * 60)

        while state != self.accept_state and state != self.reject_state:
            if steps >= max_steps:
                if verbose:
                    print(f"\nAbortado: se alcanzo el limite de {max_steps} pasos.")
                return {
                    "accepted": False,
                    "steps": steps,
                    "tape": self._tape_content(tape),
                    "aborted": True,
                }

            if verbose:
                self._print_configuration(state, head, tape, steps)

            symbol = tape[head] if head < len(tape) else self.blank_symbol

            key = (state, symbol)
            if key not in self.transition_table:
                if verbose:
                    print(f"\nNo hay transicion definida para ({state}, '{symbol}')")
                    print(f"La maquina se detiene (rechazo implicito).")
                return {
                    "accepted": False,
                    "steps": steps,
                    "tape": self._tape_content(tape),
                    "aborted": False,
                }

            new_state, new_symbol, direction = self.transition_table[key]

            # Escribir simbolo en la cinta
            while head >= len(tape):
                tape.append(self.blank_symbol)
            tape[head] = new_symbol

            # Mover cabeza
            if direction == "R":
                head += 1
            elif direction == "L":
                head = max(0, head - 1)

            # Extender cinta si es necesario
            if head >= len(tape):
                tape.append(self.blank_symbol)

            state = new_state
            steps += 1

        if verbose:
            self._print_configuration(state, head, tape, steps)
            print("-" * 60)
            result = "ACEPTADA" if state == self.accept_state else "RECHAZADA"
            print(f"Resultado: {result}")
            print(f"Pasos totales: {steps}")
            print(f"Cinta final: {''.join(tape).strip(self.blank_symbol)}")
            print("=" * 60)

        return {
            "accepted": state == self.accept_state,
            "steps": steps,
            "tape": self._tape_content(tape),
            "aborted": False,
        }

    def _print_configuration(self, state, head, tape, step):
        """Imprime la configuracion actual de la maquina."""
        tape_str = ""
        for i, symbol in enumerate(tape):
            if i == head:
                tape_str += f"[{symbol}]"
            else:
                tape_str += f" {symbol} "

        print(f"Paso {step:>4}: Estado={state:<15} Cabeza={head:<4} Cinta: {tape_str}")

    def _tape_content(self, tape):
        """Retorna el contenido de la cinta sin blancos al final."""
        content = "".join(tape).rstrip(self.blank_symbol)
        return content
