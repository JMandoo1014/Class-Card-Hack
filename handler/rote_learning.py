import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
        time.sleep(2)
        for i in range(num_d):
            time.sleep(0.3)
            try:
                # driver.find_element(By.XPATH, '//*[@id="wrapper-learn"]/div[1]/div/div[3]/div[1]/a').click() # 의미 보기
                actions = ActionChains(driver)
                actions.send_keys(Keys.SPACE).perform()
                time.sleep(0.3)
                actions.key_down(Keys.SHIFT).send_keys(Keys.SPACE).key_up(Keys.SHIFT).perform()
                time.sleep(0.3)
                driver.find_element(By.XPATH, '//*[@id="wrapper-learn"]/div[1]/div/div[2]/div[6]/a').click()
                # driver.find_element(By.XPATH, '//*[@id="wrapper-learn"]/div[1]/div/div[3]/div[2]/a').click() # 이제 알아요
            except Exception as e:
                print(e)
                break
        time.sleep(0.5)