import inspect
from dataclasses import dataclass


@dataclass
class Injection:
    """Represents an insulin injection"""
    injection_type: str = None
    notes:          str = None
    units:          float = None

    def __str__(self):
        injection_text = f"""
        Injection
        ----------
        Type: {self.injection_type}
        Units: {self.units}
        Notes: {self.notes}
        """

        return inspect.cleandoc(injection_text)
