
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from time import sleep
import re

def searchEmbed(media_name):

    options = Options()
    options.binary_location = r"C:\Users\frank\AppData\Local\Mozilla Firefox\firefox.exe"
    options.headless = True
    driver = webdriver.Firefox(options=options)

    url = "https://api.topflix.pro/"
    email = "frankllin15@outlook.com"
    password = "frank98033809"
    # media_name = "Bob Esponja"
    regex = re.compile(r"tt[0-9a-z]{7}")

    try:

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
        sleep(3)

        title_name = driver.find_elements_by_xpath("//*[@id='dataTables-example0']/tbody/tr/td[1]/a")
        links_embeds = driver.find_elements_by_css_selector("td > a[title='LINK EMBED']")
        imdb_id = driver.find_elements_by_css_selector("td > a[title='LINK IMDB']")
        rl_date = driver.find_elements_by_xpath("//*[@id='dataTables-example0']/tbody/tr/td[2]")
   
        results = []

        for l in range(0, len(links_embeds)-1):
            results.append({
                "title_name": title_name[l].get_attribute("innerHTML"),
                "embed": links_embeds[l].get_attribute("href"),
                "imdb_id": regex.search(imdb_id[l].get_attribute("href")).group(),
                "rl_date": rl_date[l].get_attribute("innerHTML")[:10]
                
            })
   
    finally:
        driver.quit()

    return results    
