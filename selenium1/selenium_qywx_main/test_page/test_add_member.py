# Gong
from time import sleep

from selenium1.selenium_qywx_main.page.main import Main


class TestAddMember:
    def setup(self):
        self.main = Main()
    def test_addmenber(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        assert add_member.get_menber('9')


