
from os import name
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from time import sleep
import re
from bs4 import BeautifulSoup, BeautifulStoneSoup
import pandas as pd

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
    sleep(3)

    html_content = driver.find_element_by_xpath("//*[@id='dataTables-example0']").get_attribute("outerHTML")

    links_embeds = driver.find_elements_by_css_selector("td > a")

    print("links "+links_embeds)
   

    driver.quit()


html = open("Buscar Filmes_Séries - TopFlix.html", "r").read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find(name='table'), 'html.parser'

dt_full = pd.read_html(str(table))[0]

# print(dt_full)
 
# print(dt_full)

    
searchEmbed("Bob Esponja", '')


