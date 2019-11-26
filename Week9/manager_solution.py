class Account:
    def __init__(self, id, nickname, password):
        self.id = id
        self.nickname = nickname
        self.password = password


    def __str__(self):
        return self.nickname + ' (' + self.id + ')'


class Database:
    def __init__(self):
        self.db = set()


    def __str__(self):
        accounts = []
        for account in self.db:
            accounts.append(str(account))
        return '\n'.join(accounts)


    def exists(self, id):
        for account in self.db:
            if account.id == id:
                return True
        return False


    def get_account(self, id):
        for account in self.db:
            if account.id == id:
                return account
        return None


    def register(self, new_account):
        if self.exists(new_account.id):
            return False

        self.db.add(new_account)
        return True


    def unregister(self, id, password):
        if not self.exists(id):
            return False

        account = self.get_account(id)
        if account.password != password:
            return False

        self.db.remove(account)
        return True


database = Database()

print(database.register(Account('abc', 'abc', 'hello1234')))
print(database.register(Account('abc', 'def', 'a1b2c3')))
print(database.register(Account('kjh618', 'kjh', 'pwd4321')))
print(database)

print(database.unregister('abc', 'a1b2c3'))
print(database.unregister('abc', 'hello1234'))
print(database)
