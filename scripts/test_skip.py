import pytest

class Test_Login:
    # 已经没有问题了，不想跑这个了，已经没有问题了
    @pytest.mark.skipif(True,reason="Done")
    def test_login(self):
        print("111")
        assert True

    def test_login2(self):
        print("2222")
        assert True
