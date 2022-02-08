from seleniumbase import BaseCase
import pytest


class DBClass(BaseCase):
    @pytest.mark.expected_failure
    def test_open(self):
        self.open("https://www.douban.com/")

    def test_sign_in(self):
        self.open("https://www.douban.com/")
        self.switch_to_frame(0)
        self.click("li.account-tab-account")
        self.type("#username", 17605068986)
        self.type("#password", "Zhanting86DB")
        self.click("div.account-form-field-submit")
        # 还是会触发验证码
