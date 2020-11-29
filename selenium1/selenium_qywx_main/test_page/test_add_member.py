# Gong
from selenium1.selenium_qywx_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()
    def test_addmenber(self):
        self.main.goto_add_member().add_member()


