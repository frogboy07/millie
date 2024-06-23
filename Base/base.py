import os.path
import unittest
import logging
from datetime import datetime
from appium import webdriver
from appium.options.android import UiAutomator2Options

# 테스트 케이스 베이스 클래스
class Base(unittest.TestCase):

    # 테스트 메소드 호출 전 자동으로 호출되는 코드 - 모든 상태를 reset 해준다
    def setUp(self) -> None:
        # selenium 4.10.0 이후 desired_capabilities 대신 option을 사용하여 전달, andorid 단말 동작이므로 UiAutomatore2의 options을 사용
        options = UiAutomator2Options()

        # options에 Appium server에 전달할 설정변수들을 담음
        options.load_capabilities({
            "appium:platformName": "Android",  # 테스트할 플랫폼
            "appium:deviceName": "R3CW40H987L",  # 테스트할 기기명
            "appium:automationName": "uiautomator2",  # 테스트 시에 사용하는 Appium driver명
            "appium:appPackage": "kr.co.millie.eink",  # 테스트할 App package명
            "appium:appActivity": "kr.co.millie.eink.SplashActivity"  # package에서 최초 실행할 App Activity
        })

        # appium server 주소, 로컬환경의 4723 포트를 사용
        appium_server_url = 'http://127.0.0.1:4723'

        self.driver = webdriver.Remote(appium_server_url, options=options)

        # 로그 생성
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        # 콘솔창에 로그 남기기
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 로그 파일 출력
        current_data = datetime.now().strftime("%Y_%m_%d_%H%M%S")
        log_file_name = f"app_{current_data}.log"
        log_file_path = os.path.join("logs", log_file_name)
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)

        # 로그 메시지 포맷 설정
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # 핸들러를 로거에 추가
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    # 테스트 실행 후 종료 시 실행되는 코드
    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()