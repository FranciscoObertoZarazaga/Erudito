from openai import OpenAI
from Config import SECRET_KEY
from User import User
import requests
import openai
import os

openai.api_key = SECRET_KEY
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY']
)


def chatIA(user, question):
    user.addConversation(question, User.Role.user)
    answer, role = getAnswer(user)
    user.addConversation(answer, User.Role.system)
    return answer


def getResponse(user):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=user.getConversation()
    )
    return response


def getAnswer(user):
    response = getResponse(user)
    response = response.choices[0].message
    answer = response.content
    role = response.role
    return answer, role


def getModels():
    header = {'Authorization': f'Bearer {openai.api_key}'}
    response = requests.get('https://api.openai.com/v1/models', headers=header)
    models = response.json()['data']
    for model in models:
        name = model['id']
        print(name)
