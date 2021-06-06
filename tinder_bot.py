from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from web_driver_conf import get_web_driver_options
from web_driver_conf import get_chrome_web_driver
from web_driver_conf import set_ignore_certificate_error
from web_driver_conf import set_browser_as_incognito_and_no_geo
from web_driver_conf import disable_security

TINDER_URL = "https://tinder.onelink.me/9K8a/3d4abb81"
USERNAME = 'User'
PASS = 'Pass'
# ---- CHROME WEB DRIVER CONFIGURATION ----------
options = get_web_driver_options()
set_ignore_certificate_error(options)
set_browser_as_incognito_and_no_geo(options)
disable_security(options)
driver = get_chrome_web_driver(options)
wait = WebDriverWait(driver, 6)

# ------FACEBOOK LOGIN ----------
driver.get("https://facebook.com")
email = driver.find_element_by_name('email')
email.send_keys(USERNAME)
password = driver.find_element_by_name('pass')
password.send_keys(PASS)
button = driver.find_element_by_name('login')
button.click()
time.sleep(5)
# -------- TINDER LOGIN ----------
driver.get(TINDER_URL)
time.sleep(5)
# ---LOGIN WITH FACEBOOK --
button_new = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
button_new.click()


# ---- WAIT TILL LOGIN
# ----- POPUP CLOSE (REMAINING) ---
def click_button(text):
    time.sleep(5)
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{text}']")))
    login_button.click()


click_button('Allow')
time.sleep(5)  # -----ALLOW LOCATION MANUALLY ------------ and press okay

click_button('Not interested')

time.sleep(3)

# ------LIKE  ---------
condition_true = True
while condition_true:
    time.sleep(2)
    try:
        full_xpath_like = "(//div[@class='Mx(a) Fxs(0) Sq(70px) Sq(60px)--s']/button)[2]"
        swipe_like = wait.until(EC.visibility_of_element_located((By.XPATH, full_xpath_like)))
        swipe_like.click()
    except:
        time.sleep(10)
        condition_true = False