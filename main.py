from User import User
from IA import chatIA
from News import News
import json

user = User(1)
news_object = News()
news = news_object.news
step = 4

for i in range(0, len(news), step):
    new_id = news.loc[i].name
    rate = news.iloc[i].rate
    if rate is None:
        prompt = news_object.getPrompt(new_id, step)
        response = chatIA(user, prompt)
        print(response)
        result = eval(response)
        print(response)
        #news_object.setResult(new_id, result)
        #news_object.update(new_id)

