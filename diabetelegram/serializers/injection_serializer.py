from dataclasses import dataclass

from diabetelegram.models.injection import Injection


@dataclass
class InjectionSerializer:
    injection: Injection

    def to_dict(self):
        data = {
            "units": self.injection.units,
            "type": self.injection.injection_type,
            "notes": self.injection.notes,
        }

        return {key: value for key, value in data.items() if value is not None}