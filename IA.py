import openai
from Config import SECRET_KEY
<<<<<<< HEAD
import requests
from User import User
=======
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405

openai.api_key = SECRET_KEY


def chatIA(user, question):
<<<<<<< HEAD
    user.addConversation(question, User.Role.user)
    answer, role = getAnswer(user)
    user.addConversation(answer, User.Role.system)
=======
    user.addConversation('\nHumano: ' + question + '\nAI: ')
    answer = getAnswer(user)
    user.addConversation(answer)
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
    return answer


def getResponse(user):
<<<<<<< HEAD
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=user.getConversation(),
        max_tokens=100
=======
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user.getConversation(),
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        presence_penalty=0.6,
        stop=['\n', 'Humano: ', 'AI: ']
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
    )
    return response


def getAnswer(user):
<<<<<<< HEAD
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
=======
    answer = ''
    while answer == '':
        response = getResponse(user)
        answer = response.choices[0].text.strip()
    return answer
>>>>>>> bf5c2e3132810d7cacb0fb10391e46ff846c9405
