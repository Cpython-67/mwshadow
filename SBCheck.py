"""I am not responsible for any misuse of this software
    Please get permission from the owner of the account and Blizzard and Activision respectfully before you use it
    Tool is incomplete
    results may vary but I have found it to be accurate
    if CODs slow website throws it off, simply run it again
    I may finish this tool to check multiple accounts from a txt on different threads
    If you are interested in seeing this tool finished feel free to contact me on Discord @C_#9495
    if package not found error, run pip install selenium -- crucial step if you are unfamiliar with python"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import time
opt = int(input("(1)Blizzard or (2)activision login(Enter number for option): "))
PATH = 'C:/Program Files/chromedriver.exe'
PROXIES = ['']
PROXY = PROXIES[0]
driver = webdriver.Chrome(PATH)

if opt == 1:
    blizzemailkey = str(input("Please enter blizz email: "))
    blizzpasskey = str(input("Password: "))
    driver.get('https://eu.battle.net/login/en-us/')
    blizzemail = driver.find_element_by_xpath("//*[@id=\"accountName\"]")
    time.sleep(1)
    blizzemail.send_keys(blizzemailkey)
    blizzpass = driver.find_element_by_xpath('//*[@id="password"]')
    time.sleep(1)
    blizzpass.send_keys(blizzpasskey)
    time.sleep(1)#
    blizzpass.send_keys(Keys.ENTER)
    time.sleep(6)
    driver.get('https://profile.callofduty.com/cod/login')
    time.sleep(1)
    blizz = driver.find_element_by_xpath("//*[@id=\"console-login\"]/ul/li[4]/a")
    blizz.click()
elif opt == 2:
    actemail = str(input("Enter acti email: "))
    actepass = str(input("Enter acti pass: "))
    driver.get('https://profile.callofduty.com/cod/login')
    time.sleep(1)
    actemailel = driver.find_element_by_xpath("//*[@id=\"username\"]")
    time.sleep(1)
    actemailel.send_keys(actemail)
    time.sleep(1)
    actepassel = driver.find_element_by_xpath('//*[@id="password"]')
    time.sleep(1)
    actepassel.send_keys(actepass)
    time.sleep(1)
    actepassel.send_keys(Keys.ENTER)

driver.maximize_window()
time.sleep(15)

try:
    infomissing1 = driver.find_element_by_xpath('//*[@id="first-name"]')
    time.sleep(1)
    infomissing1.send_keys("Karl")
    time.sleep(1)
    infomissing2 = driver.find_element_by_xpath('//*[@id="last-name"]')
    time.sleep(1)
    infomissing2.send_keys("Mooney")
    time.sleep(1)
    select = Select(driver.find_element_by_xpath('//*[@id="country"]'))
    time.sleep(1)
    select.select_by_visible_text("Andorra")
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id=\"register-missing\"]/div[1]/button").click()
    print("filled in info , ur welcome")

except NoSuchElementException:
    print("Now checking SB")
time.sleep(1)
driver.get("https://profile.callofduty.com/cod/info")
element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="account-profile"]/article/section[1]/section/nav/ul/li[1]')))
time.sleep(1)
element.click()
time.sleep(1)
html = driver.find_element_by_tag_name('html')
for i in range(8):
    html.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)
try:
    element2 = driver.find_element_by_xpath('//*[@id="account-profile"]/article/section[2]/section[3]/section[1]/ul/li[2]/div[1]/span[2]')
    # t = WebDriverWait(driver,10)
    # t.until(EC.visibility_of(element2))
    time.sleep(1)
except NoSuchElementException:
    print("No accounts linked- Cannot check")
counter = 0
while counter <2:
    locat = element2.location
    x = locat['x']
    y = locat['y']
    # print(x)
    # print(y)
    action = ActionChains(driver)
    action.move_to_element(element2)
    action.click()
    action.perform()
    time.sleep(3)
    try:
        sbelement = driver.find_element_by_class_name("under-review").get_attribute('outerHTML')
        sbelement = str(sbelement)
        # print(sbelement)
        bouncer = 0
        if "hidden under-review" in sbelement:
            bouncer = 1
            raise NoSuchElementException

        if bouncer == 0:
            if "under-review" in sbelement:
                # print("SHADOWBANNED")
                counter = 22
    except NoSuchElementException:
        ko = 0
    counter += 1
print(counter)
if counter == 23:
    print("Account has been shadow banned")
else:
    bouncer = 0
    print("Account is not under-review --- performing one more check")
    sbelement = driver.find_element_by_class_name("active-enforcement").get_attribute('outerHTML')
    sbelement = str(sbelement)
    if "hidden active-enforcement" in sbelement:
        bouncer = 1
    if bouncer == 0:
        if "active-enforcement" in sbelement:
            print("Last check detected active enforcement, account is SB.")
    else:
        print("Last check passed. Account is not shadow-banned")
    # print(sbelement)

# '//*[@id="unlink-account-modal"]/div[11]'
# '//*[@id="account-profile"]/article/section[2]/section[3]/section[1]/ul/li[2]/div[1]/span[2]'
# '//*[@id="account-profile"]/article/section[2]/section[3]/section[1]/ul/li[1]/div/span[2]'