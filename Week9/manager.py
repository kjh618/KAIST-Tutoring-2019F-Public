class Account:
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password

    def __str__(self):
        return self.id + ', ' + self.nickname


class Database:
    def __init__(self):
        self.db = []

    def __str__(self):
        strs = []
        for i in range(len(self.db)):
            strs.append(str(self.db[i]))
        return '\n'.join(strs)

    def get_account(self, id):
        for i in self.db:
            if id == i.id:
                return i
        return None


    def exist(self, id):
        for i in self.db:
            if id == i.id:
                return True
        return False


    def register(self, account):
        if self.exist(account.id):
            return
        self.db.append(account)


database = Database()

a1 = Account('abc', 'abc', 'hello1234')
database.register(a1)
print(database)

a2 = Account('abc', 'def', 'a1b2c3')
database.register(a2)
print(database)


a3 = Account('kjh618', 'kjh', 'pwd4321')
database.register(a3)
print(database)

print(database.get_account('abc'))

#
# print(database.unregister('abc', 'a1b2c3'))
# print(database.unregister('abc', 'hello1234'))
#
# print(database)
