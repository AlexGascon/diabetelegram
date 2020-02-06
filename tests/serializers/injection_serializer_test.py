from diabetelegram.models.injection import Injection
from diabetelegram.serializers.injection_serializer import InjectionSerializer


def test_to_dict():
    units = 18
    injection_type = 'Basal'
    notes = 'Notes about the injection'

    injection = Injection(units=units, notes=notes, injection_type=injection_type)
    serialized = InjectionSerializer(injection).to_dict()

    assert serialized['units'] == units
    assert serialized['type'] == injection_type
    assert serialized['notes'] == notes

def test_to_dict_with_incomplete_injection():
    units = 18
    injection_type = 'Basal'

    injection = Injection(units=units, injection_type=injection_type)
    serialized = InjectionSerializer(injection).to_dict()

    assert serialized['units'] == units
    assert serialized['type'] == injection_type
    assert 'notes' not in serialized
