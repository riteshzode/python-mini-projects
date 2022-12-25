import requests

NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

with open("file.txt", mode="r") as file:
    NEWS_API = file.readline()

COMPANY_NAME = "Meta Platforms Inc"


news_para = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API
}

r2 = requests.get(NEWS_ENDPOINT, params=news_para)

article = [
    f"Headline : {i['title']}. \nBrief: {i['description']}\nURl : {i['url']}\n"
    for i in r2.json()["articles"]]

print(f"No of news available {len(article)}")

print(f"Top 3 News")

print(article[:3])


