
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from time import sleep

options = Options()
options.binary_location = r"C:\Users\frank\AppData\Local\Mozilla Firefox\firefox.exe"
options.headless = False
driver = webdriver.Firefox(options=options)

url = "https://api.topflix.pro/"
email = "frankllin15@outlook.com"
password = "frank98033809"
mediaName = "Bob Esponja"


driver.get(url)

# sleep(5)

login_btn = driver.find_element_by_xpath("/html/body/nav/div/div/a[2]")
login_btn.click()

# sleep(5)

driver.find_element_by_xpath("//*[@id='inputEmail']").send_keys(email)
driver.find_element_by_xpath("//*[@id='inputPassword']").send_keys(password)

driver.find_element_by_xpath("/html/body/div/div/form/button").click()
sleep(2)

driver.find_element_by_xpath("//*[@id='search']").send_keys(mediaName)
driver.find_element_by_xpath("//*[@id='search']").send_keys(u'\ue007')
sleep(2)

element = driver.find_element_by_xpath("//*[@id='dataTables-example0']/tbody/tr[2]/td[4]/a[1]")

html = element.get_attribute("outerHTML")

embed_url = element.get_attribute("href")
print(embed_url)

# input_search.send_keys("dog")
# input_search.send_keys(u'\ue007')


sleep(5)


driver.quit()