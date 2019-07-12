from diabetelegram.parsers.base_parser import BaseParser
from diabetelegram.models.injection import Injection


class InjectionParser(BaseParser):
    def to_injection(self):
        injection_fields = {
            "injection_type": self.parse_injection_type(),
            "units": self.parse_units(),
            "notes": self.parse_notes(),
        }
        
        return Injection(**injection_fields)

    def parse_units(self):
        units_value = self._extract_value("unidades")

        return float(units_value) if units_value else None

    def parse_injection_type(self):
        return self._extract_value("tipo")

    def parse_notes(self):
        return self._extract_value("notas")