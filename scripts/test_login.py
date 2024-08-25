import pytest

from Common.read_data import build_data
from tools import Login

class Test_login():
    @pytest.mark.parametrize('username,password,expect',build_data())
    def test_login(self,username,password,expect):
        login_instant = Login()
        result = login_instant.login_in(username,password)
        print(f"username:{username},password:{password},expect:{expect}")
        assert expect == result



