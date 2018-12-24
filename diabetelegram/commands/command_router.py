from diabetelegram.commands.new_meal_command import NewMealCommand
from diabetelegram.commands.ping_command import PingCommand

class CommandRouter:
    """Passes a message containing a command to the corresponding handler class"""
    COMMANDS = {
        '/ping': PingCommand,
        '/newmeal': NewMealCommand
    }

    @classmethod
    def dispatch(cls, message):
        command = message['text'].split(maxsplit=1)[0]
        matching_command = cls.COMMANDS.get(command, None)

        if not matching_command:
            return False

        matching_command.handle(message)
        return True
