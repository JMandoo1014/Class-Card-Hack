import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class RoteLearning:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver  # webdriver

    def run(self, num_d: int) -> None:  # 핸들러 실행
        driver = self.driver
        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div/div[2]/div[1]/div[1]",
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[2]/div/div/div/div[4]/a",
        ).click()
        for _ in range(1, num_d):
            time.sleep(3)
            try:
                self.button_auto_pass(
                    driver,
                    '//*[@id="wrapper-learn"]/div[1]/div/div[3]/div[1]/a',  # 의미 보기
                    1,
                    '//*[@id="wrapper-learn"]/div[1]/div/div[3]/div[2]/a',  # 이제 알아요
                )  # 카드 넘기기
            except Exception:
                break
        time.sleep(0.5)
        # driver.switch_to.default_content()
        # driver.find_element(
        #     By.XPATH,
        #     '//*[@id="wrapper-learn"]/div[1]/div/div[2]/div[4]/a',
        # ).click()

    def button_auto_pass(
        self, driver, btn1: str, time_sec: int, btn2: str
    ) -> None:  # 버튼 자동 클릭
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, btn1).click()  # 1번 버튼 클릭
        time.sleep(time_sec)
        driver.switch_to.default_content()
        driver.find_element(By.XPATH, btn2).click()  # 2번 버튼 클릭
