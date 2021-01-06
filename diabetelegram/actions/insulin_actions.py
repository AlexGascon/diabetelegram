from diabetelegram.actions.base_action import BaseAction
from diabetelegram.models.injection import Injection
from diabetelegram.services.injection_sns_client import InjectionSNSClient
from diabetelegram.services.summary_sns_client import SummarySNSClient
from diabetelegram.services.state_manager import StateManager
from diabetelegram.services.telegram import TelegramWrapper


class InsulinBasalAction(BaseAction):
    def matches(self):
        return self.message_text.lower() == 'basal'

    def handle(self):
        self.state_manager.set('basal')

        response = "How many units did you take?"

        self.telegram.reply(self.message, response)


class InsulinBolusAction(BaseAction):
    def matches(self):
        return self.message_text.lower() == 'bolus'

    def handle(self):
        self.state_manager.set('bolus')

        response = "How many units did you take?"

        self.telegram.reply(self.message, response)


class InsulinUnitsAction(BaseAction):
    def matches(self):
        state = self.state_manager.get()
        is_valid_state = (state == 'basal' or state == 'bolus')

        return is_valid_state and self._is_valid_integer()

    def handle(self):
        state = self.state_manager.get()
        units = int(self.message_text)
        injection = Injection(injection_type=state, units=units)

        result = InjectionSNSClient().insulin_injected(injection)

        self.state_manager.set('initial')

        self.telegram.reply(self.message, result)

    def _is_valid_integer(self):
        try:
            int(self.message_text)
        except ValueError:
            return False

        return True


class InsulinSummaryAction(BaseAction):
    def matches(self):
        return self.message_text.lower() == 'summary'

    def handle(self):
        SummarySNSClient().summary_requested()

        self.state_manager.set('initial')