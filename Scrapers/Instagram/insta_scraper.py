from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


url = 'http://twitter.com/humanhacker/'
driver = webdriver.Firefox(executable_path='/Users/kodybentley/Documents/Tools/who-they-bee-new/Scrapers/Instagram/geckodriver')
driver.get(url)
test = WebDriverWait(driver, 300).until(driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[1]/div/span[1]/span'))
print(test)
# uname = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/h2')
# bio = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]')
# post = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a')
# print(f' Username: {uname.text}, bio: {bio.text}, first_post: {post.text}')
# soup = BeautifulSoup(driver.page_source, features='lxml')
# mydivs = soup.find_all("div", {"class": "rhpdm"})
# print(mydivs)