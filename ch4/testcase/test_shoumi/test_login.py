__author__ = 'wangxiao'

from hamcrest import assert_that, equal_to

from ch4.page.app import App


class TestSOUMiLogin:
    def setup_class(self):
        mainPage = App.start()
        self.profile_page = mainPage.into_profile_locator()
        self.login_page = self.profile_page.into_login_page()

    def test_login(self):
        self.login_page.username_login_shoumi('18860918480', '123456')
        toast = self.login_page.get_login_toast()
        assert_that(toast, equal_to('登录成功'))

    def test_logout(self):
        self.setting_page = self.profile_page.into_setting_page()
        self.setting_page.user_logout()
        toast = self.setting_page.user_logout_toast()
        assert_that(toast, equal_to('退出登录成功'))

    def teardown_class(self):
        App.quit()
