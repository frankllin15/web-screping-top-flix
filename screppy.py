
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from time import sleep
import re

def searchEmbed(media_name, release_date):

    options = Options()
    options.binary_location = r"C:\Users\frank\AppData\Local\Mozilla Firefox\firefox.exe"
    options.headless = True
    driver = webdriver.Firefox(options=options)

    url = "https://api.topflix.pro/"
    email = "frankllin15@outlook.com"
    password = "frank98033809"
    # media_name = "Bob Esponja"
    regex = re.compile(r"tt[0-9]{7}")




    driver.get(url)

    sleep(1)

    login_btn = driver.find_element_by_xpath("/html/body/nav/div/div/a[2]")
    login_btn.click()

    # sleep(2)

    driver.find_element_by_xpath("//*[@id='inputEmail']").send_keys(email)
    driver.find_element_by_xpath("//*[@id='inputPassword']").send_keys(password)

    driver.find_element_by_xpath("/html/body/div/div/form/button").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@id='search']").send_keys(media_name)
    driver.find_element_by_xpath("//*[@id='search']").send_keys(u'\ue007')
    sleep(2)

    embed_url = driver.find_element_by_xpath("//*[@id='dataTables-example0']/tbody/tr[2]/td[4]/a[1]").get_attribute("href")
    rl_date_result = driver.find_element_by_xpath("//*[@id='dataTables-example0']/tbody/tr[1]/td[2]").get_attribute("innerText")[:10]
    title_name = driver.find_element_by_xpath("//*[@id='dataTables-example0']/tbody/tr[1]/td[1]/a").get_attribute("innerText")
    imdb_id = regex.search(driver.find_element_by_xpath("//*[@id='dataTables-example0']/tbody/tr[1]/td[4]/a[2]").get_attribute("href")).group()



    

    # embed_url = element.get_attribute("href")
    print(embed_url)

    driver.quit()

    return dict({"name": title_name, "url": embed_url, "rl_date": rl_date_result, "imdb_id": imdb_id})

# searchEmbed("Bob Esponja", '')


