from diabetelegram.commands.ping_command import PingCommand

class CommandRouter:
    """Passes a message containing a command to the corresponding class"""
    COMMANDS = {
        '/ping': PingCommand
    }

    @classmethod
    def dispatch(cls, message):
        command = message['text'].split(maxsplit=1)[0]
        matching_command = cls.COMMANDS.get(command, None)

        if not matching_command:
            return False

        matching_command.handle(message)
        return True
        