import pandas as pd
from Database import DataBase


class News:

    def __init__(self):
        self.database = DataBase()
        response = self.database.select('news')
        self.news = pd.DataFrame()
        self.df(response)
        print(f'Len(news): {len(self.news)}')

    def df(self, data):
        for new in data:
            new = {
                'hash': new[0],
                'title': new[3],
                'subtitle': new[4],
                'url': new[5],
                'date': new[6],
                'time': new[7],
                'text': new[10],
                'resume': new[11],
                'rate': new[12]
            }
            self.news = self.news._append(new, ignore_index=True)
        self.news = self.news[self.news['text'] != '']
        self.news['all'] = 'Title: ' + self.news['title']
        self.news['all'] += '\nSubtitle: ' + self.news['subtitle']
        self.news['all'] += '\nArticle: ' + self.news['text']
        self.news['date'] = pd.to_datetime(self.news['date'])
        self.news['time'] = pd.to_timedelta(self.news['time'])
        self.news['datetime'] = self.news['date'] + self.news['time']

    def getPrompt(self, index):
        prompt = open('prompt', mode='r', encoding='utf-8').read()
        prompt += f'\nTitle: {self.news.iloc[index]["title"]}'
        return prompt

    def setResult(self, index, result):
        self.news.loc[index, ['rate', 'asset']] = [result['rate'], result['asset']]

    def update(self, index):
        hash_new, rate, asset = self.news.loc[index, ['hash', 'rate', 'asset']]
        self.database.update('news', 'rate', rate, hash_new, 'h_news')
        self.database.update('news', 'asset', asset, hash_new, 'h_news')


