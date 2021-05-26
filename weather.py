import requests
import json
def WeatherToday():
    wt = requests.get("https://api.seniverse.com/v3/weather/now.json?key=Soko7dj7jHDLGmkIb&location=beijing&language=zh-Hans&unit=c")
    #print("网页内容:\n%s" % wt.content.decode("utf8"))#content返回原始数据为byte类型，这里utf8解码输出
    content = wt.content.decode("utf8")
    #print(content)
    result = json.loads(content)
    #print(type(result))
    #print(result)
    #temperature = result['results'][0]#['temperature']
    #print(result['results'])
    #print(result['results'][0])
    print("当前天气：")
    print("天气状况：",result['results'][0]['now']['text'])
    print("最高温度：",result['results'][0]['now']['temperature'])
    print("更新时间：",result['results'][0]['last_update'])
    #print(type(temperature))
def WeatherForecast(n):
    ParamsData = {"key":"Soko7dj7jHDLGmkIb",
                 "location":"beijing",
                 "language":"zh-Hans",
                 "unit":"c",
                 "days":3
                 }
    #wf = requests.get("https://api.seniverse.com/v3/weather/daily.json?key=Soko7dj7jHDLGmkIb&location=beijing&language=zh-Hans&unit=c&start=0&days=3")
    wf = requests.get("https://api.seniverse.com/v3/weather/daily.json",params = ParamsData)
    #print("网页内容:\n%s" % wf.content.decode("utf8"))#content返回原始数据为byte类型，这里utf8解码输出
    content = wf.content.decode("utf-8")
    AllResults = json.loads(content)
    #print(result)
    date = AllResults["results"][0]["daily"][n]["date"]
    text_day = AllResults["results"][0]["daily"][n]["text_day"]
    text_night = AllResults["results"][0]["daily"][n]["text_night"]
    high = AllResults["results"][0]["daily"][n]["high"]
    low = AllResults["results"][0]["daily"][n]["low"]
    rainfall = AllResults["results"][0]["daily"][n]["rainfall"]
    precip = AllResults["results"][0]["daily"][n]["precip"]
    wind_direction = AllResults["results"][0]["daily"][n]["wind_direction"]
    wind_direction_degree = AllResults["results"][0]["daily"][n]["wind_direction_degree"]
    wind_speed = AllResults["results"][0]["daily"][n]["wind_speed"]
    wind_scale = AllResults["results"][0]["daily"][n]["wind_scale"]
    humidity = AllResults["results"][0]["daily"][n]["humidity"]
    return [date,text_day,text_night,high,low,rainfall,precip,wind_direction,wind_direction_degree,wind_speed,wind_scale,humidity]

def LivingToday():
    ParamsData = {"key":"Soko7dj7jHDLGmkIb",
                  "location":"beijing",
                  "language":"zh-Hans",
                 }
    LivingResults = json.loads(requests.get("https://api.seniverse.com/v3/life/suggestion.json",params=ParamsData).content.decode("utf-8"))
    #print(LivingResults)
    print("洗车指数：",LivingResults["results"][0]["suggestion"]["car_washing"]["brief"])
    print("穿衣指数：", LivingResults["results"][0]["suggestion"]["dressing"]["brief"])
    print("感冒指数：", LivingResults["results"][0]["suggestion"]["flu"]["brief"])
    print("运动指数：", LivingResults["results"][0]["suggestion"]["sport"]["brief"])
    print("旅行指数：", LivingResults["results"][0]["suggestion"]["travel"]["brief"])
    print("紫外线强度：", LivingResults["results"][0]["suggestion"]["uv"]["brief"])
    print("更新时间：", LivingResults["results"][0]["last_update"])
if __name__ == "__main__":
    WeatherToday()
    date,text_day,text_night,high,low,rainfall,precip,wind_direction,wind_direction_degree,wind_speed,wind_scale,humidity = WeatherForecast(1)
    LivingToday()
    print("明日天气预报：")
    print("日期：%s\n白天天气：%s,最高温度：%s\n晚间天气：%s,最低温度：%s\n降水概率：%s,降水量：%s\n风向：%s,风向角度：%s,风速：%s,风力等级：%s\n相对湿度：%s"%(date,text_day,high,text_night,low,precip,rainfall,wind_direction,wind_direction_degree,wind_speed,wind_scale,humidity))