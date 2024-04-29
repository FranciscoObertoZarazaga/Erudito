from User import User
from IA import chatIA
from News import News
import json
from time import sleep
import re


def prefilter(text):
    match = re.search(r'(\{.*\})', text, re.DOTALL)
    if match:
        text = match.group(1)
    return text


def postfilter(dictionary):
    dictionary['resume'] = dictionary['resume'].replace("'", "´")
    return dictionary


count = 0


while True:
    print('Running...')
    user = User(1)
    news_object = News()
    news = news_object.news

    for index, new in news.iterrows():
        rate = new['rate']
        if rate is None:
            user.reset()
            prompt = news_object.getPrompt(index)
            try:
                response = chatIA(user, prompt)
                response = prefilter(response)
                print(response)
                result = json.loads(response)
                news_object.setResult(index, result)
                news_object.update(index)
                count += 1
                print('Noticias clasificadas', count)
                sleep(1)
            except Exception as e:
                raise e
        if index == len(news) - 1:
            print('Finalizado')
            exit()





