import os
import unittest
import time
import logging
from datetime import datetime
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from Base.base import Base
from Pages.login_page import LoginPage

# 테스트 케이스 클래스
class TestLogin(Base):
    def test_login(self):
        login = LoginPage(self.driver)
        login.enter_id('mamitest01')
        login.enter_password('Testmam01!')
        login.click_login_button()
        # 스크린샷을 저장합니다
        logging.info("save screenshot")
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        activity_name = Base.self.driver.current_activity
        screenshot_file_name = f"{activity_name}_{time_stamp}.png"
        screenshot_file_path = os.path.join("screenshots", screenshot_file_name)
        os.makedirs(os.path.dirname(screenshot_file_path), exist_ok=True)
        time.sleep(1)
        Base.self.driver.save_screenshot(screenshot_file_path + screenshot_file_name)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()
