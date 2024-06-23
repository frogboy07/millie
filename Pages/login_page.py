import os
import unittest
import time
from datetime import datetime
from appium.webdriver.common.appiumby import AppiumBy
from Base.base import Base

# 테스트 페이지 클래스
class LoginPage(Base):
    def __init__(self, driver):
        self.driver = driver

    def enter_id(self, id):
        login_id = self.driver.find_element(by=AppiumBy.ID, value='kr.co.millie.eink:id/textField_login_identifier')
        login_id.send_keys(id)
        time.sleep(2)

    def enter_password(self, password):
        login_password = self.driver.find_element(by=AppiumBy.ID, value='kr.co.millie.eink:id/textField_login_password')
        login_password.send_keys(password)
        time.sleep(2)

    def click_login_button(self):
        login_button = self.driver.find_element(by=AppiumBy.ID, value='kr.co.millie.eink:id/button_login')
        login_button.click()

        # 스크린샷을 저장합니다
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        activity_name = self.driver.current_activity
        screenshot_file_name = f"{activity_name}_{time_stamp}.png"
        screenshot_file_path = os.path.join("screenshots", screenshot_file_name)
        os.makedirs(os.path.dirname(screenshot_file_path), exist_ok=True)
        self.driver.save_screenshot(screenshot_file_path + screenshot_file_name)


if __name__ == '__main__':
    unittest.main()
