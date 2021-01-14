from abc import ABCMeta, abstractmethod


class AbstractPlugin(metaclass=ABCMeta):

    def __init__(self, SKILL):
        self.media = SKILL["media"]
        self.speech = SKILL["speech"]
        self.nlp = SKILL["nlp"]

    def say(self, text):
        self.speech.TTS(text)
        self.media.play()

    def play(self, path):
        self.media.play(path)

    def getMusicName(self, text):
        return self.nlp.getMusicName(text)

    def getCity(self, text):
        return self.nlp.getCity(text)


    @abstractmethod
    def isValid(self, query):
        return False

    @abstractmethod
    def handle(self, query):
        return None 
