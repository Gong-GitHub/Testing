# Gong
import  pytest
from appnium1.weixin.page.app import App
from appnium1.weixin.page.base_page import BasePage


class TestContact():
    def setup(self):
        self.app = App()
        self.app.start()
        self.main = self.app.main()

    def test_weixing(self):
        invitpge=self.app.main().goto_addresslist().\
            addmember().addmenber_by().input_name().\
            input_genser().input_phone().click_save()
        assert '成功' in invitpge.get_toast()
if __name__ == '__main__':
    pytest.main()
