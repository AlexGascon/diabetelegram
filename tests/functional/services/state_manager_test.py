import pytest

from diabetelegram.services.state_manager import StateManager


def test_state_manager_gets_the_state_we_just_set(functional_state_manager):
    functional_state_manager.set('mock_state')
    assert functional_state_manager.get() == 'mock_state'

    functional_state_manager.set('another_mock_state')
    assert functional_state_manager.get() == 'another_mock_state'
