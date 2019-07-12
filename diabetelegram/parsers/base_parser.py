from dataclasses import dataclass


@dataclass
class BaseParser:
    message: str

    PARTS_SEPARATOR = ","
    KEY_VALUE_SEPARATOR = ":"

    def _extract_value(self, field_key):
        field_info = list(filter(lambda m: m.strip().startswith(field_key), self._message_parts()))

        if not field_info:
            return None

        field_value = field_info[0].split(self.KEY_VALUE_SEPARATOR)[1].strip()

        return field_value

    def _message_parts(self):
        return self.message.split(self.PARTS_SEPARATOR)
