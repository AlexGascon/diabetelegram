from diabetelegram.services.state_manager import StateManager


class StartCommand:
    @staticmethod
    def handle(message):
        StateManager(user_id=message['from']['id']).set('initial')
