import importlib
import os

ATTACK_MODULES = [
    "crop",
    "resize",
    "noise",
    "compress"
]


def apply_attack(image_path: str, attack_type: str):
    """
    Runs a single attack OR all attacks.
    Returns:
      - str (single attack path)
      - dict (all attacks → {attack: path})
    """

    # 🔥 ALL MODE
    if attack_type == "all":
        results = {}
        for attack in ATTACK_MODULES:
            module = importlib.import_module(f"attacks.{attack}")
            results[attack] = module.run(image_path)
        return results

    # 🔹 SINGLE ATTACK
    module = importlib.import_module(f"attacks.{attack_type}")

    if not hasattr(module, "run"):
        raise ValueError(
            f"Attack module '{attack_type}' does not define run(image_path)"
        )

    return module.run(image_path)