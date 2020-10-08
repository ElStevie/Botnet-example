from pexpect import pxssh


class Bot:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.session = self.ssh()

    def __repr__(self):
        has_password = 'with password' if self.password else 'without password'
        return f"Session: {self.user}@{self.host} {has_password}"

    def __str__(self):
        return f"{self.user}@{self.host}"

    def ssh(self):
        try:
            bot = pxssh.pxssh()
            bot.login(self.host, self.user, self.password)
            return bot
        except Exception as e:
            print("Connection failure.")
            print(e)

    def send_command(self, cmd):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before
