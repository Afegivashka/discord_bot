import requests, config
from bs4 import BeautifulSoup


def weather_city(city):
    link = f"https://www.google.com/search?q=погода+в+{city}"

    headers = {"User-Agent": config.token_pogoda}

    responce = requests.get(link, headers=headers)

    print(responce)

    soup = BeautifulSoup(responce.text, "html.parser")

    citys = soup.select("span.BBwThe")[0].getText()
    temperature = soup.select("#wob_tm")[0].getText()
    title = soup.select("#wob_dc")[0].getText()
    humidity = soup.select("#wob_hm")[0].getText()
    time = soup.select("#wob_dts")[0].getText()
    wind = soup.select("#wob_ws")[0].getText()

    return f"""{citys}
{title}
Температура: {temperature}°С
Влажность: {humidity}
Ветер: {wind}
{time}"""
