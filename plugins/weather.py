import requests
from robot.sdk.AbstractPlugin import AbstractPlugin


class Plugin(AbstractPlugin):
    SLUG = "weather"

    def getWeatherInfo(self, city):
        url = "https://free-api.heweather.net/s6/weather?location=" + str(city) + "&key=3bffba48276c408b9107e275a51f111e" 
        res = requests.post(url)
        info = res.json()
        try:
            nowInfo = info["HeWeather6"][0]["now"]
            lifeStyle = info["HeWeather6"][0]["lifestyle"]
            location = info["HeWeather6"][0]["basic"]["location"]
            parentCity = info["HeWeather6"][0]["basic"]["parent_city"]

            tmp = nowInfo["tmp"]
            fl = nowInfo["fl"]
            cond = nowInfo["cond_txt"]
            windDir = nowInfo["wind_dir"]
            windSc = nowInfo["wind_sc"]
            hum = nowInfo["hum"]
            vis = nowInfo["vis"]
            comf = lifeStyle[0]["txt"]
            drsg = lifeStyle[1]["txt"]
            flu = lifeStyle[2]["txt"]
            airBrf = lifeStyle[7]["brf"]
            cw = lifeStyle[6]["txt"]

            # return("今天%s的天气状况：%s，温度：%s℃，体感温度：%s℃，空气质量：%s，风向：%s，风力：%s级，湿度：百分之%s，能见度：%s公里，%s%s%s" % (location, cond, tmp, fl, airBrf, windDir, windSc, hum, vis, flu, drsg, cw))
            return("今天%s的天气状况：%s，温度：%s℃，体感温度：%s℃，空气质量：%s" % (location, cond, tmp, fl, airBrf))
        except:
            return("没有查到该城市的天气")

    def handle(self, query):
        city = self.getCity(query)
        weatherInfo = self.getWeatherInfo(city)
        self.say(weatherInfo)
        
        return None

    def isValid(self, query):
        return "天气" in query

