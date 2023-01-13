
class User:

    users = dict()

    def __init__(self, userid):
        self.userid = userid
        self.conversation = ''
        self.add()

    def add(self):
        if self.userid not in User.users.keys():
            User.users.update({self.userid: self})

    @staticmethod
    def get(userid):
        assert userid in User.users.keys()
        return User.users[userid]

    def addConversation(self, msg):
        self.conversation += msg

    def getConversation(self):
        return self.conversation

    def setConversation(self, conversation):
        self.conversation = conversation
