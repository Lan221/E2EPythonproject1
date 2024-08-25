class Login():

    def setup(self):
        print('1.open the webpage')
    def teardown(self):
        print('6,close the page')
    def test_login_1(self):
        print('3,login successful')
    def test_login_2(self):
        print('4,login successful')
    def test_login_3(self):
        print('5,login successful')

login_instance1 = Login()
login_instance1.setup()
login_instance1.teardown()
login_instance1.test_login_1()
login_instance1.test_login_2()
login_instance1.test_login_3()