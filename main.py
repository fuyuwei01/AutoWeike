import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from tqdm import *


SLEEP_TIME=1.25

browser = webdriver.Chrome()
def login(browser):

    browser.get(r'https://weiban.mycourse.cn/#/login')

    flag = 1

    input("登陆完成后按enter")
def watch_course(browser):
    #//*[@id="app"]/div/div[1]/div[4]/div/section/div[1]/div[2]/div

    browser.find_element("xpath","//*[@id='app']/div/div[1]/div[4]/div/section/div[1]/div[2]").click()
    time.sleep(SLEEP_TIME*2)
    #必修课程
    print("刷必修课程ing")
    tmp=browser.find_element("xpath","//*[@id='app']/div/div[1]/div[4]/div/div/ul")
    course_list_num = len(tmp.find_elements("class name","folder-item"))
    count = 0
    for idx in tqdm(range(course_list_num)):
        text = browser.find_element("xpath", "//*[@id='app']/div/div[1]/div[4]/div/div/ul/li["+str(idx+1)+"]/div/div[1]/div").text
        sub_text = text.split("/")
        if int(sub_text[0])<int(sub_text[1]):

            for _ in range(int(sub_text[1])-int(sub_text[0])):
                #//*[@id="app"]/div/div[1]/div[4]/div/div/ul/li[1]/div/div[2]/a
                browser.find_element("xpath", "//*[@id='app']/div/div[1]/div[4]/div/div/ul/li[" + str(idx + 1) + "]/div/div[2]/a").click()
                time.sleep(SLEEP_TIME*1)
                browser.find_element("xpath", "//*[@id='app']/div/div[1]/ul/li[1]/div").click()
                time.sleep(SLEEP_TIME*1)
                inner_frame = browser.find_element(by=By.TAG_NAME, value="iframe")
                browser.switch_to.frame(inner_frame)
                inner_frame_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
                time.sleep(SLEEP_TIME+10)
                browser.execute_script("finishWxCourse()", inner_frame_body)
                time.sleep(SLEEP_TIME*1)
                browser.switch_to.alert.accept()
                time.sleep(SLEEP_TIME*1)
                browser.switch_to.default_content()
                browser.back()
                time.sleep(SLEEP_TIME*1)
                browser.back()
                time.sleep(SLEEP_TIME*2)

    #匹配课程
    print("刷匹配课程")
    count=0
    browser.find_element("xpath","//*[@id='app']/div/div[1]/div[2]/div/a[2]/div[2]").click()
    time.sleep(SLEEP_TIME*2)
    tmp=browser.find_element("xpath","//*[@id='app']/div/div[1]/div[5]/div/div/ul")
    course_list_num = len(tmp.find_elements("class name","folder-item"))

    for idx in tqdm(range(course_list_num)):
        text = browser.find_element("xpath", "//*[@id='app']/div/div[1]/div[5]/div/div/ul/li["+str(idx+1)+"]/div/div[1]/div").text
        sub_text = text.split("/")
        if int(sub_text[0])<int(sub_text[1]):
            for _ in range(int(sub_text[1])-int(sub_text[0])):
                browser.find_element("xpath", "//*[@id='app']/div/div[1]/div[5]/div/div/ul/li[" + str(idx + 1) + "]/div/div[2]/a").click()
                time.sleep(SLEEP_TIME*1)
                browser.find_element("xpath", "//*[@id='app']/div/div[1]/ul/li[1]/div").click()
                time.sleep(SLEEP_TIME*1)
                inner_frame = browser.find_element(by=By.TAG_NAME, value="iframe")
                browser.switch_to.frame(inner_frame)
                inner_frame_body = browser.find_element(by=By.CSS_SELECTOR, value="body")
                time.sleep(SLEEP_TIME+10)
                browser.execute_script("finishWxCourse()", inner_frame_body)
                time.sleep(SLEEP_TIME*1)
                browser.switch_to.alert.accept()
                time.sleep(SLEEP_TIME*1)
                browser.switch_to.default_content()
                browser.back()
                time.sleep(SLEEP_TIME*1)
                browser.back()
                time.sleep(SLEEP_TIME*2)
    browser.close()
    return False
def test(n):
    for i in range(4):
        print(n)
        time.sleep(SLEEP_TIME*1)

if __name__ == '__main__':
    login(browser)
    flag = True
    while(flag):
        try:
            flag = watch_course(browser)
        except :
            browser.get(r'https://weiban.mycourse.cn/index.html#/')
            time.sleep(SLEEP_TIME * 2)
            continue
