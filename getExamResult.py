from selenium import webdriver
import time
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import datetime

################ KULLANICI BİLGİSİ ################
tc = "your_id"
sifre = "your_password"
###################################################
key = "yks"

i = 0

gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
# print(gecko)
binary = FirefoxBinary(r'C:\Program Files\Mozilla Firefox\firefox.exe')
# print(binary)
driver = webdriver.Firefox(firefox_binary=binary, executable_path=gecko+'.exe')

browser = webdriver.Firefox()
browser.implicitly_wait(1)
browser.get("https://sonuc.osym.gov.tr/SonucSec.aspx")

while True:
    latestExam = browser.find_element_by_xpath('//*[@id="grdSonuclar"]/tbody/tr[2]/td[1]/a')
    exam_name = latestExam.text.lower()
    print("Son Açıklanan Sınav: " + exam_name)
    if key in exam_name:
        break
    else:
        i = i + 1
        print("Sonuçlar bekleniyor... {}\n".format(i))
        browser.refresh()
        time.sleep(2)


latestExam.click()
time.sleep(1.5)

elementTc = browser.find_element_by_xpath('//*[@id="tc"]')
elementTc.send_keys(tc)
elementSifre = browser.find_element_by_xpath('//*[@id="sifre"]')
elementSifre.send_keys(sifre)

time.sleep(0.5)

elementGonder = browser.find_element_by_xpath('//*[@id="btng"]')
elementGonder.click()

screenshotPath = os.path.join(os.getcwd(), f'YKS_Sonuç({i}).png')
browser.save_screenshot(screenshotPath)
print("Screenshot saved to --> " + screenshotPath + "  ({})".format(datetime.now()))

time.sleep(1.5)
browser.close()
