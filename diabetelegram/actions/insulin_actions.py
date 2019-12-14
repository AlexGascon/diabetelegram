from diabetelegram.actions.base_action import BaseAction
from diabetelegram.models.injection import Injection
from diabetelegram.services.injection_sns_client import InjectionSNSClient
from diabetelegram.services.state_manager import StateManager
from diabetelegram.services.telegram import TelegramWrapper


class InsulinAction(BaseAction):
    def matches(self):
        return self.message_text == 'insulin'

    def handle(self):
        self.state_manager.set('insulin')

        response = "What type of insulin do you want to add?"

        self.telegram.reply(self.message, response)


class InsulinBasalAction(BaseAction):
    def matches(self):
        state = self.state_manager.get()
        return state == 'insulin' and self.message_text == 'basal'

    def handle(self):
        self.state_manager.set('basal')

        response = "How many units did you take?"

        self.telegram.reply(self.message, response)


class InsulinBolusAction(BaseAction):
    def matches(self):
        state = self.state_manager.get()
        return state == 'insulin' and self.message_text == 'bolus'

    def handle(self):
        self.state_manager.set('bolus')

        response = "How many units did you take?"

        self.telegram.reply(self.message, response)


class InsulinUnitsAction(BaseAction):
    def matches(self):
        state = self.state_manager.get()
        return (state == 'basal' or state == 'bolus') and self.message_text.isdigit()

    def handle(self):
        state = self.state_manager.get()
        units = int(self.message_text)
        injection = Injection(injection_type=state, units=units)

        result = InjectionSNSClient().insulin_injected(injection)

        self.state_manager.set('initial')

        self.telegram.reply(self.message, result)
