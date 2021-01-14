from package import *
from mcpi.minecraft import Minecraft


class MOOCXING():
    def __init__(self):
        pass

    '''初始化'''

    def initMedia(self):
        return MXMedia.MXMedia()

    def initSpeech(self, APP_ID, API_KEY, SECRET_KEY):
        return MXSpeech.MXSpeech(APP_ID, API_KEY, SECRET_KEY)

    def initNLP(self, APP_ID, API_KEY, SECRET_KEY):
        return MXNLP.MXNLP(APP_ID, API_KEY, SECRET_KEY)
