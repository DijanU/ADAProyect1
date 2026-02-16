"""
Carga la definicion de una Maquina de Turing desde un archivo YAML.
"""

import yaml
from src.turing_machine import TuringMachine


def load_machine(filepath):
    """
    Carga una Maquina de Turing desde un archivo YAML.

    Args:
        filepath: Ruta al archivo YAML con la definicion de la MT.

    Returns:
        Instancia de TuringMachine configurada.
    """
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)

    required_fields = [
        "states", "input_alphabet", "tape_alphabet",
        "transitions", "start_state", "accept_state",
        "reject_state", "blank_symbol"
    ]
    for field in required_fields:
        if field not in config:
            raise ValueError(f"Campo requerido '{field}' no encontrado en {filepath}")

    machine = TuringMachine(
        states=config["states"],
        input_alphabet=config["input_alphabet"],
        tape_alphabet=config["tape_alphabet"],
        transitions=config["transitions"],
        start_state=config["start_state"],
        accept_state=config["accept_state"],
        reject_state=config["reject_state"],
        blank_symbol=config["blank_symbol"],
    )

    print(f"Maquina '{config.get('name', 'Sin nombre')}' cargada exitosamente.")
    print(f"  Estados: {len(config['states'])}")
    print(f"  Transiciones: {len(config['transitions'])}")

    return machine
