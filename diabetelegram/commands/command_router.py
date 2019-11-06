from diabetelegram.commands.injection_commands import NewInjectionCommand
from diabetelegram.commands.meal_commands import DeleteMealCommand, EditMealCommand, NewMealCommand, SearchMealCommand
from diabetelegram.commands.ping_command import PingCommand
from diabetelegram.commands.start_command import StartCommand

class CommandRouter:
    """Passes a message containing a command to the corresponding handler class"""
    COMMANDS = {
        '/start': StartCommand,
        '/ping': PingCommand,
        '/newmeal': NewMealCommand,
        '/editmeal': EditMealCommand,
        '/deletemeal': DeleteMealCommand,
        '/searchmeal': SearchMealCommand,
        '/newinjection': NewInjectionCommand,
    }

    @classmethod
    def dispatch(cls, message):
        command = message['text'].split(maxsplit=1)[0]
        matching_command = cls.COMMANDS.get(command, None)

        if not matching_command:
            return False

        matching_command.handle(message)
        return True
