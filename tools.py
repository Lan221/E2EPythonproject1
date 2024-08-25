class Login:
    def login_in(self,username,password):
        self.username = username
        self.password =password
        if self.username == 'admin' and self.password == '123456':
            return ('login successful')
        else:
            return ('login failed because of wrong user name or password')


class Animal:
    pass