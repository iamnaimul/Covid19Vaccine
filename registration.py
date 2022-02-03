from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep


def indx_num(yob):
    return ((2004-yob)+1)

def to_click(xpath):
    return browser.find_element_by_xpath(xpath).click()
    
def to_write(xpath, txt):
    return browser.find_element_by_xpath(xpath).send_keys(txt)

def to_select(xpath, indx=1):
    return Select(browser.find_element_by_xpath(xpath)).select_by_index(indx)

# USER INPUT
nid = int(input('[+] Enter NID Number: '))
dob = int(input('[+] Enter Date of Birth: '))
mob = int(input('[+] Enter Month of Birth: '))
yob = int(input('[+] Enter Year of Birth: '))

path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.maximize_window()
url = 'https://surokkha.gov.bd/enroll'
browser.get(url)
browser.implicitly_wait(2)
    
to_click('//*[@id="root"]/div[2]/div/div/div[1]/ul/li[1]/a')
browser.implicitly_wait(2)
to_select('//*[@id="basic_type"]', 1)
browser.implicitly_wait(2)
to_write('//*[@id="nid"]', nid)
browser.implicitly_wait(2)
to_select('//*[@id="basic_dob_day"]', dob)
to_select('//*[@id="basic_dob_month"]', mob)
to_select('//*[@id="basic_dob_year"]', indx_num(yob))

print('End - Close the window manually')
