import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("lang=ko_KR")
chromedriver_path = "D:\ITStudy\CatchV\crawler\chromedriver.exe"
##############################################################  ############
##################### variable related selenium ##########################
##########################################################################
driver = webdriver.Chrome(executable_path=chromedriver_path)


def main(page, level, languages):
    path = "./programmers/"
    url = "https://school.programmers.co.kr/learn/challenges?page={0}&levels={1}&languages={2}&order=acceptance_desc".format(
        page, level, languages
    )
    driver.get(url)
    for i in range(1, 5):
        try:
            wait = WebDriverWait(driver, 5)
            element = wait.until(
                EC.element_to_be_clickable((By.ID, "edu-service-app-main"))
            )

            ttls = driver.find_elements(By.XPATH, '//td[@class="title"]')

            for ttl in ttls:
                ttl = ttl.text.replace("\n", "_")
                ttl = ttl.replace(" ", "_")
                ttl = ttl.translate(str.maketrans("", "", '\/:*?"<>|'))
                newpath = path + ttl
                print(newpath)
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                    open(newpath + "/problem_description.txt", "w")
                    open(newpath + "/solution.py", "w")
            nxtbtn = driver.find_elements(By.XPATH, '//button[@aria-label="다음 페이지"]')

            nxtbtn[0].click()
        except:
            pass


if __name__ == "__main__":
    main()
