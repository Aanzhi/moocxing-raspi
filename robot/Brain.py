from robot import LoadPlugin


class Brain(object):
    def __init__(self, SKILL):
        self.plugins = LoadPlugin.loadPlugin(SKILL)
        self.result = ""

    def query(self, text):
        for plugin in self.plugins:
            if not plugin.isValid(text):
                continue
            self.result = plugin.handle(text)
            return True
        return False

