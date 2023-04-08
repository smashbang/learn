
from selenium import webdriver

driver = webdriver.Firefox()
url = "https://www.google.com"
driver.get(url)

driver.find_element_by_xpath(id, )