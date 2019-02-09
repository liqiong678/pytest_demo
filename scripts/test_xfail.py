import pytest

class Test_Login:
    # 四种情况
    """
    预期 成功 ，结果成功
    预期 成功，结果失败
    预期 失败 ， 结果 失败
    预期 失败 ，结果 成功
    """
  # True ,预期是失败,结果成功
    @pytest.mark.xfail(True,reason="Done")
    def test_login(self):
        print("111")
        assert True

    @pytest.mark.xfail(False, reason="Done")
    def test_login2(self):
        print("2222")
        assert True
