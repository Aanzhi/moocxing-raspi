from moocxing import MOOCXING
from robot.Brain import Brain
import sys

mx = MOOCXING()

# 初始化播放器和录音
media = mx.initMedia()

# 初始化语音识别+语音合成
APP_ID = '16901888'
API_KEY = 'qUcr9z2IVvREkyjDtlfbhsuv'
SECRET_KEY = 'preDe7g0C4ubTQ9XOir1afybwhD3jnAn'
speech = mx.initSpeech(APP_ID, API_KEY, SECRET_KEY)

# 初始化NLP
APP_ID = '19745053'
API_KEY = 'UnBq5gNtiZnReCKts31GiPlS'
SECRET_KEY = 'Ip2YLBAkGgbCp4xSv7TXjXojihipjFku'
nlp = mx.initNLP(APP_ID, API_KEY, SECRET_KEY)

print("********初始化完成********\n")

# 技能插件
SKILL = {"media": media, "speech": speech, "nlp": nlp}
brain = Brain(SKILL)
print("********技能插件加载完成********\n")


if len(sys.argv) == 1:
    print("输入歌名")
    sys.exit(-1)

result = sys.argv[1]
print(result)
brain.query("听"+result)